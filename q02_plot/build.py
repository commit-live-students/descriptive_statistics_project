# Default Imports
import sys, os
sys.path.append(os.path.join(os.path.dirname(os.curdir),  '..'))
import pandas as pd
import matplotlib.pyplot as plt
from q01_calculate_statistics.build import calculate_statistics

dataframe = pd.read_csv('data/house_prices_multivariate.csv')
sale_price = dataframe.loc[:, 'SalePrice']

# Draw the plot for the mean, median and mode for the dataset
# Default Imports
import pandas as pd
import matplotlib.pyplot as plt
from q01_calculate_statistics.build import calculate_statistics

dataframe = pd.read_csv('data/house_prices_multivariate.csv')
sale_price = dataframe.loc[:, 'SalePrice']

# Draw the plot for the mean, median and mode for the dataset
def plot():
        '''Enter your code here'''
        mean, median, mode = calculate_statistics()
        result = plt.hist(sale_price, color='c')
        plt.axvline(mean, color='b', linestyle='dashed', linewidth=2)
        plt.axvline(median, color='b', linestyle='dashed', linewidth=2)
        plt.axvline(pd.Series(mode).values, color='b', linestyle='dashed', linewidth=2)
        return plt
