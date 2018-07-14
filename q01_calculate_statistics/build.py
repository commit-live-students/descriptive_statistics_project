# Default Imports
import numpy as np
import pandas as pd

data = pd.read_csv('data/house_prices_multivariate.csv')
sale_price = data.loc[:, "SalePrice"]


# Return mean,median & mode for the SalePrice Column
# Write your code here
def calculate_statistics():
    mean=pd.to_numeric(sale_price.mean(), downcast='float')
    median=pd.to_numeric(sale_price.median(), downcast='float')
    mode=pd.to_numeric(sale_price.mode(), downcast='signed')
    return(mean,median,mode)
