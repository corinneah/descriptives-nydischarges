# import packages 
import pandas as pd
import researchpy as rp
from tableone import TableOne, load_dataset
import numpy as np 
from scipy import stats
import matplotlib.pyplot as plt 



df = pd.read_csv('data/Hospital_SPARCS_2016.csv')
df.columns
df.shape
df.dtypes

df.isnull().sum()

# clean data a little bit
df = df.drop_duplicates(keep='first')
df = df.dropna()

#Gender 
groupby_gender = df.groupby('gender')
groupby_gender.mean()

#Age and Length
groupby_age = df.groupby('age_group')['length_of_stay'].mean()
fig, ax = plt.subplots()

# scatter plot for patient and cost 
x= data['total_costs']
y=data['facility_id']
graph2 =plt.scatter(x,y)
plt.xlabel('total_costs') 
plt.ylabel('facility_id') 
plt.show()

#tableone 
df_columns = ['length_of_stay', 'race', 'type_of_admission', 'gender']
df_categorical = ['race', 'gender']
df_groupby = ['type_of_admission']
df_labels={'length_of_stay': 'los'}

dftab1 = TableOne(df, columns=df_columns, categorical=df_categorical, groupby=df_groupby, rename=df_labels, pval=False) 
print(dftab1.tabulate(tablefmt = "fancy_grid"))