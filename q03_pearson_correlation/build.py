# %load q03_pearson_correlation/build.py
# Default Imports
import pandas as pd

dataframe_1 = pd.read_csv('data/house_prices_multivariate.csv')
dataframe_2 = pd.read_csv('data/house_prices_copy.csv')

# Return the correlation value between the SalePrice column for the two loaded datasets
# Your code here
def correlation():
#    datafrane1 = datafrane_1 .iloc[:1,3:] #the single row record
 #   dataframe2 =   dataframe_2.iloc[1:,3:]   #the remaining records.
   # Top15['Citable docs per Capita'].corr(Top15['Energy Supply per Capita'])
    return dataframe_1['SalePrice'].corr(dataframe_2['SalePrice'])
      














correlation()


