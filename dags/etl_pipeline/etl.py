from airflow import DAG
from airflow.operators.python import PythonOperator #type: ignore
from datetime import datetime,timedelta
from etl_pipeline.read_csv import read_csv_file
from etl_pipeline.process import process_csv_file
from etl_pipeline.load import load 
default_args={
    'owner':'me',
    'retries':1,
    'retry_delay':timedelta(minutes=5)
}
with DAG(
    dag_id='etl_pipeline',
    default_args=default_args,
    schedule='@daily',
    start_date=datetime(2024,1,1),
    catchup=False
) as dag:
    read_csv = PythonOperator(
        task_id="read",
        python_callable=read_csv_file,
        op_kwargs={'path': '/opt/airflow/data/ventes.csv'}  
    )
    process=PythonOperator(
        task_id="process",
        python_callable=process_csv_file,
    )
    load=PythonOperator(
        task_id='load',
        python_callable=load
    )
    read_csv >> process >> load 