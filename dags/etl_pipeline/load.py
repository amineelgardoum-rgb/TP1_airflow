import pandas as pd
from io import StringIO
def load(path,**kwargs):
    ti=kwargs['ti']
    csv_str=ti.xcom_pull(key='df',task_ids='process')
    df=pd.read_csv(StringIO(csv_str))
    df.to_csv(path,index=False)
    print("data processed successfully!")
    print("data Loaded successfully!")
    