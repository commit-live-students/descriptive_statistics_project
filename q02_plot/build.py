# Default Imports
import pandas as pd
import matplotlib.pyplot as plt
from greyatomlib.descriptive_stats.q01_calculate_statistics.build import calculate_statistics

plt.switch_backend('agg')
dataframe = pd.read_csv('data/house_prices_multivariate.csv')
sale_price = dataframe.loc[:, 'SalePrice']


def plot():
    mean = sale_price.mean()
    median = sale_price.median()
    mode = np.int64(sale_price.mode())

    plt.axvline(x=mean)
    plt.axvline(x=median)
    plt.axvline(x=mode)

   # plt.hist(median, bins=10)

plt.show()
