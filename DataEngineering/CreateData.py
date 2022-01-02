import numpy as np
import pandas as pd

time = np.linspace(0,1,8)
x = np.cos(time)

data = pd.DataFrame({"Time":time, 'x': x})

data.to_csv('data.csv',index=False)
print(data)
