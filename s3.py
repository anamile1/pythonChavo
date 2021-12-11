import boto3  
from flask import jsonify
import requests
def serviceS3():
    url=""

    OBJECT_NAME_TO_UPLOAD = "foto1.jpg"
    try:
        s3_client = boto3.client(
            's3',
            aws_access_key_id="AKIAQ3F23YO3DDIMRMGF",
            aws_secret_access_key="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"
        )

        #Generate the presigned URL
        response = s3_client.generate_presigned_post(
            Bucket = 'chavo',
            Key = OBJECT_NAME_TO_UPLOAD,
            ExpiresIn = 10 
        )
        print(response)
        #Upload file to S3 using presigned URL
        files = { 'file': open(OBJECT_NAME_TO_UPLOAD, 'rb')}
        r = requests.post(response['url'], data=response['fields'], files=files)
        print(r.status_code)

        print(response["url"])
        print(response["fields"]["key"])
        url=f"{response['url']}{response['fields']['key']}"
        print(url)
        return url
    except:
        return jsonify({"Message":"Permisos amazon"})

serviceS3()