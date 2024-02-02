import json
import boto3
import datetime

client = boto3.client('events')


# import requests


def lambda_handler(event, context):
    response = client.put_events(
        Entries=[
            {
                'Time': datetime.datetime.now(),
                'Source': 'mytestapp',
                'Resources': [
                ],
                'DetailType': 'AWS API Call via CloudTrail',
                'Detail': json.dumps(event),
                'EventBusName': 'MyEventBus',
            },
        ]
    )

    return response


