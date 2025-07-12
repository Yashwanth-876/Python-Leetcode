import pandas as pd
# 30Days Q4
def article_views(views: pd.DataFrame) -> pd.DataFrame:
    df = views[views['author_id'] == views['viewer_id']]
    df = df.rename(columns = {'author_id':'id'})
    df = df[['id']].drop_duplicates()
    return df.sort_values('id').reset_index(drop = True)[['id']]
    