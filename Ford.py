#Importing librabries

import pandas as pd
import numpy as np
import matplotlib as plt
import seaborn as sns

#Search Dataset path

data_filepath = 'C:/Users/Marcelo Sampaio/Desktop/Datasets/ford.csv'
my_data = pd.read_csv(data_filepath)
my_data.head()

#Transform U$ in R$ and Mileage in Kilometers

my_data['price'] = my_data['price'] * 5.11
my_data['mileage'] = my_data['mileage'] * 1.61

#Rename the Dataframe columns and check info
my_data.rename(columns={'price':'price_R$', 'mileage':'kilometers'}, inplace=True)
my_data.head()
my_data.describe()

#Number of cars X Kilometers traveled

sns.distplot(my_data['kilometers'], kde=False)