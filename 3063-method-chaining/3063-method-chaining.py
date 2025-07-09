import pandas as pd
# 14
def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:
    animal_weight = animals[animals['weight'] > 100 ]
    animal_order = animal_weight.sort_values(by = 'weight',ascending = False)
    return animal_order[['name']]
    