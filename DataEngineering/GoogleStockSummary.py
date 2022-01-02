# Calculate summary statistics such as the mean, median,
# standard deviation, and quartile information.
# Create two new data columns for Volatility=High-Low and
# Change=Close-Open.

import pandas as pd

###Collect the data
tableUrlSource = 'http://apmonitor.com/pds/uploads/Main/goog.txt'
table = pd.read_csv(tableUrlSource)

###Calculate new data
##Volatility
volatility = table['High'] - table['Low']
##Change
change = table['Close'] - table['Open']
##Add the new data
locationToInsert = 5
table.insert(locationToInsert, "Volatility", volatility)
table.insert(locationToInsert, "Change", change)

print(table.describe())

# ###Present the data
# startColumn=1
# endColumn=2
# for columnLocation, columnName in zip(range(startColumn,(table.shape[1]-endColumn)),table.iloc[:,startColumn:-endColumn]):
#     print(columnName)
#     column = table.iloc[:,columnLocation]
#     print(f"25%: {column.quantile(q=0.25)}")
#     print(f"median: {column.median()}")
#     print(f"mean: {column.mean()}")
#     print(f"75%: {column.quantile(q=0.75)}")
#     print(f"standard deviation: {column.std()}\n")
