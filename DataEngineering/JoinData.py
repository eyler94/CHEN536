import numpy as np
import pandas as pd

time = np.linspace(0,1,4)
x = np.cos(time)
dataX = pd.DataFrame({"Time":time, 'x': x})

time = np.linspace(0,1,3)
y = np.sin(time)
dataY = pd.DataFrame({"Time":time, 'y': y})

print(dataX)
print(dataY)

dataX = dataX.set_index('Time')
dataY = dataY.set_index('Time')

megaX = dataX.join(dataY)
print(megaX)

megaY = dataX.join(dataY, how='right')
print(megaY)

megaY = dataX.join(dataY, how='right')
print(megaY)

megaUnion = dataX.join(dataY, how='inner')
print(megaUnion)

megaTotal = dataX.join(dataY, how='outer', sort=True)
print(megaTotal)

# data.to_csv('data.csv',index=False)
