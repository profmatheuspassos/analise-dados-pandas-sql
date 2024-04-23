import pandas as pd
import numpy as np

labels = ['a', 'b', 'c']
minha_lista = [10, 20, 30]
arr = np.array([10, 20, 30])
d = {'a':10, 'b':20, 'c':30}

print("labels = ['a', 'b', 'c']")
print("minha_lista = [10, 20, 30]")
print("arr = np.array([10, 20, 30])")
print("d = {'a':10, 'b':20, 'c':30}", "\n")

print("pd.Series(labels)")
print(pd.Series(labels), "\n")

print("pd.Series(data = labels, index = minha_lista)")
print(pd.Series(data = labels, index = minha_lista), "\n")

print("pd.Series(labels, minha_lista)")
print(pd.Series(labels, minha_lista), "\n")

print("pd.Series(d)")
print(pd.Series(d), "\n")

ser1 = pd.Series([1,2,3,4], index = ['EUA', 'Alemanha', 'Rússia', 'Japão'])

print("ser1 = pd.Series([1,2,3,4], index = ['EUA', 'Alemanha', 'Rússia', 'Japão'])")
print(ser1, "\n")

ser2 = pd.Series([1,2,3,4], index = ['EUA', 'Alemanha', 'Italia', 'Japão'])

print("ser2 = pd.Series([1,2,3,4], index = ['EUA', 'Alemanha', 'Italia', 'Japão'])")
print(ser2, "\n")

print("ser1[['Alemanha', 'Rússia']]")
print(ser1[['Alemanha', 'Rússia']], "\n")

print("ser1 + ser2")
print(ser1 + ser2, "\n")