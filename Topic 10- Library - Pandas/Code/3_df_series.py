import pandas as pd

d = {
    "one": pd.Series([1, 2, 3], index = ['a', 'b', 'c']),
    "two": pd.Series([21, 22, 23], index = ['a', 'c', 'b'])
}

df = pd.DataFrame(d)

print(df)