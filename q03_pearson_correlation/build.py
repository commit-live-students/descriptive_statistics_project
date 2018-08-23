# %load q03_pearson_correlation/build.py
# Default Imports
import pandas as pd

dataframe_1 = pd.read_csv('data/house_prices_multivariate.csv')
dataframe_2 = pd.read_csv('data/house_prices_copy.csv')
def correlation():
    x = pd.DataFrame(dataframe_1.SalePrice)
    y = pd.DataFrame(dataframe_2.SalePrice)
    y.rename(columns={'SalePrice':'SalePrice2'},inplace=True)
    x=x.join(y)
    answer = x.corr()['SalePrice'][1]
    return answer

    

# Return the correlation value between the SalePrice column for the two loaded datasets
# Your code here

correlation()

