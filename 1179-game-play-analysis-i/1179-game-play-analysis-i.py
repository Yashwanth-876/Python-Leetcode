import pandas as pd

def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    activity = activity.sort_values(by = ['player_id', 'event_date'])
    activity = activity.drop_duplicates('player_id')
    result = activity[['player_id', 'event_date']].rename(columns={'event_date': 'first_login'}).sort_values(by='player_id')
    return result
    