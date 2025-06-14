provider "aws" {
  region = "eu-west-1"
}


# START IAM
resource "aws_iam_role" "msk_iam_role" {
  name = "msk-iam-role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Effect = "Allow"
        Principal = {
          Service = "kafka.amazonaws.com"
        }
        Action = "sts:AssumeRole"
      },
       {
        Effect = "Allow"
        Principal = {
          AWS = "arn:aws:sts::575240114042:assumed-role/AWSReservedSSO_NW-Administrator_f8ac33acfdb00c27/pedro.nieto@new-work.se"
        }
        Action = "sts:AssumeRole"
      }
    ]
  })
}

resource "aws_iam_policy" "msk_iam_policy" {
  name        = "msk-iam-policy"
  description = "Policy for MSK IAM authentication"
  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Effect = "Allow"
        Action = "kafka-cluster:*"
        Resource = "*"
      }
    ]
  })
}

resource "aws_iam_role_policy_attachment" "msk_iam_role_policy_attachment" {
  role       = aws_iam_role.msk_iam_role.name
  policy_arn = aws_iam_policy.msk_iam_policy.arn
}

# END IAM
resource "aws_msk_cluster" "example" {
  cluster_name           = var.msk_cluster_name
  kafka_version          = "3.6.0"
  number_of_broker_nodes = var.msk_number_of_broker_nodes
  
  broker_node_group_info {
    instance_type   = var.msk_broker_instance_type
    client_subnets  = var.subnet_ids
    security_groups = var.security_group_ids
    connectivity_info {
      public_access {
        #type = "SERVICE_PROVIDED_EIPS"
        type = "DISABLED"
      }
    }
  }

  client_authentication {
    sasl {
      iam = true
    }
  }


#   client_authentication {
#     unauthenticated = "true"
#   }

  encryption_info {
    encryption_in_transit {
      client_broker = "TLS"
      in_cluster    = true
    }
  }
#   encryption_info {
#     encryption_in_transit {
#       client_broker = "PLAINTEXT"
#       in_cluster    = false
#     }
#   }  

  configuration_info {
    arn      = aws_msk_configuration.example.arn
    revision = aws_msk_configuration.example.latest_revision
  }

  tags = {
    Name = var.msk_cluster_name
  }
}

resource "aws_msk_configuration" "example" {
  name            = "kafka-configuration"
  kafka_versions  = ["3.6.0"]
  server_properties = <<PROPERTIES
auto.create.topics.enable = true
delete.topic.enable = true
PROPERTIES
}