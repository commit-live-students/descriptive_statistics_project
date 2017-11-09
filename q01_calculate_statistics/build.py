# Default Imports
import numpy as np
import pandas as pd

data = pd.read_csv('data/house_prices_multivariate.csv')
sale_price = data.loc[:, "SalePrice"]

# Return mean,median & mode for the SalePrice Column
# Write your code here
def calculate_statistics():
    means = sale_price.mean()
    median = sale_price.median()
    arr = np.array(sale_price)
    bcount = np.bincount(arr)
    modes = np.argmax(bcount)

    return means,median,modes
