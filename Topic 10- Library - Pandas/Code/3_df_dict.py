import pandas as pd

d = {
    "one": [1, 2, 3],
    "two": [21, 22, 23]
}

df = pd.DataFrame(d)

df.to_csv('data.csv')

# print(df)

# print(df.shape)
# print(df.columns)
# print(df.index)

