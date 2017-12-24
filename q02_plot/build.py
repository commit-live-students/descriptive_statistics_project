# Default Imports
import pandas as pd
# import matplotlib.pyplot as plt
from greyatomlib.descriptive_stats.q01_calculate_statistics.build import calculate_statistics

dataframe = pd.read_csv('data/house_prices_multivariate.csv')
sale_price = dataframe.loc[:, 'SalePrice']


# Draw the plot for the mean, median and mode for the dataset
import matplotlib
matplotlib.use('tkAgg')
import matplotlib.pyplot as plt

def plot():
    sale_price.plot(kind='hist')
    plt.axvline(sale_price.mean(), color='red')
    plt.axvline(sale_price.median(), color='blue')
    plt.axvline(sale_price.mode()[0], color='yellow')
    plt.show()
    return None
