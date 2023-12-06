import pandas as pd
df = pd.read_csv('part_titanic.csv')
print(f"Before (missed age total): {df.Age.isna().sum()}")
mean_age = float(f"{df.Age.mean():.2}")
print(f"Mean age: {mean_age}")

df.Age.fillna(mean_age, inplace=True)
print(f"After (missed age total): {df.Age.isna().sum()}")


df.to_csv('filled_age_titanic.csv', index=False)