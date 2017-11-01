# Default Imports
import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt
from greyatomlib.descriptive_stats.q01_calculate_statistics.build import calculate_statistics

data = pd.read_csv('data/house_prices_multivariate.csv')
sale_price = data.loc[:, "SalePrice"]

def plot():
    mean = sale_price.mean()
    median = sale_price.median()
    mode = sale_price.mode()
    plt.hist(sale_price)
    plt.axvline(mean, color='k', linestyle='--')
    plt.axvline(median, color='r', linestyle='--')
    plt.axvline(mode[0], color='b', linestyle='--')
    plt.show()
plot()
