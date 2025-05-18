import psycopg2

try:
    connection = psycopg2.connect(
        user="myuser",
        password="mypass",
        host="localhost",
        port="5432",
        database="mydb"
    )
    cursor = connection.cursor()
    cursor.execute("SELECT version();")
    record = cursor.fetchone()
    print("PostgreSQL is working! we WOnn Version:", record)

except Exception as e:
    print("Fall Backk:", e)

finally:
    if connection:
        cursor.close()
        connection.close()