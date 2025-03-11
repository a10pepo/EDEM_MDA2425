provider "aws" {
  region = "us-east-1"
}

resource "aws_s3_bucket" "this" {
  bucket = var.s3_name


  tags = {
    Name = var.s3_name
  }
}

resource "aws_s3_bucket_policy" "this" {
  bucket = aws_s3_bucket.this.bucket

  policy = jsonencode({
    Version = "2008-10-17"
    Id      = "PolicyForCloudFrontPrivateContent"
    Statement = [
      {
        Sid       = "AllowCloudFrontServicePrincipal"
        Effect    = "Allow"
        Principal = {
            Service = "cloudfront.amazonaws.com"
        }
        Action   = "s3:GetObject"
        Resource  = "arn:aws:s3:::${aws_s3_bucket.this.bucket}/*"
        Condition = {
          StringEquals = {
            "AWS:SourceArn" = "${aws_cloudfront_distribution.this.arn}"
          }
        }
      },
    ]
  })
}


resource "aws_s3_object" "index" {
  bucket = aws_s3_bucket.this.bucket
  key    = "index.html"
  source = "index.html"
  content_type = "text/html"

}

resource "aws_cloudfront_origin_access_control" "this" {
  name                              = "cloudfront-s3-access-control"
  description                       = "cloundfront-access-s3"
  origin_access_control_origin_type = "s3"
  signing_behavior                  = "always"
  signing_protocol                  = "sigv4"
}

resource "aws_cloudfront_distribution" "this" {
  enabled = true
  default_root_object = "index.html"

  origin {
    domain_name = aws_s3_bucket.this.bucket_regional_domain_name
    origin_id   = "${var.s3_name}-origin"
    origin_access_control_id = aws_cloudfront_origin_access_control.this.id
    
  }

  default_cache_behavior {
    target_origin_id = "${var.s3_name}-origin"
    allowed_methods  = ["GET", "HEAD"]
    cached_methods   = ["GET", "HEAD"]

    forwarded_values {
      query_string = true

      cookies {
        forward = "all"
      }
    }

    viewer_protocol_policy = "allow-all"
    min_ttl                = 0
    default_ttl            = 0
    max_ttl                = 0
  }

  restrictions {
    geo_restriction {
      restriction_type = "none"
    }
  }

  viewer_certificate {
    cloudfront_default_certificate = true
  }

  price_class = "PriceClass_200"
}