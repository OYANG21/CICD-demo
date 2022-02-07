import json
import logging
import boto3

def lambda_handler(event, context):
   txt = ""
   myeventID = ""
   m = ""

   for record in event['Records']:
      txt = txt + record['eventName']

   for record in event['Records']:
      myeventID = record['eventID']

   n = str(len(event['Records']))
   k = record['dynamodb']['Keys']['username']['S']
   m = 'Successfully processed %s records. Keys: %s.' % (n, k)
   message = {"message": m}

   client = boto3.client('sns')
   response = client.publish(
      TargetArn = "arn:aws:sns:eu-central-1:111111111111:DynamoDBItemChanges",
      Message = json.dumps({'default': json.dumps(message)}),
      MessageStructure = 'json'
   )

   s3 = boto3.resource('s3')
   s3bucket = 'dynamodbstreamdata'
   fname = 'SampleDynamoDBTable/CDC/' + str(myeventID) + '.json'
   s3object = s3.Object(s3bucket, fname)
   s3object.put(
      Body=(bytes(json.dumps(event).encode('UTF-8')))
   )
   return {
      'statusCode': 200,
      'body': json.dumps('-' + txt + '-')
   }