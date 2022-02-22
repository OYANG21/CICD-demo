# Devops-CICD-example

Switch to `test` branch for responses to tech challenge response

Demo pipeline using Serverless Framework and Github Actions to deploy lambda functions with APIGateway RestAPI endpoint

## Design 
1. ```handler.py``` file includes lambda function code
1. Serverless Framework to deploy handler.py to AWS Lambda functions and related APIGateway resources
1. Github repo to manage source code
1. Github Action for the pipeline
    1.1 ```deploy-aws-lambda```
    1.1 ```AWS Credentials``` are stored in repo secrets

## How to run

1. Currently the workflow is triggered automatically when there is a `commit` or `merge` action on ```main``` branch
2. Actions workflow can also be maually triggered by navagating to `CiCD-demo -> Actions -> All workflows -> rerun`

### Replicate this pipeline to your own AWS environment
1. Navigate to Settings - > Secrets -> Action Secrets
2. update `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY` and save
3. run the pipeline again 

## Improvements for production ready

As this is a demo pipeline to show the techstack and workflow, there are few improvements needed to be made before production ready.
### Github and pipeline
1. Branch protection on main branch
2. Secrets management
3. unit testing & integration testing
4. Security/ code volubility scan 
5. PR valid checks, merge check for feature and dev branches

### Serverless.yml
1. add dynamic variables for different environment, aws account, resources arn, etc
2. add seperate iamrole.yml resource files for cleaner template
3. add multiple region and cross account resources sharing by output resources etc
4. add different service repos for different microservices /lambda functions

### AWS 
1. Seperate environment for dev/staging/prod by different environment or AWS accounts
2. Granular access controls, set up different IAM user roles for different job roles
3. monitoring and alerting for misconfigurations and application running alerts

## Reference
https://www.serverless.com/.

test
