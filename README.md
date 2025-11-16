# Serverless Image Processing Pipeline

## Overview
This project implements a fully serverless image processing workflow using AWS services. When an image is uploaded to S3, it is automatically resized, saved to a processed bucket, and metadata is recorded in DynamoDB. The system is fully event-driven and requires no servers or manual intervention.

## Technologies Used
- **AWS S3** – Storage for original and processed images  
- **AWS Lambda** – Executes image processing code  
- **AWS DynamoDB** – Stores image metadata  
- **Python** – Lambda runtime  
- **Pillow (PIL)** – Image resizing and manipulation  
- **boto3** – AWS SDK for Python  

## How It Works
1. A user uploads an image to the **upload S3 bucket**.  
2. The upload triggers the **Lambda function** through an S3 event.  
3. The Lambda function:
   - Downloads the uploaded image  
   - Resizes it to a maximum of **800×800 pixels**  
   - Uploads the processed version to the **processed bucket** with a `_processed` suffix  
   - Records metadata in **DynamoDB**, including:
     - Original and processed file names  
     - Sizes of both images  
     - Upload timestamp  
     - Upload and processed bucket names  
4. The workflow runs entirely serverlessly and scales automatically.
