import csv
import pandas as pd
  
df = pd.read_csv('Airbnb_Open_Data.csv')
print(df.head())
print(df.info())