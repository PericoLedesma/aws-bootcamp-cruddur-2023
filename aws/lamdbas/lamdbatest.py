# To test the lamdda in my computer

 
import json
import psycopg2
import os

print("Running lambda_handler")

user_display_name = 'name'
user_email = 'email'
user_handle = 'preferred_username'
user_cognito_id = 'sub'

try:  
    print('entered-try')                              
    sql = f"""
        INSERT INTO users(
        display_name,
        handle, 
        email, 
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

    conn = psycopg2.connect(os.getenv('PROD_CONNECTION_URL'))
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

