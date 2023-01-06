# -*- coding: utf-8 -*-
"""
Created on Thu Jan  5 19:27:06 2023

@author: HP
"""
#python -m pip install Graphviz
import os
import pydotplus #if we need to use any external .exe files.... Here we are using dot.exe

import io #For i/o operations
import pandas as pd
# Sklearn : Scientific kit Learn/ Scikit Learn
from sklearn import tree #For Decissin Tree

#Read Train Data file
titanic_train = pd.read_csv("C://Users//HP//Desktop//BlackBucks//train.csv")
#os.chdir("E:/Data Science/Data/")
os.environ["PATH"] += os.pathsep + 'C:\Program Files (x86)\Graphviz\bin'

titanic_train.shape 
titanic_train.info() 
titanic_train.describe()

#Let's start the journey with non categorical and non missing data columns
X_titanic_train = titanic_train[['Pclass', 'SibSp', 'Parch']] #X-Axis
y_titanic_train = titanic_train['Survived'] #Y-Axis

#Build the decision tree model
dt = tree.DecisionTreeClassifier()
dt.fit(X_titanic_train, y_titanic_train)

#visualize the decission tree
objStringIO = io.StringIO() 
tree.export_graphviz(dt, out_file = objStringIO, feature_names = X_titanic_train.columns)
#Use out_file = objStringIO to getvalues()
file1 = pydotplus.graph_from_dot_data(objStringIO.getvalue())#[0]
#os.chdir("D:\\Data Science\\Data\\")
os.getcwd()
file1.write_pdf("DecisionTree4.pdf")

#Predict the outcome using decision tree
#Read the Test Data
titanic_test = pd.read_csv("C://Users//HP//Desktop//BlackBucks//test.csv")
X_test = titanic_test[['Pclass', 'SibSp', 'Parch']]
#Use .predict method on Test data using the model which we built
titanic_test['Survived'] = dt.predict(X_test)
#To get current working directory) 
os.getcwd()
titanic_test.to_csv("submission_Titanic5.csv", columns=['PassengerId','Survived'], index=False)


