# serverless_restapi_create
import json
import logging
import os
import time
import uuid
from datetime import datetime

import boto3

dynamodb = boto3.resource('dynamodb')


def create(event, context):
    data = json.loads(event['body'])
    if 'text' not in data:
        logging.error("Validation Failed")
        raise Exception("Couldn't create the todo item.")

    timestamp = str(datetime.utcnow().timestamp())

    table = dynamodb.Table('qyt_serverless_table')

    item = {'id': str(uuid.uuid1()), 'text': data['text'], 'checked': False, 'createdAt': timestamp,
        'updatedAt': timestamp, }

    # write the todo to the database
    table.put_item(Item=item)

    # create a response
    response = {"statusCode": 200, "body": json.dumps(item)}

    return response
