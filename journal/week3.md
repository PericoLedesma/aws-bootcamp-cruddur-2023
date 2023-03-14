# Week 3 — Decentralized Authentication


__Objetive__ 
* Practical knowledge of implementing a decentralized authentication service into a web-application with custom login and signup pages in a react application.

        
__Week Summary__
* Provision via ClickOps a Amazon Cognito User Pool
* Install and configure Amplify client-side library for Amazon Cognito
* Implement API calls to Amazon Cognito for custom login, signup, recovery and forgot password page
* Show conditional elements and data based on logged in or logged out
* Verify JWT Token server side to serve authenticated API endpoints in Flask Application

__Notes__ 
* Need a basic jc tutorial
        
AWS Services used:
* AWS cognito
* AWS Amplify


(click to open section)

--------------------------------------------------------------------------------------------------------------------------------

<details><summary>Week content</summary>
\
What is AWS Cognito? 

> With Amazon Cognito, you can add user sign-up and sign-in features and control access to your web and mobile applications. Amazon Cognito provides an identity store that scales to millions of users, supports social and enterprise identity federation, and offers advanced security features to protect your consumers and business.
[AWS Cognito](https://aws.amazon.com/cognito/)

What is AWS Amplify and why to use it?

> AWS Amplify is an end-to-end solution that enables mobile and front-end web developers to build and deploy secure, scalable full stack applications, powered by AWS.
> Amplify uses Amazon Cognito as the main authentication provider. We use AWS Amplify library to use AWS Cognito. Frontend-javascript library. 

[AWS amplify](https://aws.amazon.com/amplify/?trk=d3adb855-b91b-4e74-8308-5e9f08e34ed2&sc_channel=ps&s_kwcid=AL!4422!3!647302000960!e!!g!!amplify%20aws&ef_id=EAIaIQobChMIiLeZuMLR_QIV0dDVCh0m3QCMEAAYASAAEgLMYvD_BwE:G:s&s_kwcid=AL!4422!3!647302000960!e!!g!!amplify%20aws)

[AWS Amplify Documentation](https://docs.amplify.aws/)

What is a JSON Web Tokens?

> JSON Web Token (JWT) is an open standard that defines a compact and self-contained way for securely transmitting information between parties as a JSON object. This information can be verified and trusted because it is digitally signed. JWTs can be signed using a secret (with the HMAC algorithm) or a public/private key pair using RSA or ECDSA.\

[Introduction to JSON Web Tokens](https://jwt.io/introduction)

What is a sidecar container?

> Sidecar containers are containers that are needed to run alongside the main container. The two containers share resources like pod storage and network interfaces. The sidecar containers can also share storage volumes with the main containers, allowing the main containers to access the data in the sidecars.
[ What is a sidecar container?](https://www.containiq.com/post/kubernetes-sidecar-container#:~:text=Sidecar%20containers%20are%20containers%20that,the%20data%20in%20the%20sidecars.)

Which additional AWS service should be enabled and monitored alongside Cognito to help detect malicious Cognito user behavior?

> AWS CloudTrail: This service provides a record of AWS API calls made by a user or a resource in your account. By enabling CloudTrail, you can track who is accessing your Cognito user pools and identify any unauthorized access attempts or suspicious behavior.

When it comes to single-sign-on, what does the acronym SAML stand for?

> SAML stands for Security Assertion Markup Language. It is an XML-based standard used for exchanging authentication and authorization data between parties, in particular, between an identity provider (IdP) and a service provider (SP). SAML enables single sign-on (SSO) and provides a way to authenticate users across multiple applications or domains without requiring them to enter their credentials separately for each one.

Your Cognito deployment should only be in the AWS region which you are legally allowed to hold user data in

</details>

--------------------------------------------------------------------------------------------------------------------------------

<details><summary>Implementation</summary>
        
        1. Provision Amazon Cognito User Pool using AWS UI (Console) -> easier
           * Just follow instructions. Really clear. Options of recover password and register. 
           * We have to change the status of the user with the AWS console.
        
        2. Install and Configure Amplify Client-Side Library for Amazon Congito.
        
        3. Show Some Components if You Are Logged in Only
           * Implemented some components in these pages HomeFeedPage.js, DesktopNavigation.js, ProfileInfo.js, DesktopSidebar.js.
           * We reuse the code of the next [library](https://github.com/cgauge/Flask-AWSCognito/blob/master/flask_awscognito/services/token_service.py)
        
        4. Implement API Calls to Amazon Coginto for Custom Login, Signup, Recovery and Forgot Password Page   
        
        5. Authenticating Server Side     

        6. Frontend. Stablish general variables for the frontend and changed some color to have more constrast
</details>

--------------------------------------------------------------------------------------------------------------------------------

<details><summary>Challenges</summary>
        
- [x] Made sure Resend Activation Code works in the Confirmation Page after sign up. 
</details>
  
  
 
  

