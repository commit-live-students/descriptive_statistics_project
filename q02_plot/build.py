# Default Imports
import pandas as pd
import matplotlib.pyplot as plt
from greyatomlib.descriptive_stats.q01_calculate_statistics.build import calculate_statistics

dataframe = pd.read_csv('data/house_prices_multivariate.csv')
sale_price = dataframe.loc[:, 'SalePrice']
def plot():
    graph_mean = plot.sale_price(kind='Histogram')
    return(graph_mean)
print(plot())
plt.show()

# Draw the plot for the mean, median and mode for the dataset
