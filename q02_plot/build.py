# %load q02_plot/build.py
# Default Imports
import pandas as pd
import matplotlib.pyplot as plt
from greyatomlib.descriptive_stats.q01_calculate_statistics.build import calculate_statistics

plt.switch_backend('agg')
dataframe = pd.read_csv('data/house_prices_multivariate.csv')
sale_price = dataframe.loc[:, 'SalePrice']


# Draw the plot for the mean, median and mode for the dataset

list_1 = calculate_statistics()
def plot():
    list_1 = calculate_statistics()
    plt.hist(sale_price)
    plt.axvline(list_1[0])
    plt.axvline(list_1[1])
    plt.axvline(list_1[2])
    plt.show()

#calculate_statistics()
plot()

