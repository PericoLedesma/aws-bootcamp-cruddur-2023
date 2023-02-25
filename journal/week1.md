# Week 1 — App Containerization

Structure:
1. Class contect
2. Practice/Homework

## 1. Class content

### Security on Container

Container security is the practice of protecting your applications hosted on compute services like containers. 

Why use containers?

> It is a angnostic way to run application. Most people started developing apps on container due to the simplicity to pass the package without considering requirements.

Managed vs unmanaged containers

> - Managed Containers means that the Provider like AWS managed the underlying service for the container (ECS or EKS). In this case Cloud provider will be managing the security prospective .

> - Unmanaged Containers means you are running your container on your servers and you have to manage all the system (for example you will be in charged to apply security patches).


Why containers security requires practice?

> Complexity with containers
> Relying on CSPs for features
> UnManaged requires a lot more hours of work than managed but would require you keeping updated on everthing

Containers security components
> Docker and host configurations
> Securing images
> Secret management
> Application security
> Data Security
> Monitoring Containers
> Compliance Framework

Security best practices
> - Keep Host & Docker Updated to latest security patches.
> - Docker Deamon & containers should run in non root user mode
> - Image Vulnerability Scanning
> - Trust a Private vs Public Image Registry
> - No Sensitive Data in Docker Files or Images
> - Use Secret Management Services to share secrets.
> - Read only file system and volume for dockers
> - Separate databases for long term storage
> - Use DevSecOps pratices while building application security
> - Ensure all code is tested for vulnerabilities before production use

Tools to identify vulnerailitues on your containers are:
> - Snyk OpenSource Security. 
> - AWS Inspector

Tools to store and manage secrets are:
> - AWS Secret Manager 
> - Harshicorp Vault

For Managed Containers in AWS:
> - AWS ECS
> - AWS EKS
> - AWS Fargate
 
Docker compose
> It is a tool for defining and running multi container Docker Applications (It uses yml file).

### Dockers components

![Docker components](assets/week1_architecture.svg)


## 2. Practice/Homework

### Coding the startpoint for the notifications endpoint API

Curretly, the notifications endpoint API was not created.

First, we created the endpoint in the OpenAPI file first with the same structure as homeAPI

![Current point of the notifications page](assets/week1_openapi_notifications.png)

We linked with the NotificationActivities class that we created to the openAPI route.

We can see after we linked to the class the route the hardcore results are given by the API.

![Current point of the notifications page](assets/week1_notapi_results.png)


### Coding the startpoint for the notifications frontend Page

Currently, the Notifications page was not created.

![Current point of the notifications page](assets/week1_noti_page.jpg)

We created the page in app.js and create the NotificationsFeedPage.js with same structure as home page

![Current point of the notifications page](assets/week1_notpage.png)

