# Default Imports
import pandas as pd
import matplotlib.pyplot as plt
from greyatomlib.descriptive_stats.q01_calculate_statistics.build import calculate_statistics
import matplotlib

plt.switch_backend('agg')
dataframe = pd.read_csv('data/house_prices_multivariate.csv')
sale_price = dataframe.loc[:, 'SalePrice']


# Draw the plot for the mean, median and mode for the dataset
def plot():
    mean = sale_price.mean()
    median = sale_price.median()

    ar = np.array(sale_price)
    mode1 = np.bincount(ar)
    mode = np.argmax(mode1)

    plt.hist(sale_price)
    plt.axvline(mean,0,1, color='r')
    plt.axvline(median,0,1, color='g')
    plt.axvline(mode,0,1, color='y')
    plt.show()
