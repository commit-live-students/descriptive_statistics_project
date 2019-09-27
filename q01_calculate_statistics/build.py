# Default Imports
import numpy as np
import pandas as pd

data = pd.read_csv('data/house_prices_multivariate.csv')
sale_price = data.loc[:, "SalePrice"]


# Return mean,median & mode for the SalePrice Column
# Write your code here
def calculate_statistics():
    # print type(sale_price)
    sp_mean = sale_price.mean()
    sp_median = sale_price.median()
    sp_mode = sale_price.mode()[0]
    return (sp_mean, sp_median, sp_mode)
