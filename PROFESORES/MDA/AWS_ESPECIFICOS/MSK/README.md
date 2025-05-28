## MSK AWS - Create a MSK

### Objectives

Create an MSK Cluster with the following configuration

1.- Create an MSK with 3 brokers
    1.- Apache Kafka version 3.6.0
    2.- 3 brokers
    3.- 3 availability zones





To get the values from previous exercise:

VPC ID

```bash
aws ec2 describe-vpcs --region eu-west-1 --query 'Vpcs[*].VpcId' --output text
```


SubnetIds Public

```bash
aws ec2 describe-subnets --region eu-west-1 --query 'Subnets[*].SubnetId' --output text
```

Security Groups

```bash
aws ec2 describe-security-groups --region eu-west-1 --query 'SecurityGroups[*].GroupId' --output text
```