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
    mode = sale_price.mode()
    plt.hist(sale_price)
    plt.plot([mean]*800, range(800), label = 'mean')
    plt.plot([median]*800,range(800),label = 'median')
    plt.plot([mode]*800,range(800),label = 'mode')
    plt.legend()
    plt.ylim(0,750)
    plt.xlabel('Sale Price')
    plt.title('Sale Price distribution with central tendency')
    plt.show
# Draw the plot for the mean, median and mode for the dataset
