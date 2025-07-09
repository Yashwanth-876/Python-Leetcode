import pandas as pd
# 12
def pivotTable(weather: pd.DataFrame) -> pd.DataFrame:
    weather = weather.pivot(index = 'month', columns = 'city', values = 'temperature')
    return weather
    