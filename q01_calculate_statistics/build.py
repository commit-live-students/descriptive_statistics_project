# Default Imports
import numpy as np
import pandas as pd

data = pd.read_csv('data/house_prices_multivariate.csv')
sale_price = data.loc[:, "SalePrice"]


# Return mean,median & mode for the SalePrice Column
# Write your code here
def calculate_statistics():
    me = float(sale_price.mean())
    med = float(sale_price.median())
    mo = np.array(sale_price.mode(),dtype=np.int64)
    return me, med, mo[0]
