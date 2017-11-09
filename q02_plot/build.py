# Default Imports
import pandas as pd
import matplotlib.pyplot as plt
from greyatomlib.descriptive_stats.q01_calculate_statistics.build import calculate_statistics

dataframe = pd.read_csv('data/house_prices_multivariate.csv')
sale_price = dataframe.loc[:, 'SalePrice']

def plot():
    means = sale_price.mean()
    median = sale_price.median()
    arr = np.array(sale_price)
    bcount = np.bincount(arr)
    modes = np.argmax(bcount)

    #return means,median,modes
# Draw the plot for the mean, median and mode for the dataset
    plt.hist(sale_price,bins=60)
    plt.show()
    plt.axvline(x=means,ymin=0,ymax=1,color='r')
    plt.axvline(x=medians,ymin=0,ymax=1,color='g')
    plt.axvline(x=modes,ymin=0,ymax=1,color='y')
