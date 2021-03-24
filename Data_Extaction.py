# -*- coding: utf-8 -*-
"""
Created on Sun Mar 21 14:12:52 2021

@author: Anagha
"""

from Plot_AQI import avg_data_year
import requests
import sys
import pandas as pd
from bs4 import BeautifulSoup
import os
import csv

#Function for cleaning and returning recors from perticular month from html file
def met_data(month,year):
    finalD=[] #all records of perticular month
    #Opening and reading html file
    file_html=open(r"C:\Users\Anagha\Desktop\ML_model\Air Quality Index\Data\Html_Data\{}\{}.html".format(year,month), 'rb')
    plain_text=file_html.read()
    soup = BeautifulSoup(plain_text, "lxml")
    #this for loop is used to iterate through all the table bodies and through
    #table rows and table headers to get each and every value
    for tbody in soup.findAll('table', {'class': 'medias mensuales numspan'}):
        for tr in tbody:
            tempD = [] # this variable contains one perticular record of a month
            for th in tr:
                a = th.get_text()
                tempD.append(a)
            finalD.append(tempD)
   # we have to remove last 2 records are als0 first record as they are of no use
    finalD.pop(len(finalD) - 1)
    finalD.pop(len(finalD) - 1)
    finalD.pop(0)
    # similar to doing finalD = finalD[1:-2]
    # in each rows there are some columns which are empty and hence they should be removed
    for a in range(len(finalD)):
        # removing empty fields and keeping only usefull data 
        finalD[a] = finalD[a][1:6] + finalD[a][7:10]

    return finalD
#function to combine all csv files
def data_combine(years,cs):
    for a in pd.read_csv(r'C:\Users\Anagha\Desktop\ML_model\Air Quality Index\Data\Real_Data\real_'+str(year)+'.csv', chunksize=cs):
        df=pd.DataFrame(data=a)
        mylist=df.values.tolist()
    return mylist

if __name__=='__main__':
    col_names=['T', 'TM', 'Tm', 'SLP', 'H', 'VV', 'V', 'VM', 'PM2.5']
#creating Real-Data folder if it is not present
    if not os.path.exists(r"C:\Users\Anagha\Desktop\ML_model\Air Quality Index\Data\Real_Data"):
        os.mkdir(r"C:\Users\Anagha\Desktop\ML_model\Air Quality Index\Data\Real_Data")
        
    for year in range(2013,2019):
        final_data=[] # contains all records of a year
        #creating csv file for each year
        with open(r"C:\Users\Anagha\Desktop\ML_model\Air Quality Index\Data\Real_Data"+ str(year) + '.csv', 'w') as csvfile:
            wr = csv.writer(csvfile, dialect='excel')
            wr.writerow(col_names)
        for month in range(1, 13):
            temp = met_data(month, year)
            final_data = final_data + temp
     # this is our response variable
        pm = avg_data_year(year)
        
        print('year = {} , pm = {} , final_data= {}'.format(year,len(pm),len(final_data)))
        if(len(pm)<len(final_data)):
            total_len=len(pm)
        else:
            total_len=len(final_data)
            
            
        for i in range(total_len):
            final_data[i].insert(8, pm[i])

        with open(r'C:\Users\Anagha\Desktop\ML_model\Air Quality Index\Data\Real_Data\real_' + str(year) + '.csv', 'a') as csvfile:
            wr = csv.writer(csvfile, dialect='excel')
            for row in final_data:
                flag = 0
                for elem in row:
                    if elem == " " or elem == "-":
                        flag = 1
                        break
                    if flag != 1:
                        wr.writerow(row)
                   
    data_2013 = data_combine(2013, 600)
    data_2014 = data_combine(2014, 600)
    data_2015 = data_combine(2015, 600)
    data_2016 = data_combine(2016, 600)
    data_2017 = data_combine(2017, 600)
    data_2018 = data_combine(2018, 600)
     
    total=data_2013+data_2014+data_2015+data_2016+data_2017+data_2018
    
    with open(r'C:\Users\Anagha\Desktop\ML_model\Air Quality Index\Data\Real_Data\Real_Combine.csv', 'w') as csvfile:
        wr = csv.writer(csvfile, dialect='excel')
        wr.writerow(col_names)
        wr.writerows(total)
        
        
df=pd.read_csv(r'C:\Users\Anagha\Desktop\ML_model\Air Quality Index\Data\Real_Data\Real_Combine.csv')
             
        
        
        



    
