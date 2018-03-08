# Default Imports
import pandas as pd
import matplotlib.pyplot as plt
from greyatomlib.descriptive_stats.q01_calculate_statistics.build import calculate_statistics
import numpy

dataframe = pd.read_csv('data/house_prices_multivariate.csv')
sale_price = dataframe.loc[:, 'SalePrice']

import numpy

def plot():
    mean = numpy.mean(sale_price)
    median = numpy.median(sale_price)
    mode = sale_price.mode()


    plt.hist(sale_price , color= 'y')


    values = [mean , median , mode[0]]

    for e in values:

        plt.axvline(x = e)

    plt.show()

plot()




# Draw the plot for the mean, median and mode for the dataset
