# -*- coding: utf-8 -*-
"""titanic_prediction.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1No71oMRGhPxh_CD6GWcGRGIhlhijRz49

# Titanic Survival Prediction Model
"""

# Import Dependencies

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score



""" Data Filtering"""

# Load Data
titanic_data = pd.read_csv('/content/Data/train.csv')

# Load the Head for reference
titanic_data.head()

# Load the shape of the dataframe
titanic_data.shape

# Check the number of missing values in each column
titanic_data.isnull().sum()

# Handle the missing data in Cabin / Age
# Since Cabin column is missing for majority of the data, therefore I drop it
titanic_data = titanic_data.drop(columns='Cabin', axis=1)

# Then replace all the missing age value with mean value for age
titanic_age_mean = titanic_data['Age'].mean()
titanic_data['Age'].fillna(titanic_age_mean, inplace = True)

# Lastly fill the Embark with the most commonly appeared value, aka mode
titanic_embark_mode = titanic_data['Embarked'].mode()
titanic_data['Embarked'].fillna(titanic_embark_mode[0], inplace = True)

# Check Again for null
# titanic_data.isnull().sum()

"""Data Analysis"""

titanic_data.describe()

# Find the number that survived
titanic_data['Survived'].value_counts()

sns.set()

# Count plot for 'Survived' column
sns.countplot(x = 'Survived', data = titanic_data)

# Count plot for 'Set' column
sns.countplot(x = 'Survived', data = titanic_data)

# Number of Survivor Gender wise
sns.countplot(x='Sex', hue='Survived',data=titanic_data)

# Count graph for Pclass
sns.countplot(x='Pclass',data=titanic_data)

# Number of Survivor via class
sns.countplot(x='Pclass', hue='Survived', data=titanic_data)

"""Converting Data Type for Model to use"""

#  Replace male and female with numerical value and then replace Embarked with numerical value

# Converting categorical to numerical
titanic_data['Sex'] = titanic_data['Sex'].replace({'male':0, 'female':1})
titanic_data['Embarked'] = titanic_data['Embarked'].replace({'S':0, 'C':1, 'Q':2})

# Drop the name, passengerId and Ticket columns since they are not important
x = titanic_data.drop(columns=['PassengerId','Name','Ticket','Survived'], axis=1)
y = titanic_data['Survived']



"""Split dataset into Train and test data"""

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

"""Apply Logistic Regression"""

model = LogisticRegression()

# train logistic regression model using training data
model.fit(x_train, y_train)

"""Evaluate"""

# accuracy on training data

x_train_accuracy = model.predict(x_train)
# print(x_train_accuracy)
training_data_accuracy = accuracy_score(y_train, x_train_accuracy)
print("training data accuracy: ", training_data_accuracy)

# accuracy on test data

x_test_accuracy = model.predict(x_test)
# print(x_train_accuracy)
test_data_accuracy = accuracy_score(y_test, x_test_accuracy)
print("test data accuracy: ", test_data_accuracy)

