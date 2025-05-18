from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import csv
import psycopg2

default_args = {
    'start_date': datetime(2025, 3, 5),
}

dag= DAG(
    dag_id='load_csv_to_postgres',
    default_args=default_args,
    description='ETL DAG to load CSV into PostgreSQL',
    schedule=None,
    catchup=False,
)

def load_csv_to_postgres():
    conn = psycopg2.connect(
        host='host.docker.internal', #to connect from airflow container to your local machine
        port='5432',
        database='your_database',
        user='your_username',
        password='your_password'
    )
    cur = conn.cursor()

    with open('/opt/airflow/data/fake_users.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            cur.execute("""
                        INSERT INTO users(id, name, email, address, created_at)
                        VALUES (%s, %s, %s, %s, %s)
                        ON CONFLICT (id) DO NOTHING
                        """, (row['id'], row['name'], row['email'], row['address'], row['created_at']))
    conn.commit()
    cur.close()
    conn.close()
    print("Data loaded into PostgreSQL")

load_task = PythonOperator(
    task_id='load_csv',
    python_callable=load_csv_to_postgres,
    dag=dag,
)
            
