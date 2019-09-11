# Default Imports
import numpy as np
import pandas as pd

def calculate_statistics():
    data = pd.read_csv('data/house_prices_multivariate.csv')
    sale_price = data.loc[:, "SalePrice"]
    sale_price_mean = sale_price.mean()
    sale_price_median = sale_price.median()
    sale_price_mode = np.int64(sale_price.mode())
    return sale_price_mean, sale_price_median, sale_price_mode



# Return mean,median & mode for the SalePrice Column
# Write your code here
