import pandas as pd
from io import StringIO
def load(**kwargs):
    ti=kwargs['ti']
    csv_str=ti.xcom_pull(key='df',task_ids='process')
    df=pd.read_csv(StringIO(csv_str))
    df.to_csv('/opt/airflow/data/processed_ventes.csv',index=False)
    print("data processed successfully!")
    