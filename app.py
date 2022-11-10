import json
import boto3
import numpy as np

def handler(event, context):
    inp = event['Input']
    res = int(4*(inp))

    return {
        'statusCode': 200,
        'body': res
    }