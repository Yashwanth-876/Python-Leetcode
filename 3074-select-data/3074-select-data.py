import pandas as pd
# 4
def selectData(students: pd.DataFrame) -> pd.DataFrame:
    df = students[students['student_id'] == 101]
    return df[['name','age']]
    