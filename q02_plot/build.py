# %load q02_plot/build.py
# Default Imports
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from greyatomlib.descriptive_stats.q01_calculate_statistics.build import calculate_statistics

dataframe = pd.read_csv('data/house_prices_multivariate.csv')
sale_price = dataframe.loc[:, 'SalePrice']


# Draw the plot for the mean, median and mode for the dataset
def plot():
    plt.hist(sale_price)
    plt.axvline(x=mean,label='mean',color='r')
    plt.axvline(x=median,label='median',color='w')
    plt.axvline(x=mode[0],label='mode',color='y')


    plt.legend()
    plt.show()
