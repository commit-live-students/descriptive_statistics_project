# Default Imports
import numpy as np
import pandas as pd

data = pd.read_csv('data/house_prices_multivariate.csv')
sale_price = data.loc[:, "SalePrice"]


# Return mean,median & mode for the SalePrice Column
# Write your code here
def calculate_statistics():
    mean=sale_price.mean()
    median=sale_price.median()
    mode_series=sale_price.mode()
    mode=mode_series[0]
    return mean,median,mode
