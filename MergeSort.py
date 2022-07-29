# Merge Sort 
import matplotlib.pyplot as plt
# data
import pandas as pd
kiwi_list= pd.read_csv('data.csv')
kiwi_weight= kiwi_list['Weight(kg)'].copy()
n_arr = list(kiwi_weight)
# time
import time
starttime = time.time()

#sort data
def m_sort(arr):
    if len(arr) <=1:
       return
    #split data into two grouops
    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]
    m_sort(left)
    m_sort(right)
    #merge two sorted lists
    merged_lists(left, right, arr)
    return arr
   
# combine two pre-sorted lists into one sorted list
def merged_lists(a, b, arr):
    len_a = len(a)
    len_b = len(b)
    i = j = k = 0
# compare data from left and right, add lowest number to new list
    while i < len_a and j< len_b:
        if a[i] <= b[j]:
            arr[k] = a[i]
            i+=1
        else:
            arr[k] = b[j]
            j+=1
        k+=1
    # add any remaining data points to end of list
    while i< len_a:
        arr[k] = a[i]
        i+=1
        k+=1
    while j< len_b:
        arr[k] = b[j]
        j+=1
        k+=1
    
if __name__ == '__main__':
    #graph results - unsorted
    plt.plot(n_arr)
    plt.ylabel("Total Number")
    plt.xlabel("Average Weight")
    plt.title("Weights of kiwi")
    plt.show()
    #sorted data
    m_sort(n_arr)
    plt.plot(n_arr)
    plt.ylabel("Total Number")
    plt.xlabel("Average Weight")
    plt.title("Weights of kiwi")
    plt.show()
    print (n_arr)
    #time calcuation
    executetime = (time.time()- starttime)
    print ("Merge Sort time: " + str(executetime))