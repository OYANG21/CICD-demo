import json
def lambda_handler(event, context):
    print(event)

    auth = 'Deny'
    if event['authorization'] == 'testChallenge':
        auth = 'Allow'
    else:
        auth = 'Deny'

    authResponse = {    "principalID": "testChallenge", 
                        "policyDocument": 
                        {   "Version":"2012-10-17",
                            "Statement":
                                [ 
                                    {   "Action": 
                                        "execute-api":Invoke",
                                        "Resource":[
                                            "arn:aws:execute-api:us-east-1:811620960246:ht9nrqipl6/*/*"],
                                            # Update to the target API arn
                                    "Effect": auth
                                } 
                            ] 
                        } 
                    }
    return authResponse