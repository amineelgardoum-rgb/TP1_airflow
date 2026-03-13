import pandas as pd
from io import StringIO
def read_csv_file(path:str,**kwargs):
    """
    Args:
        path (str): the path to the data csv file

    Returns:
        pd.DataFrame: data frame object from the csv file 
    """
    print(f"Reading data from :{path}.")
    df=pd.read_csv(path) # read the csv file
    csv_buffer=StringIO()
    df.to_csv(csv_buffer,index=False)
    ti=kwargs['ti']
    ti.xcom_push(key='df',value=csv_buffer.getvalue())
    print("the csv file is ready to be used.")
     