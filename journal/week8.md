# Week 8 — Serverless Image Processing


### Content

1. [Objetives](#Objetives)
2. [Week summary](#Week-summary)
3. [AWS Services used](#AWS-Services-used)
4. [Week content](#Week-content)
5. [Implementation notes](#Implementation-notes)

Implement CDK Stack
Serving Avatars via CloudFront
Backend and Frontend for Profile Page
DB Migration
Implement Avatar Uploading
Double Check Environment Variables
   
7. [Implementation instructions](https://github.com/PericoLedesma/aws-bootcamp-cruddur-2023/blob/main/journal/week_instructions/week8.md)

----------------------------------------------------------------

### Objetives
- Basic knowledge of writing, deploying, and logging serverless functions
- Basic knowledge of working with serverless object storage
- Basic knowledge of working with event-bus actions



### Week Summary
- Test our JavaScript code to use Sharp and process a thumbnail
- Write an AWS Lambda function
- Deploy our Lambda function
- Create an S3 Bucket
- Create an S3 Event Notification to process images upload to S3 and deposit them back in the bucket
- Implement basic file upload to S3 client-side



### AWS Services used
S3
Budgets
SDK
cloudfront

# Week content
[(Back to index)](#content)k content

SDK with typescript
Layers or constract of SDK AWS 
Cloudformation

What is bootstrap 

cdk bootstrap "aws://528963888625/eu-central-1" 

bootstrap and we can see it in cloudformation
![Proof of work](assets/week6/cdk_cloudformation.png)


cdk deploy

differences between put and post

we are going to put the images in cloudfront cdn


We created a endpoint to cloudfront to the s3 bucket 

https://assets.mycruddurapp.com/avatars/processed/data.jpg

To install the client s3 

npm i @aws-sdk/client-s3 --save

To generate the uploading url

cd to cruddur-upload-file and them bundle exec ruby function.rb

Another for crudduur-upload-file  - npm install aws-jwt-verify --save

![Proof of work](assets/week6/ecs_cluster.png)

-------------------------------

# Implementation notes
[(Back to index)](#content)




![Proof of work](assets/week6/ecs_cluster.png)
