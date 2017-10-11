# Default Imports
import pandas as pd
import matplotlib.pyplot as plt
#from greyatomlib.descriptive_stats.q01_calculate_statistics.build import calculate_statistics
def plot() :
    dataframe = pd.read_csv('data/house_prices_multivariate.csv')
    sale_price = dataframe.loc[:, 'SalePrice']
    #print(sale_price)
    dataframe.hist(column = 'SalePrice')
    mean = sale_price.mean()
    median = sale_price.median()
    mode = sale_price.mode()
    plt.axvline(mean, color = 'g', linestyle = 'dashed', linewidth = 2)
    plt.axvline(median, color = 'r', linestyle = 'dashed', linewidth = 2)
    plt.axvline(mean, color = 'b', linestyle = 'dashed', linewidth = 2)
    plt.show()



# Draw the plot for the mean, median and mode for the dataset
