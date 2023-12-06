import catboost.datasets as cbd
import pandas as pd

titanic_df = cbd.titanic()[0]

titanic_df.to_csv('titanic.csv', index=False)