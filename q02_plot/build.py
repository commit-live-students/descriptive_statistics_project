# %load q02_plot/build.py
# Default Imports
import pandas as pd
import matplotlib.pyplot as plt
from greyatomlib.descriptive_stats.q01_calculate_statistics.build import calculate_statistics
def plot():
    dataframe = pd.read_csv('data/house_prices_multivariate.csv')
    sale_price = dataframe.loc[:, 'SalePrice']
    m=sale_price.mean()
    me=sale_price.median()
    mo=sale_price.mode()[0]
    plt.hist(sale_price, normed=True, bins=30)
    plt.axvline(m, color = 'r', linestyle = 'dashed', linewidth = 2)
    plt.axvline(me, color = 'g', linestyle = 'dashed', linewidth = 3)
    plt.axvline(mo, color = 'b', linestyle = 'dashed', linewidth = 4)
    return plt.show()
#plot()
# Draw the plot for the mean, median and mode for the dataset
