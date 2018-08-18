# %load q02_plot/build.py
# Default Imports
import pandas as pd
import matplotlib.pyplot as plt
from greyatomlib.descriptive_stats.q01_calculate_statistics.build import calculate_statistics
import numpy as np
plt.switch_backend('agg')
dataframe = pd.read_csv('data/house_prices_multivariate.csv')
sale_price = dataframe.loc[:, 'SalePrice']
def plot():
    mean=np.mean(sale_price)
    median=sale_price.median()
    mode=sale_price.mode()
    mode=mode[0]
    plt.figure(figsize=(10, 6))
    plt.hist(sale_price, bins=40)
    plt.plot([mode]*300, range(300), label='mode')
    plt.plot([median]*300, range(300), label='median')
    plt.plot([mean]*300, range(300), label='mean')
    plt.ylim(0, 250)
    plt.legend()
    plt.show()
    return


plot()




