"""
INFO about postgresql:
https://www.cherryservers.com/blog/how-to-install-and-setup-postgresql-server-on-ubuntu-20-04

"""

import psycopg2, os, ssl
from dotenv import load_dotenv

#CREATES TABLES
#create_table_query = """
#CREATE TABLE urlInfo (
#    id serial PRIMARY KEY,
#    urlName VARCHAR
#)
#"""
#cursor.execute(create_table_query)

class PostgresqlDB():

    def dbParseUrl(url):

        # Load environment variables from .env file
        load_dotenv('environmentVariables.env')

        # Retrieve the value of the environment variable
        password = os.environ.get('POSTGRESQL_PASSWORD')

        conn = psycopg2.connect(
            host="192.168.1.14",
            port=5432,
            database="links",
            user="postgres",
            password=password,
        ) 

        cursor = conn.cursor()

        insert_query = "INSERT INTO urlInfo (urlName) VALUES (%s)"
        data = [url] 

        cursor.execute(insert_query, data)

        #Commit the transaction to make the changes permanent
        conn.commit()

        #After executing the queries, close the cursor and the database connection
        cursor.close()
        conn.close()


