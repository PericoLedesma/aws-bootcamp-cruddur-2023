# Week 4 — Postgres and RDS

### Content

1. [Objetives](#Objetives)
2. [Week summary](#Week-summary)
3. [AWS Services used](#AWS-Services-used)
4. [Week content](#1-Week-content)
5. [Implementation notes(homework)](#2-Implementation-notes)
6. [Challenges](#3-Challenges)
7. [Implementation instructions](https://github.com/PericoLedesma/aws-bootcamp-cruddur-2023/blob/main/journal/week_instructions/week4.md)


### Objetives
   * Be able to data model using 3rd normal forms
   * Practical working knowledge of utilizing a Postgres database
   * Basic knowledge of working with an Online Analytical Processing (OLAP)


### Week Summary

   * Provision an RDS instance
   * Temporarily stop an RDS instance
   * Remotely connect to RDS instance
   * Programmatically update a security group rule
   * Write several bash scripts for database operations
   * Operate common SQL commands
   * Create a schema SQL file by hand
   * Work with UUIDs and PSQL extensions
   * Implement a postgres client for python using a connection pool
   * Troubleshoot common SQL errors
   * Implement a Lambda that runs in a VPC and commits code to RDS
   * Work with PSQL json functions to directly return json from the database
   * Correctly sanitize parameters passed to SQL to execute
        
### AWS Services used
   * [RDS](https://eu-central-1.console.aws.amazon.com/rds/home?region=eu-central-1#)



# 1 Week content
[Back index](#index)

   ### What is a AWS RDS instance?
  
   - Amazon Relational Database Service (Amazon RDS) is a collection of managed services that makes it simple to set up, operate, and scale databases in the cloud. 
   - Choose from seven popular engines — Amazon Aurora with MySQL compatibility, Amazon Aurora with PostgreSQL compatibility, MySQL, MariaDB, PostgreSQL, Oracle, and SQL Server — and deploy on-premises with Amazon RDS on AWS Outposts.
   
  [AWS RDS](https://aws.amazon.com/rds/)
  
  DynamoDB is not available as an option on the AWS RDS service. While DynamoDB is a database service provided by AWS, it is not a relational database like the others listed (Postgres, MySQL, and Aurora) that are available on RDS. DynamoDB is a NoSQL database and is available on AWS as a separate service called Amazon DynamoDB.
  

# 2 Implementation notes
[Back index](#index)
  
  ### RDS postgres implementation
  
   * RDS is much easy to use with the CLI command
   * However, to check the option check UI
   * We are using public access. We will have a security layer with the groups
   * VPC security we use the default
   * Typical port 5432. Best practice to change it so it is not easy to know what is there.
   * Important: instance can get stop, started and terminated. We stop it to recude cost. In 7 days turns on
     
   [RDS CLI](https://docs.aws.amazon.com/cli/latest/reference/rds/)
   
   [Amazon RDS User monitoring](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Monitoring.OS.html)
   
   [Amazon RDS User monitoring](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Monitoring.OS.Enabling.html)
   
  ### Postgres local
  
  We create a cruddur DB locally meanwhile. We setup tables and schemas,
   * Schema -> ./backend/db/schema.sql
   * The struture is the same as the APIs that we already have

 Postgress comes with some extensions and we have to check that they are available and are compatible with AWS
 
 To start postgres locally:
 ```
  psql cruddur < db/schema.sql -h localhost -U postgres
 ```
 or 
 ``` 
   psql -Upostgres --host localhost
  ```
  
 This is really teadious to have to introduce password everytime. We are going to automate the process with bash files(backend/bin). 
 
 We can connect directly using a CONNECTION_URL, where we include user, password, localtion, url and database name. Thefore, a way to provide all the detail to authenticate to the server.
 
 Format:  "postgresql://[user[:password]@][netloc][:port][/dbname][?param1=value1&...]"

 [Connection URL format](https://stackoverflow.com/questions/3582552/what-is-the-format-for-the-postgresql-connection-string-url)
  
  
 We store it locally:
 
  ```
  export CONNECTION_URL="postgresql://postgres:password@localhost:5432/cruddur"
  gp env CONNECTION_URL="postgresql://postgres:password@localhost:5432/ "
  ```

  Thefore, we can use it to connect directly to the local DB:
  
  ```
  psql $CONNECTION_URL
  ```

  We create some bash file to automate all the process we need to start and stop postgres.
  
  ![Bash files](assets/week4/week4_bashfile.png)
  
  __Extra bash__ file create to display the data of the DBs in prod and locally.
  
  One of the task is the upload of the __schema:__ A database schema defines how data is organized within a relational database; this is inclusive of logical constraints such as, table names, fields, data types, and the relationships between these entities.
  
  [Postgres defining schema](https://www.postgresqltutorial.com/postgresql-administration/postgresql-schema/)
  
  We can see the tables we created.
  
  ![Tables display](assets/week4/week4_tables.png)
  
  Note: 
    * to select a table and see ```SELECT * FROM tablename;```
    *  use ```\x on``` command to expand records and ```\x auto``` to autochange
 
  Alternative to connect to the database in gitpod:
  
  ![Tables display](assets/week4/week4_alternative.png)
  
  ![Tables display](assets/week4/week4_Struc.png)
 
  We seed it with data with the seed file:
  
  ![Seed File](assets/week4/week4_seed.png)
  
  We can see the data with the display data. The user Pedro was create with cognito(lamdba function, next section)
  
  ![RDS database](assets/week4/week4_displaydata.png)
    
  ### RDS with Postgres
  
  For production(AWS) we created other connection URL:
  
  ```
  export PROD_CONNECTION_URL=**
  gp env PROD_CONNECTION_URL=**
   ```
  
  We can use it by adding prod:
  
  ```
  psql $CONNECTION_URL prod
  ```

  ### Psycopg
  
  Psycopg is the most popular PostgreSQL adapter for the Python programming language.
  
  Psycopg_pool is a Python library that provides a connection pooling mechanism for psycopg.

  [Documentation](https://www.psycopg.org/)
  
  [Pooling connections](https://www.psycopg.org/psycopg3/docs/api/cursors.html)
  
  
  [Postgres json transformation functions](https://www.postgresql.org/docs/9.5/functions-json.html)

 
 RDS UI we create a inbound rule for the connexion of gitpod -> Connect to RDS via Gitpod --> VPC Security groups
     * The inbound IP has to be stored
 
 To see our current Gitpod ID curl ifconfig.me
     * We store it as env varible
 ```GITPOD_IP=$(curl ifconfig.me)```
     * We will have to update the IP on the security group everytime we launch the env.
     [Security group modify](https://docs.aws.amazon.com/cli/latest/reference/ec2/modify-security-group-rules.html)
 
  Other variables needed for the connection:

  ```
  export DB_SG_ID="sg-**"
  gp env DB_SG_ID="sg-**"

  export DB_SG_RULE_ID="sgr-**"
  gp env DB_SG_RULE_ID="sgr-**"
  
  ```
  And commendas for the CLI of AWS to update security rules:
  
  ```
   aws ec2 modify-security-group-rules \
    --group-id $DB_SG_ID \
    --security-group-rules "SecurityGroupRuleId=$DB_SG_RULE_ID,SecurityGroupRule={Description=GIDPOD,IpProtocol=tcp,FromPort=5432,ToPort=5432,CidrIpv4=$GITPOD_IP/32}"
    
   ```
    
   We update process witht the bash file rds-update-sg-rule

  ### Create AWS Cognito trigger to insert user into database
  
  We create a lambda that gets trigger every time a user confirm the email. The lamdba function connects to the RDS database and stores the users data. 
  I had a issue while connecting. Had to change the inbound rules of the RDS db to accept the lamdba function API. I will have to change the inbound at some point.
  
  The postgres connection url was stored as a env variable.
  
  ![Lambda function](assets/week4/week4_lambda2.png)
  
  ![Lambda function](assets/week4/week4_lambda.png)
  
  ### Create new activities with a database insert
  
  We modified the services create_activity and home_activities to store the created activity in the home page in the database
  

# 3 Challenges
[Back index](#index)

A new bash file and sql file was created to automate the process of displaying the data of the databases.

