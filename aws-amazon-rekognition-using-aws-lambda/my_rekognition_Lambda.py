import json
import boto3
def lambda_handler(event, context):
   
    bucket_name = "whizlabs.rekognition.2512"
    image_obj_name = event['image_name']

    try:
        rkClient = boto3.client("rekognition", region_name="us-east-1")
        try:
            rkResponse = rkClient.detect_labels(
                Image={
                    'S3Object': {
                        'Bucket': bucket_name,
                        'Name': image_obj_name
                    }
                },
            )
            print(rkResponse['Labels'])
            return rkResponse['Labels']
        except Exception as e:
            print("Get labels failed because ", e)
    except Exception as e:
        print("Client connection to Rekognition failed because ", e)