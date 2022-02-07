#include .env

stack-set-name = "Test"

validate-template:
	@aws cloudformation validate-template  --template-body file://CloudCFTemplate.yaml

deploy-template:
	@echo "Creating cloudformation resources from template "
	@aws cloudformation create-stack \
		--stack-name $(stack-set-name) \
		--parameters ParameterKey=MyName,ParameterValue=test \
		--template-body file://CloudCFTemplate.yaml \
		--capabilities CAPABILITY_IAM
		--tags \
			Key=Owner,Value="test";
	@echo "Successfully Created stack set"	
