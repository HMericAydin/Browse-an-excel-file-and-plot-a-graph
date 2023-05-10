#!/usr/bin/env python
# coding: utf-8

# In[56]:


from tkinter.filedialog import askopenfilename
import pandas as pd
import numpy as np
from array import array

## Choose your file

filename = askopenfilename()
df = pd.read_excel(filename, usecols='A:D') # Describe the column length according to your data

## Make a matrix by using the values from selecting file

value_matrix = df.to_numpy() # Collect the data to matrix
C_col_values = [] # An empty array to collect C column data
filter_arr = [] # An empty array to collect filtered C column data

## Collect the values to arrays

for i in range(len(value_matrix)):
    C_col_values.append(value_matrix[i][2])

## Filtering

C_col_values = np.array(C_col_values) # Convert the values from list to array
for element in C_col_values:
    if (element<=400):
        filter_arr.append(True)
    else:
        filter_arr.append(False)
filter_value = C_col_values[filter_arr] # Filter the values

## Plotting

import matplotlib.pyplot as plt

plt.plot(filter_value)
# naming the x axis
plt.xlabel('The Numbers of Values')
# naming the y axis
plt.ylabel('Force - N')
  
# giving a title to my graph
plt.title('The Forces Below the 400 N Forces')
plt.show()

