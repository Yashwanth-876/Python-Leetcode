import pandas as pd 

# 3

def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    df = employees.head(3)
    return df
    