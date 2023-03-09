# Week 2 — Distributed Tracing

Note: week 2 was done with week 3 due to master examns.

(click to open section)

<details><summary>Week content</summary>
<p>
Objetive: Distributed tracing implementation to add the functionality to easy pinpoint issue when adding cloud services.

        </p>
</details>



        
        
        
<details><summary>Practice</summary>
<p>
   
</p>
</details>

What is obnservability?
>Observability is the extent to which the internal states of a system can be inferred from externally available data. An observable software system provides the ability to understand any issue that arises. Conventionally, __the three pillars of observability data are metrics, logs and traces.__

What are traces?

>A trace represents the entire journey of a request or action as it moves through all the nodes of a distributed system.

What are logs?

>A log file is a computer-generated data file that contains information about usage patterns, activities, and operations within an operating system, application, server or another device. Log files show whether resources are performing properly and optimally.\
>On-Premise logs: infraestructure , applications, anti-virus, Firewall..
>Cloud Logs: infraestructure** , applications**, anti-virus, Firewall..

Observability vs Monotoring
Image 

What is Observability in AWS?

>Open-source solutions, giving you the ability to understand what is happening across your technology stack at any time. AWS observability lets you collect, correlate, aggregate, and analyze telemetry in your network, infrastructure, and applications in the cloud, hybrid, or on-premises environments so you can gain insights into the behavior, performance, and health of your system. 
>These insights help you detect, investigate, and remediate problems faster; and coupled with artificial intelligence and machine learning, proactively react, predict, and prevent problems.

[AWS Observability](https://aws.amazon.com/cloudops/monitoring-and-observability/?whats-new-cards.sort-by=item.additionalFields.postDateTime&whats-new-cards.sort-order=desc&blog-posts-cards.sort-by=item.additionalFields.createdDate&blog-posts-cards.sort-order=desc)

Image aws tools

For what are we using Honeycomb? To visualice and read the data extracted.

>Is a software debugging tool that can help you solve problems faster within your distributed services. Honeycomb provides full stack observability—designed for high cardinality data and collaborative problem solving, enabling engineers to deeply understand and debug production software together.

[HoneyComb](https://www.honeycomb.io)

How are we sending the traces, metrics and logs to HoneyComb? OpenTelemetry

> Honeycomb supports OpenTelemetry, the CNCF open standard for sending traces, metrics, and logs. If your application is already instrumented for OpenTelemetry, you can send OTLP data directly to Honeycomb’s endpoint.

[OpenTelemetry](https://docs.honeycomb.io/getting-data-in/opentelemetry-overview/)


Task: Seting up opentelemetry
Seting up the endpoint in Honeycomb with the api key
Service name: how the data is span

I had in second a trouble problem becuase the was a step that I miss or was not explained and I lost some days strying to fix it. We have to go to the frontend repository and install npm. Because I did not run this step i was stak for a while. I thought the npm was installed with the docker file


Endpoints, each points ahs a service object. Each endpoints is modular and points to a services in the back.

To include tracers in other parts

[https://devpress.csdn.net/python/62f4e4c27e66823466189204.html](https://docs.honeycomb.io/getting-data-in/opentelemetry/python/) Acquiring a Tracer 

To create spans, you need to get a Tracer. We just impor the api

from opentelemetry import trace
tracer = trace.get_tracer("tracer.name.here")

# This is to creating the spans

with tracer.start_as_current_span("mock-data"): # This is the name of the span
        # do something


in HONEYCOMB, library says what did that spans

We have automaticatly some fields on the right part
Some are globnal
We can add some fields for our owns. Next step. Spans because replacement for logs

So next step Adding Attributes to Spans 

Challenge:Instrument the frontend. Is dificult. 
Had our instrumentation. What would we usefull for us
Run custum queries.



# XRAY

we need a daemon to make it work. Another container it seems

Image of best practices

task what is npm? and sdk?

link sdk and aws

https://docs.aws.amazon.com/xray/latest/devguide/xray-sdk-python.html

https://github.com/aws/aws-xray-sdk-python

We add to requirement aws-xray-sdk 

What is middleware for web applications?


We can used middleware layers to handdle steps before the request arrieve to the application, like a security layer. 
We are going to use it for tracing


Task: what is flask



Groups of XRAYS traces: to group traces together


https://eu-central-1.console.aws.amazon.com/cloudwatch/home?region=eu-central-1#xray:settings/groups

Next task to create a sampling rule: how much information you want to see. 


https://eu-central-1.console.aws.amazon.com/cloudwatch/home?region=eu-central-1#xray:settings/sampling-rules

Now we have to isntall xray daemon

Documentation https://docs.aws.amazon.com/xray/latest/devguide/xray-daemon.html

We are going to put xray tracer in 


Next video: cloudwatch logs 

watchtower library in python to handle cloudwatch logs 

https://pypi.org/project/watchtower/

Task: check all the options in cloudwatch what are

Carefull cloudwatch cost money. Same xray. Not much. We disable it.

End video


Video rollbar

waht is a rollbar. https://rollbar.com

Challenge: add aditional information rollbar

why we need rollwbar? in production we dont see the error

Here we can see https://rollbar.com/rgzledesma/all/items/?sort=%5Bobject%20Object%5D&status=active&date_from=&date_to=&environments=production&activated_to=&framework=&levels=10&levels=20&levels=30&levels=40&levels=50&activated_from=&offset=0&timezone=Europe%2FBerlin&assigned_user=&date_filtering=seen&projects=624482&query=&enc_query=



XRAY subsegments

https://olley.hashnode.dev/aws-free-cloud-bootcamp-instrumenting-aws-x-ray-subsegments

