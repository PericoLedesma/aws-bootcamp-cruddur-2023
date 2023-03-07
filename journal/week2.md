# Week 2 — Distributed Tracing

What are traces?
Instrumentation

What are we using Honeycomb? To visualice the traces

How are we sending them? Usin opentelemetry

Link what is opentelemetry 



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
