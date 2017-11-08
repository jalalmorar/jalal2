
# coding: utf-8

# # jalal yasser morar folder1

# # array 

# In[4]:


xs = [3, 1, 2,'jalal']    
print(xs, xs[2])  
xs[2] = 'morar'     
print(xs)         
xs.append('bar')  
print(xs)         
print( xs)


# # Dictionaries
# 
# 

# In[5]:


d = {'j': 'jalal', 'y': 'yasser' ,'m': 'morar'}  
print(d['j'])      
print('y' in d) 
d['m'] = 'abu sbaih'     
print(d['m'])      
print(d.get('yanone', 'N/A'))  
print(d.get('m', 'N/A'))    
del d['m']        
print(d.get('m', 'N/A')) 


# # Sets

# In[6]:


animals = {'cat', 'dog'}
print('cat' in animals)   
print('fish' in animals)  
animals.add('fish')       
print('fish' in animals)  
print(len(animals))       
# Number of elements in a set; prints "3"
animals.add('cat')        
print(len(animals))       
animals.remove('cat')     
# Remove an element from a set
print(len(animals))       


# # boxplot

# In[7]:


get_ipython().magic(u'matplotlib inline')

import numpy as np 
import matplotlib as mpl
import matplotlib.pyplot as plt 

np.random.seed(129)
data_1 = np.random.normal(62, 13, 60)
data_2 = np.random.normal(55, 9, 60)

combined_data = [data_1, data_2]

# figure instance
fig = plt.figure(1, figsize=(9, 6))

# axes instance
ax = fig.add_subplot(111)

# draw boxplot
bxp = ax.boxplot(combined_data)


# In[8]:


import numpy as np
import matplotlib.pyplot as plt

# Compute the x and y coordinates for points on a sine curve
x = np.arange(0, 3 * np.pi, 0.1)
y = np.sin(x)

# Plot the points using matplotlib
plt.plot(x, y)
plt.show()  

