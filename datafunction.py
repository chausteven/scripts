#!/usr/bin/env python
# coding: utf-8

# In[225]:


#Import necessary modules
import pandas as pd
import matplotlib.pyplot as plt

filename = str(input('What .csv file would you like to analyze?'))
#Asks what csv file you would like to analyze and takes the csv file and reads it, and asks the user for inputs for what they want to find and for what category.
data = pd.read_csv(filename) 
stat = str(input('What statistic do you want to find from the data? (i.e. Max, Min, Avg, Std) '))
assert stat.upper() == 'MAX' or stat.upper() == 'MIN' or stat.upper() == 'AVG' or stat.upper() == 'STD', 'Please choose one of the example statistical analysis'
key = str(input('What do you want to find the {} of? (i.e Slow approach, Vigilance, Foraging)'.format(stat)))
assert key == 'Foraging' or key == 'Vigilance' or key == 'Slow approach', "Please choose from one of the catagories shown above"
#Seperates the data based on treatment type
catdata = data.loc[data['TREATMENT'] == 'Cat']
controldata = data.loc[data['TREATMENT'] == 'Control']
#If statements to check what statistic the user wants to find out
#Prints out the the behavior score depending on the statistics and rounds it to 3 sigfig
#Plots behavior score for each subject based on their treatment type
if stat.upper() == 'MAX': #Max function
    print('This is the maximum behavior score for bettongs exposed to cats:',round(catdata[key].max(), 3))
    print('This is the maximum behavior score for bettongs not exposed to cats:',round(controldata[key].max(), 3))
    plt.scatter(range(len(catdata)),catdata[key], label='Cat Exposed')
    plt.scatter(range(len(controldata)),controldata[key], label='Control')
    plt.legend(loc='upper right') #Creates a legend on the top right with two labels, 'Cat Exposed' and 'Control'
    plt.ylabel('Behavior Score') #Label the axis of the graph 
    plt.xlabel('Subject #')
elif stat.upper() == 'MIN': #Min function
    print('This is the minimum behavior score for bettongs exposed to cats:',round(catdata[key].min(), 3))
    print('This is the minimum behavior score for bettongs not exposed to cats:',round(controldata[key].min(), 3))
    plt.scatter(range(len(catdata)),catdata[key], label='Cat Exposed')
    plt.scatter(range(len(controldata)),controldata[key], label='Control')
    plt.legend(loc='upper right')
    plt.ylabel('Behavior Score')
    plt.xlabel('Subject #')
elif stat.upper() == 'AVG': #Average function
    print('This is the average behavior score for bettongs exposed to cats:',round(catdata[key].mean(), 3))
    print('This is the average behavior score for bettongs not exposed to cats:',round(controldata[key].mean(), 3))
    plt.scatter(range(len(catdata)),catdata[key], label='Cat Exposed')
    plt.scatter(range(len(controldata)),controldata[key], label='Control')
    plt.legend(loc='upper right')
    plt.ylabel('Behavior Score')
    plt.xlabel('Subject #')
elif stat.upper() == 'STD': #Standard deviation function
    print('This is the standard deviation for behavior score for bettongs exposed to cats:', round(catdata[key].std(), 3))
    print('This is the standard deviation for behavior scores for bettongs not exposed to cats:',round(controldata[key].std(), 3))
    plt.scatter(range(len(catdata)),catdata[key], label='Cat Exposed')
    plt.scatter(range(len(controldata)),controldata[key], label='Control')
    plt.legend(loc='upper right')
    plt.ylabel('Behavior Score')
    plt.xlabel('Subject #')


# In[ ]:




