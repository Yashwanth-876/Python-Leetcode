import pandas as pd
# 13
def meltTable(report: pd.DataFrame) -> pd.DataFrame:
    report = report.melt(
        id_vars = 'product',
         var_name = 'quarter',
          value_name = 'sales'
)
    return report