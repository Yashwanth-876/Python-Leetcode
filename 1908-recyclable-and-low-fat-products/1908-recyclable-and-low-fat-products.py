import pandas as pd
# 30days Q2
def find_products(products: pd.DataFrame) -> pd.DataFrame:
    df = products[(products['low_fats'] == 'Y') & (products['recyclable'] 
    ==  'Y')]
    return df[['product_id']]
    