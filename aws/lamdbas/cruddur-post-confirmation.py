import json
import psycopg2
import os

def lambda_handler(event, context):
    print("Running lambda_handler")
    user = event['request']['userAttributes']
    print('*userAttributes*')
    print(user)
    
    user_display_name = user['name']
    user_email = user['email']
    user_handle = user['preferred_username']
    user_cognito_id = user['sub']

    try:                                
        sql = f"""
            INSERT INTO users(
            display_name,
            email, 
            handle, 
            cognito_user_id
            ) 
             VALUES(%s,%s,%s,%s)
        """ 
        params = [
            user_display_name,
            user_email,
            user_handle,
            user_cognito_id
        ]
        
        print('SQL Statement ----')
        print(sql)

        conn = psycopg2.connect(os.getenv('CONNECTION_URL'))

        print("---1---")
        cur = conn.cursor()
        print("---2---")
        cur.execute(sql,params)     
        print("---3---")
        conn.commit() 
        print("---4--")

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        
    finally:
        if conn is not None:
            cur.close()
            conn.close()
            print('Database connection closed.')

    return event
