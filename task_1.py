# -*- coding: utf-8 -*-
"""Task 1

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1zV77E9EEBiyq6Nk2rftjO8oafOBrUgfF
"""

import pandas as pd
import matplotlib
import numpy as np
import seaborn as sns
from matplotlib import pyplot as plt

task1 = pd.read_csv('Titanic-Dataset.csv')

task1.head()

task1.shape

task1.tail()

task1['Age']

task1['Survived'].value_counts().keys()

plt.figure(figsize=(5,5))
plt.bar(list(task1['Survived'].value_counts().keys()),list(task1['Survived'].value_counts()),color=["b","y"])
plt.show()

task1['Pclass'].value_counts()

plt.figure(figsize=(5,5))
plt.bar(list(task1['Pclass'].value_counts().keys()),list(task1['Pclass'].value_counts()),color=["red","green","orange"])
plt.show()

task1['Sex'].value_counts()

plt.figure(figsize=(5,5))
plt.bar(list(task1['Sex'].value_counts().keys()),list(task1['Sex'].value_counts()),color=["green","blue"])
plt.show()

sns.countplot(x=task1['Sex'],hue=task1['Survived'])

sns.countplot(x=task1['Survived'],hue=task1['Pclass'])

task1.isna().sum()

task1.replace({'Sex':{'male':0,'female':1}},inplace=True)
task1.head()

x=task1[['Pclass','Sex']]
y=task1['Survived']

x,y

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=0)

print(x.shape,x_train.shape,x_test.shape)

print(y.shape,y_train.shape,y_test.shape)

from sklearn.linear_model import LogisticRegression
ML=LogisticRegression()
ML.fit(x_train,y_train)

x_test_prediction=ML.predict(x_test)
print(x_test_prediction)

print(y_test)

x_train_prediction=ML.predict(x_train)
print(x_train_prediction)

print(y_train)

from sklearn.metrics import accuracy_score
train_accuracy=accuracy_score(x_train_prediction,y_train)
test_accuracy=accuracy_score(x_test_prediction,y_test)
print("Accuracy scores of training and test data are ",train_accuracy,"and",test_accuracy,"respectively")