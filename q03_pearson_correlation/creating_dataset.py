import pandas as pd
import random

dataframe = pd.read_csv('../data/house_prices_multivariate.csv')
sale_price = dataframe.loc[:, 'SalePrice']
sale_price_copy = [0]*len(sale_price)

for i in range(len(sale_price)):
    sign = random.randint(0,2)
    if sign%2 == 0:
        sale_price_copy[i] = sale_price[i]+random.randint(1000, 10000)**1.7
    else:
        sale_price_copy[i] = sale_price[i]-random.randint(1000, 10000)**1.7

dataframe['SalePrice'] = pd.Series(sale_price_copy)
dataframe.to_csv('../data/house_prices_copy.csv', index=False)

dataframe_1 = pd.read_csv('../data/house_prices_multivariate.csv')
dataframe_2 = pd.read_csv('../data/house_prices_copy.csv')
print(dataframe_1.SalePrice.corr(dataframe_2.SalePrice))
print(dataframe_1.SalePrice.corr(dataframe_2.SalePrice, method="spearman"))