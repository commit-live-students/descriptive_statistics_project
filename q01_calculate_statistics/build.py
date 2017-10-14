# Default Imports
import numpy as np
import pandas as pd

data = pd.read_csv('data/house_prices_multivariate.csv')
sale_price = data.loc[:, "SalePrice"]

def calculate_statistics():
    mean = sale_price.mean()
    median = sale_price.median()
    temp_mode = sale_price.mode()
    mode = np.int64(temp_mode)
    return mean ,median ,mode
# Return mean,median & mode for the SalePrice Column
# Write your code here
