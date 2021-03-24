# -*- coding: utf-8 -*-
"""
Created on Sun Mar 21 19:46:37 2021

@author: Anagha
"""
import  pandas as pd
import matplotlib.pyplot as plt

#Function for creating response variable (PM2.5)
def avg_data_year(year=2013):
    avg_365_days = [] #list which contains average PM2.5 of 365 days
    invalid_strings = ['NoData','PwrFail','---','InVld']
    csv_file_path = 'Data/AQI/aqi{}.csv'.format(year)
    for rows in pd.read_csv(csv_file_path,chunksize = 24):
        hour_sum = 0 #sum of 24 hours values
        day_avg = 0 #1 day's average value i.e., sum/24
        data = [] #list which contains 24 hours values
        df = pd.DataFrame(data = rows)
        
        for index,row in df.iterrows():
            data.append(row["PM2.5"])
        
        for i in data:
            if(type(i) is int or type(i) is float):
                hour_sum +=1
            elif(type(i) is str):
                if i not in invalid_strings:
                    hour_sum += float(i)
        day_avg=hour_sum/24
        avg_365_days.append(day_avg)
    return avg_365_days

if __name__=="__main__":
    lst_year = []
    for i in range(2013,2019):
        lst_year.append(avg_data_year(i))
    #for visualizing some of the results
    year_lab = 2013
    for i in range(3):
        plt.plot(range(len(lst_year[i])),lst_year[i],label="{} data".format(year_lab))
        year_lab += 1
    plt.xlabel('Day')
    plt.ylabel('PM 2.5')
    plt.legend(loc='upper right')
    plt.show()


    