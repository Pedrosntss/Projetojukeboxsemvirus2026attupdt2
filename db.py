import os
from dotenv import load_dotenv

from mysql.connector import connect

load_dotenv()

def connect_db():
    connection = connect(
        host = os.getenv('HOST'),
        user = os.getenv('USER'),
        password = os.getenv('PSW'),
        database = os.getenv('DATABASE')
    )

    cursor = connection.cursor()
    return cursor, connection

def close_connection(cursor,connection):
    cursor.close()
    connection.close()

def execute_sql(query, params = None):
    cursor, connection = connect_db()

    data = None
    try:
        if params:
            cursor.execute(
                    query, params
                )
        else:
            cursor.execute(query)

        data = cursor.fetchall()
        connection.commit()
    except Exception as e:
        print(f'Erro: {e}')
    finally:
        close_connection(cursor,connection)

        return data


if __name__ == '__main__':
    query = f'insert into()'
    print(execute_sql(query))

    print(execute_sql(query, (id,)))
