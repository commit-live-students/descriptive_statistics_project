# Default Imports
import numpy as np
import pandas as pd

data = pd.read_csv('data/house_prices_multivariate.csv')
sale_price = data.loc[:, "SalePrice"]

def calculate_statistics():
    means = sale_price.mean()
    medians = sale_price.median()
    arr = np.array(sale_price)
    bcount = np.bincount(arr)
    modes = np.argmax(bcount)
    return means, medians, modes


# Return mean,median & mode for the SalePrice Column
# Write your code here
