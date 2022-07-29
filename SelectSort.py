#Select Sort
import pandas as pd
kiwi_list= pd.read_csv('data.csv')
#time to sort
import time
starttime = time.time()

def s_sort(n_data):
    #find min value 
    for n in range(len(n_data)-1):
        minpos = n
        for s in range(n,(len(n_data))):
            if n_data [s]< n_data[minpos]:
                minpos = s
        #Swap
        temp = n_data[n]
        n_data[n] = n_data[minpos]
        n_data[minpos] = temp

    return(n_data)
#data
kiwi_weight= kiwi_list['Weight(kg)'].copy()
n_data = list(kiwi_weight)

s_sort(n_data)
#show sorted results
print(n_data)

#time    
executetime = (time.time()- starttime)
print ("Select Sort time elapsed: " + str(executetime))    