# %load q02_plot/build.py
# Default Imports
import pandas as pd
import matplotlib.pyplot as plt
from greyatomlib.descriptive_stats.q01_calculate_statistics.build import calculate_statistics
from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from pandas import Series, DataFrame
import matplotlib.pyplot as plt

dataframe = pd.read_csv('data/house_prices_multivariate.csv')
sale_price = dataframe.loc[:, 'SalePrice']
def plot():

    plt.hist(sale_price)
    plt.axvline(sale_price.mean(),color='pink')
    plt.axvline(sale_price.median(), linestyle='dashed', color='y')
    plt.axvline(int(sale_price.mode()),color='r')
    plt.show()
