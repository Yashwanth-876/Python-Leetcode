import pandas as pd
# 30Days Q6
def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    conditions = (employees['employee_id'] % 2 == 1) & (~employees['name'].str.startswith('M'))
    employees['bonus'] = employees['salary'] * conditions
    return employees[['employee_id','bonus']].sort_values("employee_id")



# import pandas as pd

# def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
#     df = employees
#     df.loc[df['name'].str.startswith('M'), 'salary'] = 0
#     df.loc[df['employee_id'] % 2 == 0, 'salary'] = 0
#     df = df[['employee_id', 'salary']].rename(columns={'salary' : 'bonus'})
#     return df.sort_values(by=['employee_id'])
