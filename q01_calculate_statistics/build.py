# Default Imports
import numpy as np
import pandas as pd

data = pd.read_csv('./data/house_prices_multivariate.csv')
sale_price = data.loc[:, "SalePrice"]

def calculate_statistics():
    mean = float(np.mean(sale_price))
    median = float(np.median(sale_price))
    mode = sale_price.mode()
    return mean,median,mode.iloc[0]
#m1,m2,m3 = calculate_statistics()
#print (m1,m2,m3)
#print (type(m1))
#print (type(m2))
#print (type(m3))
