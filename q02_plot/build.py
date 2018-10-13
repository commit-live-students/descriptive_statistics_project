import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from greyatomlib.descriptive_stats.q01_calculate_statistics.build import calculate_statistics

plt.switch_backend('agg')
dataframe = pd.read_csv('data/house_prices_multivariate.csv')
sale_price = dataframe.loc[:, 'SalePrice']

def plot():
    plt.figure()
    sale_price.hist(bins=60)
    plt.axvline(x=sale_price.mean(),label='mean')
    plt.axvline(x=sale_price.median(),label='median')
    plt.axvline(x=np.array(sale_price.mode())[0],label='mode')
    plt.legend()
    plt.show();
    
    return


plot()





