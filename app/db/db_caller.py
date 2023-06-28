import os
import pyodbc
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


def call_sp(procedure_name, *args):
    server = os.environ.get("DB_SERVER")
    database = os.environ.get("DB_DATABASE")
    username = os.environ.get("DB_USERNAME")
    password = os.environ.get("DB_PASSWORD")
    driver = os.environ.get("DB_DRIVER")

    conn = pyodbc.connect(f"DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password}")
    cursor = conn.cursor()

    try:
        param_placeholders = ', '.join(['?' for _ in args])
        call_statement = f"EXEC {procedure_name} {param_placeholders}"
        cursor.execute(call_statement, args)
        cursor.commit()
        results = cursor.fetchall()

        return [dict(zip([column[0] for column in cursor.description], row)) for row in results]

    except pyodbc.Error as e:
        # Handle any errors that occur
        print(f"Error executing stored procedure: {e}")

    finally:
        # Close the connection
        cursor.close()
        conn.close()
