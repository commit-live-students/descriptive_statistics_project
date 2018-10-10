# %load q02_plot/build.py
# Default Imports
import pandas as pd
import matplotlib.pyplot as plt
from greyatomlib.descriptive_stats.q01_calculate_statistics.build import calculate_statistics

plt.switch_backend('agg')
dataframe = pd.read_csv('data/house_prices_multivariate.csv')
sale_price = dataframe.loc[:, 'SalePrice']

# Draw the plot for the mean, median and mode for the dataset
def plot():
    plt.hist(sale_price)
    #plotting the mean, median and mode
    plt.axvline(x = np.mean(sale_price),c='#00FF00',label='mean')
    plt.axvline(x = np.median(sale_price),c='#FFA500',label='median')
    plt.axvline(x = np.array(sale_price.mode()).item(),c='#EE82EE',label='mode')

    #defining x and y label
    plt.xlabel('SalePrice')
    plt.ylabel('Frequency')

    plt.legend()
    
plt.show()





