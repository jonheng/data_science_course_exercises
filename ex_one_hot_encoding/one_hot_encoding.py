import pandas as pd

df = pd.read_csv('car.csv')
print(df.head())
print(df['Brand'].unique())

# Shows count of each unique value
print(df['Brand'].value_counts())

df = pd.get_dummies(df, columns=['Brand'])

df.to_csv('one_hot_encoding_car.csv')
