import json

# import requests


def lambda_handler(event, context):
    print(event)
    print("task Update")
    print("Sample Update")
    print("Locla Update")
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "hello world",
            # "location": ip.text.replace("\n", "")
        }),
    }
