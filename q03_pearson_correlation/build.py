# Default Imports
import pandas as pd

dataframe_1 = pd.read_csv('data/house_prices_multivariate.csv')
dataframe_2 = pd.read_csv('data/house_prices_copy.csv')
sale_price1 = dataframe_1.loc[:, "SalePrice"]
sale_price2 = dataframe_2.loc[:, "SalePrice"]
#print dataframe_2[:10]

# Return the correlation value between the SalePrice column for the two loaded datasets
# Your code here
def correlation():
    sale_correlation = sale_price1.corr(sale_price2)

    return sale_correlation
print correlation()
