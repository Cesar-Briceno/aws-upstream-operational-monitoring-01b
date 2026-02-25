from decimal import Decimal
import json
import random
import uuid
import time
from datetime import datetime
import boto3
import os

dynamodb = boto3.resource('dynamodb')
sns = boto3.client('sns')

THRESHOLD_TABLE = os.environ.get('THRESHOLD_TABLE')
EVENTS_TABLE = os.environ.get('EVENTS_TABLE')
SNS_TOPIC_ARN = os.environ.get('SNS_TOPIC_ARN')


def get_threshold(asset_id, variable):
    table = dynamodb.Table(THRESHOLD_TABLE)
    response = table.get_item(
        Key={
            "asset_id": asset_id,
            "variable": variable
        }
    )
    return response.get("Item")


def lambda_handler(event, context):

    asset_id = "WELL-01"

    # Simulación de variables operativas
    rop = round(random.uniform(5, 40), 2)
    torque = round(random.uniform(5, 30), 2)
    standpipe_pressure = round(random.uniform(2000, 4500), 2)
    mud_density = round(random.uniform(1.0, 2.2), 2)

    variables = {
        "rop": rop,
        "torque": torque,
        "standpipe_pressure": standpipe_pressure,
        "mud_density": mud_density
    }

    detected_event = None

    for variable_name, value in variables.items():

        threshold = get_threshold(asset_id, variable_name)

        if not threshold:
            continue

        min_value = threshold.get("min")
        max_value = threshold.get("max")

        if min_value is not None and value < float(min_value):
            detected_event = {
                "variable": variable_name,
                "threshold_type": "MIN",
                "threshold_value": min_value
            }

        if max_value is not None and value > float(max_value):
            detected_event = {
                "variable": variable_name,
                "threshold_type": "MAX",
                "threshold_value": max_value
            }

        if detected_event:
            break

    if not detected_event:
        return {
            "statusCode": 200,
            "body": json.dumps({"message": "No anomaly detected"})
        }

    # Construcción del evento
    event_id = str(uuid.uuid4())
    timestamp = int(time.time())

    variable_name = detected_event["variable"]
    threshold_type = detected_event["threshold_type"]
    threshold_value = detected_event["threshold_value"]

    measured_value = variables[variable_name]

    severity = "HIGH"

    event_item = {
        "event_id": event_id,
        "asset_id": asset_id,
        "variable": variable_name,
        "measured_value": Decimal(str(measured_value)),
        "severity": severity,
        "timestamp": timestamp
    }

    if threshold_type == "MIN":
        event_item["min_threshold"] = Decimal(str(threshold_value))

    if threshold_type == "MAX":
        event_item["max_threshold"] = Decimal(str(threshold_value))

    # Guardar en DynamoDB
    events_table = dynamodb.Table(EVENTS_TABLE)
    events_table.put_item(Item=event_item)

    # Publicar en SNS
    sns.publish(
        TopicArn=SNS_TOPIC_ARN,
        Subject="Operational Alert",
        Message=json.dumps(event_item, default=str)
    )

    return {
        "statusCode": 200,
        "body": json.dumps(event_item, default=str)
    }
