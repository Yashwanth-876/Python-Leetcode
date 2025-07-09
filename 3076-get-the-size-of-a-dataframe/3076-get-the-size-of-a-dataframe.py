import pandas as pd
# 2
def getDataframeSize(players: pd.DataFrame) -> List[int]:
    df = list(players.shape)
    return df