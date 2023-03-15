# Week 2 — Distributed Tracing

__Objetive__ 
* Distributed tracing implementation to add the functionality to easy pinpoint issue when adding cloud services.
        
__Week Summary__
* Instrument our backend flask application to use Open Telemetry (OTEL) with Honeycomb.io as the provider
* Run queries to explore traces within Honeycomb.io
* Instrument AWS X-Ray into backend flask application
* Configure and provision X-Ray daemon within docker-compose and send data back to X-Ray API
* Observe X-Ray traces within the AWS Console
* Integrate Rollbar for Error Logging
* Trigger an error an observe an error with Rollbar
* Install WatchTower and write a custom logger to send application log data to - CloudWatch Log group

__Notes__ 
* Week 2 was done with week 3 due to master exams.
        
AWS Services used:
* AWS X-Ray
* AWS CloudWatch

(click to open section)

<details><summary>Week content</summary>

<br/><br/> 

### What is observability?
>Observability is the extent to which the internal states of a system can be inferred from externally available data. An observable software system provides the ability to understand any issue that arises. Conventionally, __the three pillars of observability data are metrics, logs and traces.__

### What are traces?

>A trace represents the entire journey of a request or action as it moves through all the nodes of a distributed system.

### What are logs?

>A log file is a computer-generated data file that contains information about usage patterns, activities, and operations within an operating system, application, server or another device. Log files show whether resources are performing properly and optimally.\
>On-Premise logs: infraestructure , applications, anti-virus, Firewall..
>Cloud Logs: infraestructure** , applications**, anti-virus, Firewall..

### Observability vs Monotoring
        
Problem of logging
- Time-consuming
- Tons of data with no context for why of the security events
- Needles in a haystack to find things
- Increase alert fatigue for SOC team and application team

Why Observability?
- Decreased alert fatigue
- Visibility of end2end of logs, metrics and tracing
- troubleshoot and resolve things quickly
- Understand application health
- Accelerate team collaboration
- Reduce overall operational cost
- Increase customer satisfaction

![Observability vs Monotoring](assets/week2_obsvsmonit.jpeg)


### What is Observability in AWS?

>Open-source solutions, giving you the ability to understand what is happening across your technology stack at any time. AWS observability lets you collect, correlate, aggregate, and analyze telemetry in your network, infrastructure, and applications in the cloud, hybrid, or on-premises environments so you can gain insights into the behavior, performance, and health of your system. 
>These insights help you detect, investigate, and remediate problems faster; and coupled with artificial intelligence and machine learning, proactively react, predict, and prevent problems.
        
Obeservability services in AWS
- AWS Cloudwatch logs
- AWS Cloudwatch metrics
- AWS X Ray traces

***Instrumentation*** is what helps you to create or produce logs metrics traces.

![Observability AWS Tools](assets/week2_aws_observabilitytools.jpeg)

[AWS Observability](https://aws.amazon.com/cloudops/monitoring-and-observability/?whats-new-cards.sort-by=item.additionalFields.postDateTime&whats-new-cards.sort-order=desc&blog-posts-cards.sort-by=item.additionalFields.createdDate&blog-posts-cards.sort-order=desc)

### For what are we using Honeycomb? To visualice and read the data extracted.

>Is a software debugging tool that can help you solve problems faster within your distributed services. Honeycomb provides full stack observability—designed for high cardinality data and collaborative problem solving, enabling engineers to deeply understand and debug production software together.

[HoneyComb](https://www.honeycomb.io)

### How are we sending the traces, metrics and logs to HoneyComb? OpenTelemetry

> Honeycomb supports OpenTelemetry, the CNCF open standard for sending traces, metrics, and logs. If your application is already instrumented for OpenTelemetry, you can send OTLP data directly to Honeycomb’s endpoint.

[OpenTelemetry](https://docs.honeycomb.io/getting-data-in/opentelemetry-overview/)

What is middleware for web applications?
        
> Middleware is software that different applications use to communicate with each other. It provides functionality to connect applications intelligently and efficiently so that you can innovate faster. Middleware acts as a bridge between diverse technologies, tools, and databases so that you can integrate them seamlessly into a single system. The single system then provides a unified service to its users. For example, a Windows frontend application sends and receives data from a Linux backend server, but the application users are unaware of the difference.
 
        
What is a Daemon?

>A daemon is a process that runs in the background rather than under the direct control of the user. Although you run docker commands on your host machine, these commands do none of the processing on your Docker containers and images. They are frequently also servers that accept requests from clients to perform actions for them.

![Docker Daemons](assets/week2_daemons.png)

### What is AWS X-RAY?
>AWS X-Ray provides a complete view of requests as they travel through your application and filters visual data across payloads, functions, traces, services, APIs, and more with no-code and low-code motions.

[AWS X-RAY](https://aws.amazon.com/xray/?nc1=h_ls)

![AWS X-RAY](assets/week2_awsxray.png)

[Configuring the AWS X-Ray daemon](https://docs.aws.amazon.com/xray/latest/devguide/xray-daemon-configuration.html)

[What are the best practises for setting up x-ray daemon?](https://stackoverflow.com/questions/54236375/what-are-the-best-practises-for-setting-up-x-ray-daemon)

![Best practices](assets/week2_xraybestpractices.png)

[AWS X-RAY:SDK python](https://docs.aws.amazon.com/xray/latest/devguide/xray-sdk-python.html)

[AWS X-RAY:SDK python](https://github.com/aws/aws-xray-sdk-python)



</details>

--------------------------------------------------------------------------------------------------------------------------------

<details><summary>Implementation</summary>
<br></br>

[Implementation code](https://github.com/PericoLedesma/aws-bootcamp-cruddur-2023/blob/main/week_instructions/week2.md)


1. Instrument our backend flask application to use Open Telemetry (OTEL) with Honeycomb.io as the provider
   * Set up the endpoint in the honeycomb.ai API
   * Service name is the name of the span
   * Each endpoint as a service object. Each endpoint is modular and points to a service in the back in our application.
   * To create spans we need tracers that will send the data to the API
   * [To include tracers in other parts](https://devpress.csdn.net/python/62f4e4c27e66823466189204.html)
        
2. Run queries to explore traces within Honeycomb.io
   * Right panel we can search for our tracers
        
![Honeycomb.ai traces](assets/wek2_trace.png)
        
![Honeycomb.ai metrics](assets/week2_metrics.png)
        
![Honeycomb.ai traces](assets/wee2_metrics1.2.png)
        
![Honeycomb.ai traces](assets/week2_metric2.png)
              
3. Instrument AWS X-Ray into backend flask application
   * [We create groups of X-RAYS traces: to group traces together](https://eu-central-1.console.aws.amazon.com/cloudwatch/home?region=eu-central-1#xray:settings/groups)
   * [We create a sampling rule to control how much information we see.](https://eu-central-1.console.aws.amazon.com/cloudwatch/home?region=eu-central-1#xray:settings/sampling-rules)

4. Configure and provision X-Ray daemon within docker-compose and send data back to X-Ray API

   * We need a docker daemon to make it work. 
 
   * [X-RAY-SED-Python]([assets/week2_trace.png](https://docs.aws.amazon.com/xray/latest/devguide/xray-sdk-python.html))
         
   * [X-RAY-SED-Python Github Repository]([assets/week2_trace.png](https://github.com/aws/aws-xray-sdk-python))        
        
   * How to install daemon [Documentation](https://docs.aws.amazon.com/xray/latest/devguide/xray-daemon.html)
        
5. Observe X-Ray traces within the AWS Console
   * [X-RAY subsegments](https://olley.hashnode.dev/aws-free-cloud-bootcamp-instrumenting-aws-x-ray-subsegments)

6. Integrate Rollbar for Error Logging
   * [Reports](https://rollbar.com/rgzledesma/all/items/?sort=%5Bobject%20Object%5D&status=active&date_from=&date_to=&environments=production&activated_to=&framework=&levels=10&levels=20&levels=30&levels=40&levels=50&activated_from=&offset=0&timezone=Europe%2FBerlin&assigned_user=&date_filtering=seen&projects=624482&query=&enc_query=)
        
7. Trigger an error an observe an error with Rollbar
        
8. Install WatchTower and write a custom logger to send application log data to CloudWatch Log group
   * Watchtower: library in python to habdle cloudwatch logs. [Documentation](https://pypi.org/project/watchtower/)
   * Carefull cloudwatch cost money. Same xray. Not much. We disable it.

Troubles during implementation.     
>I had issures becuase the was a step that I miss or was not explained and I lost some days strying to fix it. We have to go to the frontend repository and install npm. Because I did not run this step i was stak for a while. I thought the npm was installed with the docker file


</details>

--------------------------------------------------------------------------------------------------------------------------------

<details><summary>Challenges</summary>

- [ ] Adding Attributes to Spans 
- [ ] Instrument Honeycomb for the frontend-application to observe network latency between frontend and backend[HARD]
- [ ] Add custom instrumentation to Honeycomb to add more attributes eg. UserId, Add a custom span What would we usefull for us
- [ ] Run custom queries in Honeycomb and save them later eg. Latency by UserID, Recent Traces
- [ ] Add aditional information rollbar
       


</details>

--------------------------------------------------------------------------------------------------------------------------------


<details><summary>Pricing aspects</summary>

<br/><br/> 
        
* 100 million monthly events are included in the Honeycomb free tier       
* The Rollbar free tier includes up to 5,000 events per month, which can include error events, logged errors, and custom events.
* On the AWS X-Ray free tier, you can trace up to 100,000 requests per month at no charge.
* Cloudwatch (always free tier):
        - 10 custom metrics and alarm
        - 1.000.000 API request
        - 5GB of log dataingestion and 5 GB of log Data Archive
        - 3 Dashboards with up to 50 Metrics each per month
  
        
        
</details>

--------------------------------------------------------------------------------------------------------------------------------

<details><summary>Implementation instructions</summary>
<br></br>
  

## X-Ray

### Instrument AWS X-Ray for Flask


```sh
export AWS_REGION="ca-central-1"
gp env AWS_REGION="ca-central-1"
```

Add to the `requirements.txt`

```py
aws-xray-sdk
```

Install pythonpendencies

```sh
pip install -r requirements.txt
```

Add to `app.py`

```py
from aws_xray_sdk.core import xray_recorder
from aws_xray_sdk.ext.flask.middleware import XRayMiddleware

xray_url = os.getenv("AWS_XRAY_URL")
xray_recorder.configure(service='Cruddur', dynamic_naming=xray_url)
XRayMiddleware(app, xray_recorder)
```

### Setup AWS X-Ray Resources

Add `aws/json/xray.json`

```json
{
  "SamplingRule": {
      "RuleName": "Cruddur",
      "ResourceARN": "*",
      "Priority": 9000,
      "FixedRate": 0.1,
      "ReservoirSize": 5,
      "ServiceName": "Cruddur",
      "ServiceType": "*",
      "Host": "*",
      "HTTPMethod": "*",
      "URLPath": "*",
      "Version": 1
  }
}
```

```sh
FLASK_ADDRESS="https://4567-${GITPOD_WORKSPACE_ID}.${GITPOD_WORKSPACE_CLUSTER_HOST}"
aws xray create-group \
   --group-name "Cruddur" \
   --filter-expression "service(\"bacnkend-flask\")"
```


Creating sampling rule:
```sh
aws xray create-sampling-rule --cli-input-json file://aws/json/xray.json
```

 [Install X-ray Daemon](https://docs.aws.amazon.com/xray/latest/devguide/xray-daemon.html)

[Github aws-xray-daemon](https://github.com/aws/aws-xray-daemon)
[X-Ray Docker Compose example](https://github.com/marjamis/xray/blob/master/docker-compose.yml)



```sh
 wget https://s3.us-east-2.amazonaws.com/aws-xray-assets.us-east-2/xray-daemon/aws-xray-daemon-3.x.deb
 sudo dpkg -i **.deb
 ```

### Add Deamon Service to Docker Compose

```yml
  xray-daemon:
    image: "amazon/aws-xray-daemon"
    environment:
      AWS_ACCESS_KEY_ID: "${AWS_ACCESS_KEY_ID}"
      AWS_SECRET_ACCESS_KEY: "${AWS_SECRET_ACCESS_KEY}"
      AWS_REGION: "us-east-1"
    command:
      - "xray -o -b xray-daemon:2000"
    ports:
      - 2000:2000/udp
```

We need to add these two env vars to our backend-flask in our `docker-compose.yml` file

```yml
      AWS_XRAY_URL: "*4567-${GITPOD_WORKSPACE_ID}.${GITPOD_WORKSPACE_CLUSTER_HOST}*"
      AWS_XRAY_DAEMON_ADDRESS: "xray-daemon:2000"
```

### Check service data for last 10 minutes

```sh
EPOCH=$(date +%s)
aws xray get-service-graph --start-time $(($EPOCH-600)) --end-time $EPOCH
```

## HoneyComb

When creating a new dataset in Honeycomb it will provide all these installation insturctions



We'll add the following files to our `requirements.txt`

```
opentelemetry-api 
opentelemetry-sdk 
opentelemetry-exporter-otlp-proto-http 
opentelemetry-instrumentation-flask 
opentelemetry-instrumentation-requests
```

We'll install these dependencies:

```sh
pip install -r requirements.txt
```

Add to the `app.py`

```py
from opentelemetry import trace
from opentelemetry.instrumentation.flask import FlaskInstrumentor
from opentelemetry.instrumentation.requests import RequestsInstrumentor
from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
```


```py
# Initialize tracing and an exporter that can send data to Honeycomb
provider = TracerProvider()
processor = BatchSpanProcessor(OTLPSpanExporter())
provider.add_span_processor(processor)
trace.set_tracer_provider(provider)
tracer = trace.get_tracer(__name__)
```

```py
# Initialize automatic instrumentation with Flask
app = Flask(__name__)
FlaskInstrumentor().instrument_app(app)
RequestsInstrumentor().instrument()
```

Add teh following Env Vars to `backend-flask` in docker compose

```yml
OTEL_EXPORTER_OTLP_ENDPOINT: "https://api.honeycomb.io"
OTEL_EXPORTER_OTLP_HEADERS: "x-honeycomb-team=${HONEYCOMB_API_KEY}"
OTEL_SERVICE_NAME: "${HONEYCOMB_SERVICE_NAME}"
```

You'll need to grab the API key from your honeycomb account:

```sh
export HONEYCOMB_API_KEY=""
export HONEYCOMB_SERVICE_NAME="Cruddur"
gp env HONEYCOMB_API_KEY=""
gp env HONEYCOMB_SERVICE_NAME="Cruddur"
```

## CloudWatch Logs


Add to the `requirements.txt`

```
watchtower
```

```sh
pip install -r requirements.txt
```


In `app.py`

```
import watchtower
import logging
from time import strftime
```

```py
# Configuring Logger to Use CloudWatch
LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.DEBUG)
console_handler = logging.StreamHandler()
cw_handler = watchtower.CloudWatchLogHandler(log_group='cruddur')
LOGGER.addHandler(console_handler)
LOGGER.addHandler(cw_handler)
LOGGER.info("some message")
```

```py
@app.after_request
def after_request(response):
    timestamp = strftime('[%Y-%b-%d %H:%M]')
    LOGGER.error('%s %s %s %s %s %s', timestamp, request.remote_addr, request.method, request.scheme, request.full_path, response.status)
    return response
```

We'll log something in an API endpoint
```py
LOGGER.info('Hello Cloudwatch! from  /api/activities/home')
```

Set the env var in your backend-flask for `docker-compose.yml`

```yml
      AWS_DEFAULT_REGION: "${AWS_DEFAULT_REGION}"
      AWS_ACCESS_KEY_ID: "${AWS_ACCESS_KEY_ID}"
      AWS_SECRET_ACCESS_KEY: "${AWS_SECRET_ACCESS_KEY}"
```

> passing AWS_REGION doesn't seems to get picked up by boto3 so pass default region instead


## Rollbar

https://rollbar.com/

Create a new project in Rollbar called `Cruddur`

Add to `requirements.txt`


```
blinker
rollbar
```

Install deps

```sh
pip install -r requirements.txt
```

We need to set our access token

```sh
export ROLLBAR_ACCESS_TOKEN=""
gp env ROLLBAR_ACCESS_TOKEN=""
```

Add to backend-flask for `docker-compose.yml`

```yml
ROLLBAR_ACCESS_TOKEN: "${ROLLBAR_ACCESS_TOKEN}"
```

Import for Rollbar

```py
import rollbar
import rollbar.contrib.flask
from flask import got_request_exception
```

```py
rollbar_access_token = os.getenv('ROLLBAR_ACCESS_TOKEN')
@app.before_first_request
def init_rollbar():
    """init rollbar module"""
    rollbar.init(
        # access token
        rollbar_access_token,
        # environment name
        'production',
        # server root directory, makes tracebacks prettier
        root=os.path.dirname(os.path.realpath(__file__)),
        # flask already sets up logging
        allow_logging_basic_config=False)

    # send exceptions from `app` to rollbar, using flask's signal system.
    got_request_exception.connect(rollbar.contrib.flask.report_exception, app)
```

We'll add an endpoint just for testing rollbar to `app.py`

```py
@app.route('/rollbar/test')
def rollbar_test():
    rollbar.report_message('Hello World!', 'warning')
    return "Hello World!"
```


[Rollbar Flask Example](https://github.com/rollbar/rollbar-flask-example/blob/master/hello.py)

  
  
  
</details>
  
  --------------------------------------------------------------------------------------------------------------------------------
