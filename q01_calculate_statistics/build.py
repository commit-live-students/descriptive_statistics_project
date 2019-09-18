# Default Imports
import numpy as np
import pandas as pd

data = pd.read_csv('data/house_prices_multivariate.csv')
sale_price = data.loc[:, "SalePrice"]


# Return mean,median & mode for the SalePrice Column
# Write your code here
def calculate_statistics():
    Mean = sale_price.mean()
    Median = sale_price.median()
    Mode = sale_price.mode()

    print type(Mean)
    print type(Median)
    print type(Mode[0])
    return Mean,Median,Mode[0]

print calculate_statistics()
