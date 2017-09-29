# Task 4:

## Spearman Correlation Coeffecient

**Now what is Spearman Correlation Coefficient?**

Pearson Correlation measures the strength of the linear relationship between normally distributed variables.

However, it is not always possible to have a linear relationship between the variables in a dataset.

There might come a situation where the variables will not be related linearly, in such situations we use Spearman Correlation Coeffecient. Say, the variables might not be normally distributed or the relationship between the variables might not be linear


**Spearman Correlation Coeffecient can be calculated as follows :**

* Find the ranks for each individual row in a column. The values can be ranked as per any criteria.
For simplicity, we can rank them in a increasing order of values.

* Add a column 'd', which would store the difference between the row values for the 2 columns selected above.

* Add another column 'd-squared', which would contain the values for squares for each element in the 'd' column.

* Sum up all the values in the 'd-squared' column.

* Substitute these values in the Spearman's Rank Correlation formula.


For these you don't need to load the data, we have already done it for you.

You must calculate the Spearman Correlation Coeffecient between the SalePrice column for the loaded datasets.
#### Parameters:

None 

The required data has already been loaded for you.

#### Returns:

| Return | dtype | description |
| --- | --- | --- | 
| Spearman Correlation Coeffecient| Float | Spearman Correlation Coeffecient between SalePrice column of the loaded datasets|
