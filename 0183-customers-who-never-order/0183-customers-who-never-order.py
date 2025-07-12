import pandas as pd
# 30Days Q3
def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    df = pd.merge(customers, orders,left_on ='id',right_on ='customerId',  how = 'left')
    df = df[df['customerId'].isnull()]
    return df.rename(columns = {'name':'customers'})[['customers']]
