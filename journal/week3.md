# Week 3 — Decentralized Authentication


__Objetive:__ Practical knowledge of implementing a decentralized authentication service into a web-application with custom login and signup pages in a react application.
        Note: Need a basic jc tutorial

AWS Services used:
* AWS cognito

* [AWS amplify](https://aws.amazon.com/amplify/?trk=d3adb855-b91b-4e74-8308-5e9f08e34ed2&sc_channel=ps&s_kwcid=AL!4422!3!647302000960!e!!g!!amplify%20aws&ef_id=EAIaIQobChMIiLeZuMLR_QIV0dDVCh0m3QCMEAAYASAAEgLMYvD_BwE:G:s&s_kwcid=AL!4422!3!647302000960!e!!g!!amplify%20aws)

(click to open section)

<details><summary>Week content</summary>
  
We are using AWS Cognito via CLI.
        AMAZON congnito - user pool -create pool. Just follow instructions. Really clear. Options of recover password and register. 
We have to use AWS amplify library to use aws cognito. Frontend-javascript library 
        We dont need to use it to config cognito, we did it by CLI that is easier.

[AWS Amplify Documentation](https://docs.amplify.aws/)
        
Others: dependencies are libraries that are required to make the application to work
        
</details>

--------------------------------------------------------------------------------------------------------------------------------

<details><summary>Implementation</summary>
        
        
        First step to install aws amplify
        
        
        Note: react app env varibles need to start with REACT_APP
        
        We have to change the status of the user with the aws terminal console 
        
        Users can be created in cognito directly 
        ----
        Backend implementation cognito
        We have to protect our api point, we are passing out token 
        For validating the token
        https://github.com/cgauge/Flask-AWSCognito/blob/master/flask_awscognito/services/token_service.py
        
        We have the authentification client side
        
        We are going to use the library=-- we truy but we reach limitation
        
        
</details>

--------------------------------------------------------------------------------------------------------------------------------

<details><summary>Challenges</summary>
</details>
  
  
  --------------------------------------------------------------------------------------------------------------------------------

<details><summary>Implementation</summary>
</details>
  
