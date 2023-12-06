import pandas as pd

train_df = pd.read_csv('titanic.csv')

X = train_df[["Pclass", "Sex", "Age"]]
y = train_df["Survived"]

X.reset_index(drop=True)

print(X.head())
X.to_csv('part_titanic.csv', index=False)