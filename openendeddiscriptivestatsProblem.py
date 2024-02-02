# -*- coding: utf-8 -*-
"""OpenEndedDiscriptiveStats.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1QXwwDe_V3N4gZxTnD3NvAn3BfSd3j8gC
"""

import numpy as np
import pandas as pd
import seaborn as sns

df = pd.read_excel("EmployeeResponse.xlsx")

df.head()

df.shape

df.isnull().sum()

df.isnull().sum().sum()

df.dtypes

df.Response.unique()

sns.barplot(x="Response", y="Response Text", data=df);

sns.lineplot(x="Response", y="Response Text", data=df);

df[['Director', 'Manager', 'Supervisor', 'Staff', 'Response']].groupby('Response').mean()

df[['Director', 'Manager', 'Supervisor', 'Staff', 'Response Text']].groupby('Response Text').mean()

df[['Director', 'Manager', 'Supervisor', 'Staff', 'Response']].groupby('Response').median()

df[['Director', 'Manager', 'Supervisor', 'Staff', 'Response']].groupby('Response').median()

df[['Status', 'Question']].groupby('Question').mean()

sns.lineplot(x='Status', y='Question', data=df)

sns.barplot(x='Status', y='Question', data=df)

sns.barplot(x='Department', y='Response', data=df);

sns.lineplot(x='Department', y='Response', data=df);

df

sns.violinplot(x='Department', y='Response Text', data=df)

