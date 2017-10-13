# %load q01_calculate_statistics/build.py
# Default Imports
import numpy as np
import pandas as pd

data = pd.read_csv('data/house_prices_multivariate.csv')
sale_price = data.loc[:, "SalePrice"]
def calculate_statistics():
    x=data["SalePrice"].median()
    y=data["SalePrice"].mean()
    z=data["SalePrice"].mode()[0]
    return (y,x,z)
#calculate_statistics()
# Return mean,median & mode for the SalePrice Column
# Write your code here
