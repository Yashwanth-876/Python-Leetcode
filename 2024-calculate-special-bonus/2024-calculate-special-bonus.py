import pandas as pd
# 30Days Q6
def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    conditions = (employees['employee_id'] % 2 == 1) & (~employees['name'].str.startswith('M'))
    employees['bonus'] = employees['salary'] * conditions
    return employees[['employee_id','bonus']].sort_values("employee_id")
