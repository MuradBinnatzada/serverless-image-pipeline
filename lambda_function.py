import boto3
import os
from PIL import Image
import io
from datetime import datetime

# S3 client
s3 = boto3.client('s3')

# DynamoDB client
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('ImageMetadata')

UPLOAD_BUCKET = 'murad-project-image-upload'
PROCESSED_BUCKET = 'murad-project-image-processed'

def lambda_handler(event, context)
    for record in event['Records']
        try
            bucket = record['s3']['bucket']['name']
            key = record['s3']['object']['key']

            # Download the image from S3
            response = s3.get_object(Bucket=bucket, Key=key)
            image_data = response['Body'].read()

            # Open image and resize
            image = Image.open(io.BytesIO(image_data))
            image.thumbnail((800, 800))  # resize to max 800x800

            # Save to bytes
            buffer = io.BytesIO()
            image_format = image.format if image.format else 'PNG'
            image.save(buffer, format=image_format)
            buffer.seek(0)

            # Processed file name
            name, ext = os.path.splitext(key)
            processed_key = f{name}_processed{ext if ext else '.' + image_format.lower()}

            # Upload processed image to S3
            s3.put_object(
                Bucket=PROCESSED_BUCKET,
                Key=processed_key,
                Body=buffer,
                ContentType=fimage{image_format.lower()}
            )

            # Prepare metadata
            upload_timestamp = datetime.utcnow().isoformat() + Z

            table.put_item(
                Item={
                    'image_id' key,  # original key as unique id
                    'original_name' key,
                    'processed_name' processed_key,
                    'original_size' response['ContentLength'],
                    'processed_size' len(buffer.getvalue()),
                    'content_type' fimage{image_format.lower()},
                    'upload_bucket' bucket,
                    'processed_bucket' PROCESSED_BUCKET,
                    'upload_timestamp' upload_timestamp
                }
            )

        except Exception as e
            print(fError processing {key} {e})

    return {'status' 'success'}
