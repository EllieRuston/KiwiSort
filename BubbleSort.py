# Bubble Sort
#time to sort
import time
starttime = time.time()
#data
import pandas as pd
kiwi_list= pd.read_csv('data.csv')
kiwi_weight= kiwi_list['Weight(kg)'].copy()
n_arr = list(kiwi_weight)

def b_sort (n_data):
    
    
    # calculate itterations
    for i in range(len(n_data)-1,0,-1):
     
     #swapping 
        for j in range(i):
            if n_data[j]>n_data[j+1]:
                temp = n_data[j]
                
                n_data[j] = n_data [j+1]
                n_data [j+1] = temp
                
    return n_data
    
#show sorted results
b_sort(n_arr)
print (n_arr)

executetime = (time.time()- starttime)
print ("Bubble Sort time: " + str(executetime))




