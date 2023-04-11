from datetime import datetime, timedelta, timezone

from lib.ddb import Ddb
from lib.db import db


class MessageGroups:
  def run(cognito_user_id):
    print("Running MessageGroup", flush=True)
    
    model = {
      'errors': None,
      'data': None
    }


    # Buscamos la plantilla sql para buscar nuestro usuario
    sql = db.template('users','uuid_from_cognito_user_id')
    my_user_uuid = db.query_value(sql,{
      'cognito_user_id': cognito_user_id
    })

    print(f"We have the UUID to search conversations: {my_user_uuid}", flush=True)

    ddb = Ddb.client()
    data = Ddb.list_message_groups(ddb, my_user_uuid)
    print("list_message_groups:",data, flush=True)

    model['data'] = data
    return model