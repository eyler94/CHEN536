import numpy as np
import pandas as pd

time = np.linspace(0,1,4)
x = np.cos(time)
dataX = pd.DataFrame({"Time":time, 'x': x})

time = np.linspace(0,1,3)
y = np.cos(time)
dataY = pd.DataFrame({"Time":time, 'y': y})

print(dataX)
print(dataY)

dataX.set_index('Time')
dataY.set_index('Time')

dataX = dataX.append(dataY)
dataX = dataX.sort_values(by='Time')
dataX = dataX.drop_duplicates(subset='Time')
dataX = dataX.reset_index(drop=True)


print(dataX)
