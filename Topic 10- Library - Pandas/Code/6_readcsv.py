import pandas as pd

df = pd.read_csv("fastfood_NJ.csv")
name = df['name']

rating = df['rating'].to_numpy()

# print(name)
print(rating)