# Default Imports
import pandas as pd
import matplotlib.pyplot as plt
from greyatomlib.descriptive_stats.q01_calculate_statistics.build import calculate_statistics

plt.switch_backend('agg')
dataframe = pd.read_csv('data/house_prices_multivariate.csv')
sale_price = dataframe.loc[:, 'SalePrice']

def plot():
    mean=np.mean(sale_price)
    median=np.median(sale_price)
    mode1=sale_price.mode()
    mode=mode1[0]
    plt.axvline(mean,color='R',linestyle='dashed',linewidth=2)
    plt.axvline(median,color='B',linestyle='dashed',linewidth=2)
    plt.axvline(mode,color='Y',linestyle='dashed',linewidth=2)
    plt.show()

# Draw the plot for the mean, median and mode for the dataset
