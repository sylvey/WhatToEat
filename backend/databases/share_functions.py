import mysql.connector
import os
from dotenv import load_dotenv




def connect():
    load_dotenv()
    db_config = {
        'host': os.getenv('MYSQL_HOST'),
        'port': int(os.getenv('MYSQL_PORT')),  # 轉成 int 型態
        'user': os.getenv('MYSQL_USER'),
        'password': os.getenv('MYSQL_PASSWORD'),
        'database': os.getenv('MYSQL_DATABASE')
    }

    mydb = mysql.connector.connect(**db_config)
    cursor = mydb.cursor()
    
    
    return mydb, cursor 


# def sample():
#     db, cursor = connect()

#     cursor.execute("SHOW TABLES") ## put your schema here
#     tables = cursor.fetchall()  
#     if not tables:
#         print('no table')
#     else:
#         for table in tables:
#             print(table)

#     return <RETURN YOURS>