# Default Imports
import numpy as np
import pandas as pd

data = pd.read_csv('data/house_prices_multivariate.csv')
sale_price = data.loc[:, "SalePrice"]

# Return mean,median & mode for the SalePrice Column
def calculate_statistics():
    mean = pd.Series.mean(sale_price)
    median = pd.Series.median(sale_price)
    mode = pd.Series.mode(sale_price)

    return mean, median, mode

calculate_statistics()
