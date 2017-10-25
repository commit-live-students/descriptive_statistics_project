# Default Imports
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from greyatomlib.descriptive_stats.q01_calculate_statistics.build import calculate_statistics

dataframe = pd.read_csv('data/house_prices_multivariate.csv')
sale_price = dataframe.loc[:, 'SalePrice']

plt.axvline(x=sale_price.mean(), color='k', linestyle='--')
plt.axvline(x=sale_price.median(), color='k', linestyle='--')
plt.axvline(x=sale_price.mode(), color='k', linestyle='--')
plt.show()
