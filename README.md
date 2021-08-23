# Nostos-Genomics-Interview-Project
  This is a SAM template file to build decimal to roman number function
  it uses python3.8 docker image and put app.py which contains business logic
  This is a serverless project for Nostos Genomics Interview Progress. 
  It includes a decimal number to roman number converter AWS lambda function which works as an image(no zip) and AWS api gateway to test it easier

# Using
- Execute **sam build** and **sam deploy** in orderly to if code is changed or to create from scratch
- Execute **sam local invoke -e ./events/decimal_success.json** to test lambda function locally.  Docker enginge should be working for local development and testing
- Fill **./tests/test.sh** first with **api key** and execute it. The payload is only data for request body no need to send full http-request here because 
 api gateway will transform it.
- Need api key and will be provided by email due not to add any secret key git history

# Elements
- Sam Template
- AWS Api Gateway
- AWS Lambda Function
- AWS Elastic Container Registry
- Python3.8
- Docker


## Sam Template
Sam is not only resource definition template, it is also build tool and create needing resources
Sam template named as **template.yaml** and located in **./decimal_to_roman/template.yaml**
It has resource definitions of Api Gateway and Lambda Function. Whenever **sam build** command executed, it builds project and docker image using **./decimal_to_roman/Dockerfile** and create **.aws-sam** folder.  
**.aws-sam** folder includes compiled **template.yaml** file which merge data from **sam build** params and **build.toml** is for image definitions
Sam template create roles under the hood in contrast to native cloudformation. 

## AWS Api Gateway
It is described in template.yaml and binded to lambda function in order to call it. **ApiKeyRequired** is enabled to prevent abusing api gateway. So api keys created for the users. **x-api-key: <api-key>** should be added to header of request. Api has has only 1 endpoint and http-medhod which is post : **<apigateway>/decimaltoroman**

## AWS Lambda Function
It is described in **template.yaml** and binded to api gateway by using **Events** section

## AWS Elastic Container Registry
When **create_ecr_repo.sh** is executed needing ecr repository will be created. Usual deployment progress doesn't to create repo once it is created. When **sam deploy** is executed sam publish already built docker image to ECR repo by checking build.toml

## Python3.8
Even Python is not installed build and deployment phased of project can work due to pulling python runtime docker.

## Docker
Key point of easy shipment is docker. Even **lambda**  has different virtulization technology than docker  it accepts docker images. **lambda** use use more performant way similar to https://firecracker-microvm.github.io/ because it excluded needless implementation as new **containerd** is doing


## Cons
- Api key is not working with postman although it is working with **curl**
- ECR repo creation could be done by template.yaml
- Prod and test enviroment deployments could be done by using parameters in template.yaml
