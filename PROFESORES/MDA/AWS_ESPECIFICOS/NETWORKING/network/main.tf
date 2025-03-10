provider "aws" {
  alias = "master_region"
}

resource "aws_vpc" "main" {
  provider = aws.master_region
  cidr_block = var.vpc_cidr_block
  tags = {
    Name = "Main VPC"
  }
}

resource "aws_subnet" "public_subnets" {
  provider = aws.master_region
  count = 3
  cidr_block = var.public_cidr_blocks[count.index]
  vpc_id     = aws_vpc.main.id
  availability_zone = var.availability_zones[count.index]
  tags = {
    Name = "public_subnet_${var.availability_zones[count.index]}"
  }
}

resource "aws_subnet" "private_subnets" {
  provider = aws.master_region
  count = 3
  cidr_block = var.private_cidr_blocks[count.index]
  vpc_id     = aws_vpc.main.id
  availability_zone = var.availability_zones[count.index]
  tags = {
    Name = "private_subnet_${var.availability_zones[count.index]}"
  }
}

resource "aws_internet_gateway" "internet_gateway" {
  provider = aws.master_region
  vpc_id = aws_vpc.main.id
}

resource "aws_eip" "elastic_ip" {
  provider = aws.master_region
  domain = "vpc"
  depends_on = [
    aws_internet_gateway.internet_gateway
  ]
}

resource "aws_nat_gateway" "nat_gateway" {
  provider = aws.master_region
  subnet_id = aws_subnet.public_subnets[0].id
  allocation_id = aws_eip.elastic_ip.id
}

resource "aws_route_table" "public_route_table" {
  provider = aws.master_region
  vpc_id = aws_vpc.main.id
  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.internet_gateway.id
  }
  tags = {
    Name = "subnet_public_route_table"
  }
}

resource "aws_route_table" "private_route_tables" {
  provider = aws.master_region
  count = length(aws_subnet.private_subnets)
  vpc_id = aws_vpc.main.id
  route {
    cidr_block = "0.0.0.0/0"
    nat_gateway_id = aws_nat_gateway.nat_gateway.id
  }
  tags = {
    Name = "subnet_private_route_table_${count.index}"
  }
}

resource "aws_route_table_association" "public_route_table_associations" {
  provider = aws.master_region
  count = length(aws_subnet.public_subnets)
  route_table_id = aws_route_table.public_route_table.id
  subnet_id = aws_subnet.public_subnets[count.index].id
}

resource "aws_route_table_association" "private_route_table_associations" {
  provider = aws.master_region
  count = length(aws_route_table.private_route_tables)
  route_table_id = aws_route_table.private_route_tables[count.index].id
  subnet_id = aws_subnet.private_subnets[count.index].id
}