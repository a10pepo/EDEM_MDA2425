## VPC AWS - Create a VPC

### Objectives

1. Create a VPC
    1. Use base CIDR 10.1.0.0/16 and region us-east-1
    2. It must have 3 public subnets
        1. us-east-1a with CIDR block 10.1.1.0/24 PublicSubnetAza
        2. us-east-1b with CIDR block 10.1.2.0/24 PublicSubnetAzb
        3. us-east-1c with CIDR block 10.1.3.0/24 PublicSubnetAzc
    3. It must have 3 private subnets
        1. us-east-1a with CIDR block 10.1.11.0/24 PrivateSubnetAza
        2. us-east-1b with CIDR block 10.1.12.0/24 PrivateSubnetAzb
        3. us-east-1c with CIDR block 10.1.13.0/24 PrivateSubnetAzc
    4. The public subnets should share route table
    5. The private subnets should have a route table each one
    6. The private subnets should have internet access