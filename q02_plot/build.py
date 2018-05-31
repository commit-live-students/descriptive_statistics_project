# %load q02_plot/build.py
# Default Imports
import pandas as pd
import matplotlib.pyplot as plt
from greyatomlib.descriptive_stats.q01_calculate_statistics.build import calculate_statistics

dataframe = pd.read_csv('data/house_prices_multivariate.csv')
sale_price = dataframe.loc[:, 'SalePrice']


# Draw the plot for the mean, median and mode for the dataset
def plot():
    mean,median,mode=calculate_statistics()
#     print(mean,median,mode)
    plt.hist(sale_price)
    plt.axvline(mean,color='red')
    plt.axvline(median,color='yellow')
    plt.axvline(mode,color='green')
    plt.show()

plot()

