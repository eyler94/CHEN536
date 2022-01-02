import pandas as pd
import numpy as np

table = pd.read_csv('data.csv')
print(table)

url = 'http://apmonitor.com/pds/index.php/Main/GatherData'
table2 = pd.read_html(url)
print(table2)

table3 = np.genfromtxt('data.csv', delimiter=',')
print(table3)

table4 = np.loadtxt('data.csv', delimiter=',', skiprows=1)
print(table4)

with open('data.csv') as file:
    for line in file:
        print(line)
