from datetime import datetime, timedelta, timezone
from opentelemetry import trace

from lib.db import db

import logging #Cloudwatch logs

# OpenTelemetry ------
tracer = trace.get_tracer("home.activities")

class HomeActivities:
  def run(cognito_user_id): # arg Logger
    print('==== Running HomeActivities.run')
    #Logger.info("HomeActivities") #Cloudwatch logs. Carefull cost money
    # OpenTelemetry tracer setup
    #with tracer.start_as_current_span("home-activities-mock-data"): # Span caller
    #  span = trace.get_current_span() # Span attributes 
    #  now = datetime.now(timezone.utc).astimezone()
    #  span.set_attribute("app.now", now.isoformat())
    
    sql = db.template('activities','home')


    
    results = db.query_array_json(sql)
    print('==== End HomeActivities.run')
    return results
