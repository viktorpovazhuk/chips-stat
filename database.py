import os
import psycopg2
import pandas as pd

DATABASE_URL = os.environ['DATABASE_URL']
# DATABASE_URL = "postgresql://postgres@localhost:5432/linuxhint"


def fetch():
    conn = psycopg2.connect(DATABASE_URL, sslmode='require')
    cur = conn.cursor()
    query = f"""SELECT * 
                 FROM users 
                 """
    results = pd.read_sql(query, conn)
    # print(results)
    return results
