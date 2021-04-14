import os
import psycopg2
import pandas as pd

# DATABASE_URL = os.environ['DATABASE_URL']
# DATABASE_URL = "postgresql://postgres@localhost:5432/linuxhint"


DATABASE_URL = "postgres://inzrarrburisae:ce434db881dbfda4a6227e2eec" \
               "a32e2685f6cfd55ab1a2ac66ac7f28a1432651@" \
               "ec2-34-195-233-155.compute-1.amazonaws.com:5432/dd7opeb1svvj6h"

class DBWorker:
    def __init__(self):
        self._connection = None
        # self._cursor = None

    def add_user(self):
        # cur.execute("INSERT INTO students (name, mail) VALUES (%(name)s, %(mail)s)",
        #             {'mail': "ddd@gmail.com", 'name': "Bon Doron"})

        # provides auto commit and close
        with self._connection:
            with self._connection.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO students (name) VALUES (%(name)s);",
                    {'name': "Viktor"})

        # save changes
        # self._connection.commit()

    def get_users(self):
        query = f"""SELECT * 
                     FROM students 
                     """
        # results = pd.read_sql(query, self._connection)
        # print(results)
        with self._connection:
            with self._connection.cursor() as cursor:
                cursor.execute(query)
                results = cursor.fetchall()

        return results

    def delete_user(self, id):
        with self._connection:
            with self._connection.cursor() as cursor:
                cursor.execute("DELETE FROM students "
                               "WHERE id = %s", (id,))

    def update_user(self, id, new_name):
        with self._connection:
            with self._connection.cursor() as cursor:
                cursor.execute("UPDATE students "
                               "SET name = %(name)s "
                               "WHERE id = %(id)s", {'id': id, 'name': new_name})

    def open_connection(self):
        self._connection = psycopg2.connect(DATABASE_URL)  # , sslmode='require'
        print('Database connection opened.')


    def close_connection(self):
        if self._connection is not None:
            self._connection.close()
            print('Database connection closed.')


worker = DBWorker()

# def add_user():
#     conn = psycopg2.connect(DATABASE_URL) # , sslmode='require'
#     cur = conn.cursor()
#
#     # cur.execute("INSERT INTO students (name, mail) VALUES (%(name)s, %(mail)s)",
#     #             {'mail': "ddd@gmail.com", 'name': "Bon Doron"})
#     cur.execute("INSERT INTO students (id) VALUES (%(id)s)",
#                 {'id': 1})
#
#     if conn is not None:
#         conn.close()
#         print('Database connection closed.')


# def fetch():
#     conn = psycopg2.connect(DATABASE_URL, sslmode='require')
#     cur = conn.cursor()
#
#     query = f"""SELECT *
#                  FROM students
#                  """
#     results = pd.read_sql(query, conn)
#     # print(results)
#
#     if conn is not None:
#         conn.close()
#         print('Database connection closed.')
#
#     return results


# def execute_query(query, conn):
