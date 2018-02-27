# -*- coding: utf-8 -*-
"""
Created on Thu Aug  3 23:14:40 2017

@author: Darshil
"""


import requests
import os
import zipfile
import openpyxl
import sqlite3
import glob
import getpass
import requests
import csv
import string
import pandas as pd
import numpy as np
import shutil

#Getting the training data from URL
url="http://kevincrook.com/utd/market_basket_training.txt"
r1=requests.get(url)

#Storing the data into Temporary txt file
training_file=open("market_basket_training.txt","wb")
training_file.write(r1.content)
training_file.close()
training_df=pd.read_csv("market_basket_training.txt",header=None,index_col =0, names=[None,1,2,3,4])

#Getting the testing data from URL
url="http://kevincrook.com/utd/market_basket_test.txt"
r2=requests.get(url)

#Storing the data into Temporary txt file
testing_file=open("market_basket_test.txt","wb")
testing_file.write(r2.content)
testing_file.close()
testing_df=pd.read_csv("market_basket_test.txt",header=None,index_col =0, names=[None,1,2,3,4])

#Removing the temporary txt files
os.remove('market_basket_training.txt')
os.remove('market_basket_test.txt')

#Logic for seperating group of 2,3,4 products and putting them into different dataframes
training_df_2=[None]*500000
training_df_3=[None]*500000
training_df_4=[None]*500000

count_2=1
count_3=1
count_4=1
for i in list(training_df.index):
    #print(i)
    x=list(training_df.loc[i,:])
    cleanedList = [y for y in x if str(y) != 'nan']
    length=len(cleanedList)
    if length==2:
        training_df_2[count_2]=i
        count_2+=1
    elif length==3:
        training_df_3[count_3]=i
        count_3=count_3+1
    elif length==4:
        training_df_4[count_4]=i
        count_4=count_4+1 



#Extracting data from main training dataframe
training_df_2_new=training_df.loc[training_df_2]
training_df_3_new=training_df.loc[training_df_3]
training_df_4_new=training_df.loc[training_df_4]

#Dropping Unnecessory columns
training_df_2_new = training_df_2_new.loc[:,[1,2]]
training_df_3_new = training_df_3_new.loc[:,[1,2,3]]


#Doing group by to get total number of 2,3,4 size data values
total_count_2=training_df_2_new.groupby([1,2]).size()
total_count_3=training_df_3_new.groupby([1,2,3]).size()
total_count_4=training_df_4_new.groupby([1,2,3,4]).size()


#total_count_2=pd.Series.to_frame(total_count_2)
#total_count_3=pd.Series.to_frame(total_count_3)
#total_count_4=pd.Series.to_frame(total_count_4)

#Coversting index into columns 
total_count_2.reset_index(inplace=True)
total_count_3.reset_index(inplace=True)
total_count_4.reset_index(inplace=True)

#Generating empty recommendation data frame
d2={1:np.nan}
index2=np.arange(1,101,1);
recomm_df= pd.DataFrame(d2,index2);

#Removing values of 'P04' and 'P08'
testing_df=testing_df.replace('P04', np.NaN)
testing_df=testing_df.replace('P08', np.NaN)

#Logic for finding out best product to be recommendated 
for i in list(testing_df.index):
    max_count=0
    x=list(testing_df.loc[i,:])
    #Clearing Nan values 
    cleanedList = [y for y in x if str(y) != 'nan']
    length=len(cleanedList)
    if length==1:
        for j in list(total_count_2.index):
            if set(cleanedList)<set(total_count_2.loc[j,:]):
                if (total_count_2.loc[j,0]>max_count):
                    max_count=total_count_2.loc[j,0]
                    recomm_df.loc[i]=list(set(total_count_2.loc[j,[1,2]])-set(cleanedList))
    elif length==2:
        for j in list(total_count_3.index):
            if set(cleanedList)<set(total_count_3.loc[j,:]):
                if (total_count_3.loc[j,0]>max_count):
                    max_count=total_count_3.loc[j,0]
                    recomm_df.loc[i]=list(set(total_count_3.loc[j,[1,2,3]])-set(cleanedList))
    elif length==3:
        for j in list(total_count_4.index):
            if set(cleanedList)<set(total_count_4.loc[j,:]):
                if (total_count_4.loc[j,0]>max_count):
                    max_count=total_count_4.loc[j,0]
                    recomm_df.loc[i]=list(set(total_count_4.loc[j,[1,2,3,4]])-set(cleanedList))
#Reindexing
new_index=[None]*101
for i in list(range(1,101)):
    new_index[i]=str(i).zfill(3)

new_index=new_index[1:]
recomm_df.index=new_index
# Writing final output into (Comma seperated)Text file
recomm_df.to_csv('market_basket_recommendations.txt',sep=',',encoding='utf-8',header=False)
