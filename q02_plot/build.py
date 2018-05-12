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
    plt.hist(sale_price)
    meanVal = sale_price.mean()
    medianVal = sale_price.median()
    modeVal = sale_price.mode()
    plt.axvline(meanVal,color='red')
    plt.axvline(medianVal,color='yellow')
    plt.axvline(modeVal[0],color='green')
    plt.plot()
plot()


