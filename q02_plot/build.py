# Default Imports
import pandas as pd
import matplotlib.pyplot as plt
from greyatomlib.descriptive_stats.q01_calculate_statistics.build import calculate_statistics

dataframe = pd.read_csv('data/house_prices_multivariate.csv')
sale_price = dataframe.loc[:, 'SalePrice']


# Draw the plot for the mean, median and mode for the dataset
def plot():
    a = calculate_statistics()
    Mean = a[0]
    Median = a[1]
    Mode = a[2]
    result = plt.hist(sale_price,color = 'y')
    #plt.axvline(sale_price.mean(), color='red', linestyle='dashed', linewidth=2)
    #plt.axvline(sale_price.median(), color='g', linestyle='dashed', linewidth=2)
    plt.axvline(Mean, color='r', linestyle='dashed', linewidth=2)
    plt.axvline(Median, color='g', linestyle='dashed', linewidth=2)
    plt.axvline(Mode, color='b', linestyle='dashed', linewidth=2)
    plt.show()



#print plot()
