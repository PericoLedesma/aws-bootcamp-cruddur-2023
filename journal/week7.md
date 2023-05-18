# Week 7 — Solving CORS with a Load Balancer and Custom Domain

### Content

1. [Objetives](#Objetives)
2. [Week summary](#Week-summary)

Week 7 was delivered together with Week 6. Check my [week6 journal](https://github.com/PericoLedesma/aws-bootcamp-cruddur-2023/blob/main/journal/week6.md)

----------------------------------------------------------------

### Objetives

- Working with DNS records and hosted zones
- Configuring TLS termination at the load balancer
- Deploying and configuring a load balancer for multiple subdomains
- Basic understanding of solving CORS issues and backend-to-frontend communication


### Week Summary

- Create a Route53 hosted zone to manage our domain
- Generate a public certificate via AWS Certificate Manager (ACM)
- Create an Application Load Balancer (ALB)
- Create ALB target group that points to our Fargate instances
- Update our application to handle CORS
