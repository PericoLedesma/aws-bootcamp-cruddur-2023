# Week 5 — DynamoDB and Serverless Caching

[Week 5: Unofficial Homework Guide](https://www.linuxtek.ca/2023/03/19/aws-cloud-project-bootcamp-week-5-unofficial-homework-guide/)

### Content

1. [Objetives](#Objetives)
2. [Week summary](#Week-summary)
3. [AWS Services used](#AWS-Services-used)
4. [Week content](#Week-content)
5. [Implementation notes](#Implementation-notes)
    - [Backend Preparation](##Backend-Preparation)
    - [DynamoDB Utility Scripts](##DynamoDB-Utility-Scripts)
    - [Implement Conversations with DynamoDB Local}(##Implement-Conversations-with-DynamoDB-Local)
    - [Implement DynamoDB Stream with AWS Lambda](##Implement-DynamoDB-Stream-with-AWS-Lambda)
7. [Implementation instructions](https://github.com/PericoLedesma/aws-bootcamp-cruddur-2023/blob/main/journal/week_instructions/week4.md)


### Objetives
- Be able to data model using single table design
- Basic knowledge of working with a cloud SDK
- Basic implementation of read-aside cache in front of a database
- Interact with a production NoSQL database
- Basic knowledge of working with an OLTP



### Week Summary

- Have a lecture about data modeling (Single Table Design) for NoSQL
- Launch DynamoDB local
- Seed our DynamoDB tables with data using Faker
- Write AWS SDK code for DynamoDB to query and scan put-item, for predefined endpoints
- Create a production DynamoDB table
- Update our backend app to use the production DynamoDB
- Add a caching layer using Momento Severless Cache


# Week content
[(Back to index)](#content)

### DynamoDB

[Amazon DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Introduction.html) is a fully managed NoSQL database service that provides fast and predictable performance with seamless scalability

#### [Partition and sort key:](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.CoreComponents.html#HowItWorks.CoreComponents.TablesItemsAttributes)
- Partition key – A simple primary key, composed of one attribute known as the partition key. DynamoDB uses the partition key's value as input to an internal hash function. The output from the hash function determines the partition (physical storage internal to DynamoDB) in which the item will be stored. 

- Partition key and sort key – Referred to as a composite primary key, this type of key is composed of two attributes. The first attribute is the partition key, and the second attribute is the sort key. All items with the same partition key value are stored together, in sorted order by sort key value. In a table that has a partition key and a sort key, it's possible for multiple items to have the same partition key value. However, those items must have different sort key values.

#### [PartQL](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/ql-reference.html)

PartiQL provides SQL-compatible query access across multiple data stores containing structured data, semistructured data, and nested data. It is widely used within Amazon and is now available as part of many AWS services, including DynamoDB.

https://docs.aws.amazon.com/es_es/amazondynamodb/latest/developerguide/ql-reference.html


#### [NoSQL Workbench for DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/workbench.html)

NoSQL Workbench for Amazon DynamoDB is a cross-platform, client-side GUI application that you can use for modern database development and operations.

[Amazon DynamoDB Accelerator (DAX)](https://aws.amazon.com/dynamodb/dax/)
Amazon DynamoDB Accelerator (DAX) is a fully managed, highly available, in-memory cache for Amazon DynamoDB that delivers up to a 10 times performance improvement—from milliseconds to microseconds—even at millions of requests per second.

GSI and LSI stand for Global Secondary Index and Local Secondary Index respectively. Here are the key differences between them:

1. Definition: A GSI is a secondary index that is defined on a table and spans all its partitions, while an LSI is a secondary index that is defined on a table and is local to a single partition.
2. Scope: GSIs are available to all queries that access the table, while LSIs are only available to queries that access the partition on which they are defined.
3. Key attributes: A GSI can have any attribute(s) of the table as its key, while an LSI must have the same partition key as the table and one or more non-key attributes.
4. Performance: GSIs can provide better query performance for certain types of queries that are not covered by the primary key or LSIs. However, they also have some overhead in terms of storage and write performance. LSIs have lower overhead and can provide faster query performance for queries that involve the partition key and the LSI's non-key attributes.
5. Usage: GSIs are typically used to support queries that require filtering or sorting based on attributes other than the table's primary key, while LSIs are typically used to support queries that involve the partition key and a few other attributes.

Overall, the choice between GSI and LSI depends on the specific requirements of the application and the types of queries that need to be supported.

Important to think when designing databases:
- What are my access pattern?
- What data do we need?
- What is the frequency?

Single Table Design is a data modelling technique in which all related data is stored in a single database table

# Implementation notes
[(Back to index)](#content)

We are going to use single table desing. We do it with DynamoDB for the Direct Messaging System in our Cruddur application. Here, data access can be break down into four patterns:

1. Pattern A for showing messages. Users can see a list of messages that belong to a message group.
2. Pattern B for showing message groups. Users can see a list of message groups so they can check the other persons they have been talking to.
3. Pattern C for creating a new message in a new message group.
4. Pattern D for creating a new message in an existing message group.

Accordingly, there are 3 types of items to put in our DynamoDB table.

```
my_message_group = {
    'pk': {'S': f"GRP#{my_user_uuid}"},
    'sk': {'S': last_message_at},
    'message_group_uuid': {'S': message_group_uuid},
    'message': {'S': message},
    'user_uuid': {'S': other_user_uuid},
    'user_display_name': {'S': other_user_display_name},
    'user_handle':  {'S': other_user_handle}
}

other_message_group = {
    'pk': {'S': f"GRP#{other_user_uuid}"},
    'sk': {'S': last_message_at},
    'message_group_uuid': {'S': message_group_uuid},
    'message': {'S': message},
    'user_uuid': {'S': my_user_uuid},
    'user_display_name': {'S': my_user_display_name},
    'user_handle':  {'S': my_user_handle}
}

message = {
    'pk':   {'S': f"MSG#{message_group_uuid}"},
    'sk':   {'S': created_at},
    'message': {'S': message},
    'message_uuid': {'S': message_uuid},
    'user_uuid': {'S': my_user_uuid},
    'user_display_name': {'S': my_user_display_name},
    'user_handle': {'S': my_user_handle}
}

```

## Backend Preparation## DynamoDB Utility Scripts

Restructure bash scripts so that there are 3 folders storing utility commands for Postgres database (`backend-flask/bin/db`), DynamoDB (`backend-flask/bin/db`), AWS RDS (`backend-flask/bin/rds`) and AWS Cognito (`backend-flask/bin/cognito`).

Add `boto3` into `backend-flask/requirements.txt`, which is the AWS SDK for Python to create, configure, and manage AWS services such as DynamoDB.

For the local Postgres database:

- Update seed data in `backend-flask/db/seed.sql` to have 3 users and 1 activity (NOTE: set one user the same as the one you used for cruddur signin to avoid potential data conflicts).
- Create `backend-flask/bin/cognito/list-users` to list users data saved in AWS Cognito.
- Create `backend-flask/bin/db/update_cognito_user_ids` to update users in the seed data with actual Cognito IDs if exist.
- Set `CONNECTION_URL: "postgresql://postgres:password@db:5432/cruddur"` in `docker-compose.yml`, because this week we are working with the users data queried from the local Postgres database named `cruddur`.

Add `python "$bin_path/db/update_cognito_user_ids"` to run `backend-flask/bin/db/update_cognito_user_ids` in the end of `backend-flask/bin/db/setup`. If we compose up the docker and run the setup script, it will create a local Postgres database named `cruddur` with 2 tables. In the `users` table, 1 user with handle `pedro_user` will be updated with actual AWS Cognito ID, which matches the value if we check with `./bin/cognito/list-users` as shown in the screenshot below.


## DynamoDB Utility Scripts

In the directory `backend-flask/bin/ddb/`, create the following utility scripts to easily setup, teardown, and debug DynamoDB data.

- `schema-load`: create a table named `cruddur-messages` either for DynamoDB local or on the AWS
- `list-tables`: list the name of tables we created
- `drop`: drop a table by its name, e.g. `drop cruddur-messages`
- `seed`: load the seed data into the table `cruddur-messages` with hard-coded `message_group_uuid` (**NOTE**: to avoid potential data conflict, I replaced `my_handle` from `andrewbrown` to `pedro_user`
- `scan`: scan all the items saved in the table `cruddur-messages`
- `patterns/get-conversation`: list messages associated with the hard-coded `message_group_uuid` and print the consumed capacity
- `patterns/list-conversations`: list message groups and print the consumed capacity (NOTE: this script uses functions from `backend-flask/lib/db.py`)

Then we can run `./bin/ddb/schema-load` and then `./bin/ddb/seed` to actually load the seed data into our local DynamoDB. The terminal will print out info as seen in the screenshot below.

## Implement Conversations with DynamoDB Local

Firstly, create `backend-flask/lib/ddb.py` which creates `class Ddb` to reuse its functions in other scripts. Since this section is to work with local Dynamodb, set `AWS_ENDPOINT_URL: "http://dynamodb-local:8000"` in `docker-compose.yml`.

Update/create routes and functions in the backend to get messages and message groups from Dynamodb instead of hard-coded data; Instead of passing in `handle`, pass `message_group_uuid`; These implementations mainly use `list_message_groups` and `list_messages` of the `Ddb` class:

- `backend-flask/app.py` (mainly, instead of using `"/api/messages/@<string:handle>"`, use `"/api/messages/<string:message_group_uuid>"`)
- `backend-flask/services/message_groups.py`
- `backend-flask/services/messages.py`
- Create `backend-flask/db/sql/users/uuid_from_cognito_user_id.sql`
- Change `backend_url` from using `${handle}` to `${params.message_group_uuid}` in `frontend-react-js/src/pages/MessageGroupPage.js`
- Change path from `"/messages/@:handle"` to `"/messages/:message_group_uuid"` in `frontend-react-js/src/App.js`
- Change `params.handle` to `params.message_group_uuid` and `props.message_group.handle` to `props.message_group.uuid` in `frontend-react-js/src/components/MessageGroupItem.js`

Update authentication in the frontend:

- Create `frontend-react-js/src/lib/CheckAuth.js` which can be reused in other scripts for authentication
- `frontend-react-js/src/pages/HomeFeedPage.js`
- `frontend-react-js/src/pages/MessageGroupPage.js`
- `frontend-react-js/src/pages/MessageGroupsPage.js`
- `frontend-react-js/src/components/MessageForm.js`

Implementation of creating a new message, which mainly uses `create_message` of the `Ddb` class:

- Update the content for `body` in `frontend-react-js/src/components/MessageForm.js`
- Update function `data_create_message` in `backend-flask/app.py`
- Update `backend-flask/services/create_message.py` which has two modes - "update" the new message to an existing message group, or "create" the new message with a new message group
- Create `backend-flask/db/sql/users/create_message_users.sql`

Implementation for extra pages, which mainly uses `create_message_group` of the `Ddb` class:

- Import `MessageGroupNewPage` from `./pages/MessageGroupNewPage` and add the corresponding router in `frontend-react-js/src/App.js`
- Create `frontend-react-js/src/pages/MessageGroupNewPage.js`
- Create `frontend-react-js/src/components/MessageGroupNewItem.js`
- Add the endpoint and function for user short in `backend-flask/app.py`
- Create `backend-flask/services/users_short.py`
- Create `backend-flask/db/sql/users/short.sql`
- Update `frontend-react-js/src/components/MessageGroupFeed.js`
- Update `frontend-react-js/src/components/MessageForm.js`

After completing the above steps, compose up and go to the frontend, sign in and visit the messages tab, it shows the seed data. If I send a direct message to Bayko, the message will be presented in the bottom of the current message group:

![Proof of working messages]()

We can visit url `https://<frontend_address>/messages/new/<handle>` to create and update new messages in a new message group with Bayko (set the url handle to `bayko`), or start a conversation with Londo (set the url handle to `londo`) as seen in the screenshots below.

![Proof of messages with bayko])

![Proof of messages with londo]()

## Implement DynamoDB Stream with AWS Lambda

We can work with the DynamoDB on the AWS, and add a trigger to execute a Lambda function which can deal with DynamoDB stream events:

- Comment `AWS_ENDPOINT_URL` in `docker-compose.yml`, then compose up and run `./bin/db/setup`
- Update `./bin/ddb/schema-load` with a Global Secondary Index (GSI) and run `./bin/ddb/schema-load prod`, leading to a DynamoDB table named `cruddur-messages` created on our AWS
- On AWS in DynamoDB > Tables > cruddur-messages > Turn on DynamoDB stream, choose "new image"
- On AWS in the VPC console, create an endpoint named `cruddur-ddb`, choose services with DynamoDB, and select the default VPC and route table
- On AWS in the Lambda console, create a new function named `cruddur-messaging-stream` and enable VPC in its advanced settings; deploy the code as seen in `aws/lambdas/cruddur-messaging-stream.py`; add permission of `AWSLambdaInvocation-DynamoDB` to the Lambda IAM role; more permissions can be added by creating inline policies as seen in `aws/policies/cruddur-message-stream-policy.json`
- On AWS in the DynamoDB console, create a new trigger and select `cruddur-messaging-stream`

Now if we compose up, visit the frontend and sign in, it's empty under the messages tab, because there is no data in our AWS DynamoDB. To create a new message in a new message group with Bayko, visit `https://<frontend_address>/messages/new/bayko`, messages can be created and updated as seen in the screenshot below.

![Proof of seed dynamodb]()

If everything works, there is no error observed on AWS in CloudWatch > Log groups > /aws/lambda/cruddur-messaging-stream as shown in the screenshots below.

![Proof of seed dynamodb]()









