import json
import boto3
import pyjokes


def get_joke(event, context):
        body = {
        "message": "Greetings from Githun. Your function is deployed by a Github Actions. Enjoy your joke",
        "joke": pyjokes.get_joke()
        }
        response = {
        "statusCode": 200,
        "body": json.dumps(body)
        }
        return response

def dynamo_itemcreate(team_name, team_country, team_desc, team_rating):
        dynamodb = boto3.client('dynamodb')
        db_name = "Challenge_DB"
        dynamodb.put_item(TableName=db_name, Item={'country':{'S':team_country}, 'team':{'S':team_name}, 'desc':{'S':team_desc}, 'rating':{'S':team_rating}})

def lambda_handler(event, context):
        print('Team Country: %s' % event['team_country'])
        print('Team Name: %s' % event['team_name'])
        print('Team Description: %s' % event['team_desc'])
        print('Team Rating: %s' % event['team_rating'])
        dynamo_itemcreate(event['team_name'], event['team_country'], event['team_desc'],event['team_rating'])