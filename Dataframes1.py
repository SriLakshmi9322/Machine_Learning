# -*- coding: utf-8 -*-
"""
Created on Thu Jan  5 19:49:35 2023

@author: HP
"""

import pandas as pd
#============================================================
#pd.__version_
#pd.set_option('display.max_rows', 500))
#pd.set_option('display.max_columnss', 500)
#pd.set_option('display.width', 1000)
#============================================================

pd.__version__
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)


#To check the version
print(pd.__version__)
#Use / or \\
train=pd.read_csv("C://Users//HP//Desktop//BlackBucks//train.csv")
print(type(train))
# print(train)

#Explore the dataframe
train.shape #no. of rows and columns
train.info() #Data type and nullable/non-nullable
train.describe() #Gives statistical information

#Access column/columns of a dataframe
train['Sex']
train['Fare']
train.Sex
train.Fare
temp=train[['Survived','Fare','Embarked']]
print(type(temp))

#Access rows of a dataframe
train.iloc[855:865] #ith record

train[10:20]
train.iloc[10:20]

train[885:891]
train.iloc[885:891]

#Get me top n records
train.head(10)
#Get me bottom n records
train.tail(10)

#Access both rows and columns of a dataframe
train.iloc[10:11]

#If you want to access by column name then use .loc
train.loc[10:20,('Name','Age')]

#conditional access of dataframe 
train.loc[train.Sex == 'male','Sex']
train.loc[train.Sex == 'female','Age']

#Grouping data in Dataframes
train.groupby(['Embarked']).size()
train.groupby(['Pclass','Sex']).size()
train.groupby(['Pclass','Embarked']).mean()

train.groupby(['Embarked','Pclass']).mean()['Fare']









