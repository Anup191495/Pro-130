import pandas as pd
import csv

df = pd.read_csv('merged_dataset.csv')

del df['Luminosity']

print(df.shape)

df.to_csv('Main.csv')