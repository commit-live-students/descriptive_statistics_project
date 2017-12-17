# Default Imports
import numpy as np
import pandas as pd

data = pd.read_csv('data/house_prices_multivariate.csv')
sale_price = data.loc[:, "SalePrice"]

def calculate_statistics():
    mean = sale_price.mean()
    median = sale_price.median()
    mode = np.int64(sale_price.mode())

    return (mean, median, mode)
