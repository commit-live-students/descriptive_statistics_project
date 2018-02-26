# Default Imports
import pandas as pd
import matplotlib.pyplot as plt
from greyatomlib.descriptive_stats.q01_calculate_statistics.build import calculate_statistics

dataframe = pd.read_csv('data/house_prices_multivariate.csv')
sale_price = dataframe.loc[:, 'SalePrice']


# Draw the plot for the mean, median and mode for the dataset
def plot():
    mean, median, mode = calculate_statistics()
    ax = sale_price.plot(kind='hist',grid=True, color='c')
    ax.set_xlabel("Sales Price")
    ax.axvline(mean, color='r', label='Mean', linestyle='--', lw='1.9')
    ax.axvline(median, color='g', label='Median', linestyle='--', lw='1.9')
    ax.axvline(mode, color='m', label='Mode', linestyle='--', lw='1.9')
    ax.legend()
    ax.set_title('Histogram of Sale Price with Mean, Median and Mode')
    plt.show()
