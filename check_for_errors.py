

import pandas as pd 

generator = {
    'barbel curl': [0,0,0]
}

df = pd.DataFrame(generator)

print(df)
df.to_csv('exercises.csv')
