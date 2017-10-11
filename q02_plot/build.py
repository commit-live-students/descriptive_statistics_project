# Default Imports
import pandas as pd
import matplotlib.pyplot as plt
from greyatomlib.descriptive_stats.q01_calculate_statistics.build import calculate_statistics

dataframe = pd.read_csv('data/house_prices_multivariate.csv')
sale_price = dataframe.loc[:, 'SalePrice']


# Draw the plot for the mean, median and mode for the dataset
def plot():
    mean_sale, median_sale, mode_sale = calculate_statistics()
    #sales = [mean_sale, median_sale, mode_sale]
    plt.hist(sale_price, color="b")
    #plt.axvline((mean_sale, median_sale, mode_sale), color='r', linestyle='dashed', linewidth=2)
    plt.axvline(mean_sale, color='g', linestyle='dashed', linewidth=2)
    plt.axvline(median_sale, color='r', linestyle='dashed', linewidth=2)
    plt.axvline(mode_sale[0], color='c', linestyle='dashed', linewidth=2)
    #plt.axvline(sales[0], sales[1],sales[2])
    plt.show()
