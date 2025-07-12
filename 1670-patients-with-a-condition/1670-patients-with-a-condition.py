import pandas as pd
# 30Days Q9
def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    result = patients['conditions'].str.contains(' DIAB1') | patients['conditions'].str.startswith('DIAB1')
    return patients[result]
    