from mysql.connector import connect, Error
import os
from dotenv import load_dotenv

load_dotenv()

def get_content():
    try:
        with connect(
            host=os.getenv('DB_HOST'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASS'),
            database=os.getenv('DB_NAME'),
        ) as connection:
            select_movies_query = "SELECT * FROM content LIMIT 5"
            with connection.cursor() as cursor:
                cursor.execute(select_movies_query)
                result = cursor.fetchall()
                return result
    except Error as e:
        return e
