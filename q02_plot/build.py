# %load q02_plot/build.py
# Default Imports
import pandas as pd
import matplotlib.pyplot as plt
from greyatomlib.descriptive_stats.q01_calculate_statistics.build import calculate_statistics
plt.switch_backend('agg')
dataframe = pd.read_csv('data/house_prices_multivariate.csv')
sale_price = dataframe.loc[:, 'SalePrice']

mean= sale_price.mean()
median= sale_price.median()
mode = sale_price.mode()[0]


def plot():
    plt.figure(figsize=(10, 6))
    plt.hist(sale_price, bins=40)
    
    plt.axvline(mode,color='r')
    plt.axvline(median,color='g')
    plt.axvline(mean,color='y')
    plt.ylim(0, 250)
    plt.legend()
    plt.show();
plot()


