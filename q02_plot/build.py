# Default Imports
import pandas as pd
import matplotlib.pyplot as plt
from greyatomlib.descriptive_stats.q01_calculate_statistics.build import calculate_statistics

dataframe = pd.read_csv('data/house_prices_multivariate.csv')
sale_price = dataframe.loc[:, 'SalePrice']
def plot():
    mean_plot=sale_price.plot(kind=Histogram)
    median_plot=sale_price.plot(kind=Histogram)
    mode_plot=sale_price.plot(kind=Histogram)
    return(mean_plot, median_plot, mode_plot)
print(plot())
