# Serverless Image Processing Pipeline

## Overview
This project implements a serverless image processing pipeline on AWS. It automatically resizes uploaded images and tracks metadata.

### Used Services
- **AWS S3** – for storing original and processed images
- **AWS Lambda** – for image processing logic
- **AWS DynamoDB** – for storing image metadata
- **Python** – scripting language
- **Pillow** – Python library for image manipulation
- **boto3** – AWS SDK for Python

## How It Works
1. A user uploads an image to the `upload` S3 bucket.
2. An S3 event triggers the Lambda function.
3. Lambda:
   - Downloads the uploaded image
   - Resizes the image (max 800x800)
   - Uploads the processed image to the `processed` S3 bucket
   - Records metadata in DynamoDB (original & processed file names, sizes, upload timestamp, bucket info)
4. Fully serverless workflow; no manual intervention needed.
