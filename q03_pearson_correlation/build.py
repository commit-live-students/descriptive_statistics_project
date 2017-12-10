# Default Imports
import pandas as pd
from scipy import stats

dataframe_1 = pd.read_csv('data/house_prices_multivariate.csv')
dataframe_2 = pd.read_csv('data/house_prices_copy.csv')


# Return the correlation value between the SalePrice column for the two loaded datasets
# Your code here

def correlation():
    sales_price_1 = dataframe_1.loc[:,'SalePrice']
    #print sales_price_1
    sales_price_2 = dataframe_2.loc[:,'SalePrice']
    #print sales_price_2

    pearson_coeff = stats.pearsonr(sales_price_1,sales_price_2)

    return pearson_coeff[0]
