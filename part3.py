import pandas as pd
from sklearn.preprocessing import OneHotEncoder

df = pd.read_csv('filled_age_titanic.csv')

#creating instance of one-hot-encoder
encoder = OneHotEncoder(handle_unknown='ignore')

#perform one-hot encoding on 'Sex' column 
encoder_df = pd.DataFrame(encoder.fit_transform(df[['Sex']]).toarray())

#merge one-hot encoded columns back with original DataFrame
final_df = df.join(encoder_df)

#view final df
print(final_df.head())

#drop 'Sex' column
final_df.drop('Sex', axis= 1 , inplace= True )

final_df.columns = ['Pclass', 'Age', 'is_female', 'is_male']
print(final_df.head())

final_df.to_csv('ohe_sex_titanic.csv', index=False)