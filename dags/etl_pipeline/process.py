import pandas as pd
from io import StringIO
def process_csv_file(**kwargs):
    """
    Args:
        df (pd.DataFrame): data frame that holds the data 

    Returns:
        pd.DataFrame: processed data
    """
    print("Begin the processing.")
    ti=kwargs['ti']
    csv_str=ti.xcom_pull(key='df',task_ids='read')
    df=pd.read_csv(StringIO(csv_str))
    df=df.dropna()
    df=df.drop_duplicates()
    csv_buffer=StringIO()
    df.to_csv(csv_buffer,index=False)
    ti.xcom_push(key='df',value=csv_buffer.getvalue())
    
    
    