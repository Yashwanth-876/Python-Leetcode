import pandas as pd
# 30Days Q5
def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    df = tweets[tweets['content'].str.len() > 15][['tweet_id']]
    return df