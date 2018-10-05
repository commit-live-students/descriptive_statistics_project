# %load q02_plot/build.py
# Default Imports
import pandas as pd
import matplotlib.pyplot as plt
from greyatomlib.descriptive_stats.q01_calculate_statistics.build import calculate_statistics
plt.switch_backend('agg')
dataframe = pd.read_csv('data/house_prices_multivariate.csv')
sale_price = dataframe.loc[:, 'SalePrice']


# Draw the plot for the mean, median and mode for the dataset
def plot():
    plt.hist(sale_price)
    plt.axvline(sale_price.mean(),color='r',linestyle='--')
    plt.axvline(sale_price.median(), color='g', linestyle='-')
    plt.axvline(sale_price.mode()[0], color='b', linestyle='-')
    plt.legend({'Mean':sale_price.mean(),'Median':sale_price.median(),'Mode':sale_price.mode()[0]})
    plt.show()
plot()


