import json
import logging


def hello(event, context):
    body = {
        "message": "Go Serverless v3.0! Your function executed successfully!",
        "input": event,
    }

    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    logger.info('this is test')

    response = {"statusCode": 200, "body": json.dumps(body)}

    return response
