
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
df = pd.read_csv('diabetes.csv')
df.head()



# In[2]:


columns = ['Pregnancies' , 'Glucose' , 'BloodPressure' ,'SkinThickness' , 'Insulin' , 'BMI' , 'DiabetesPedigreeFunction' , 'Age']
labels = df['Outcome'].values
features = df[list(columns)].values

         


# In[7]:


from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
x_train, x_test ,y_train ,y_test = train_test_split(features ,labels , test_size = 0.30)
clf = RandomForestClassifier(n_estimators=1)
clf = clf.fit(x_train, y_train)



# In[8]:


accuracy =clf.score(x_train, y_train)
print accuracy * 100


