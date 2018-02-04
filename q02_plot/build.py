# %load q02_plot/build.py
# Default Imports
import pandas as pd
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt
from greyatomlib.descriptive_stats.q01_calculate_statistics.build import calculate_statistics

dataframe = pd.read_csv('data/house_prices_multivariate.csv')
sale_price = dataframe.loc[:, 'SalePrice']


# Draw the plot for the mean, median and mode for the dataset
def plot():
    me = float(sale_price.mean())
    med = float(sale_price.median())
    mo = float(sale_price.mode())
    #sale_price.plot(kind='hist')
    plt.axvline(x=me)
    plt.axvline(x=med)
    plt.axvline(x=mo)
    plt.show()


plot()
