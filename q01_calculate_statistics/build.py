import numpy as np
import pandas as pd

data = pd.read_csv('data/house_prices_multivariate.csv')
sale_price = data.loc[:, 'SalePrice']

def calculate_statistics():
# Return mean,median & mode for the SalePrice Column
# Write your code here
    m1 = np.mean(sale_price)
    m2 = np.median(sale_price)
    m3 = sale_price.mode()[0]
    return m1, m2, m3

calculate_statistics()



