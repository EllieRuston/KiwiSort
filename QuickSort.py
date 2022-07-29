# Quick Sort
#data
import pandas as pd
kiwi_list= pd.read_csv('data.csv')
# time
import time
starttime = time.time()

#swap
def swap(a, b, arr):
    if a!=b:
        tmp = arr[a]
        arr[a] = arr[b]
        arr[b] = tmp

def partition(elements, start, end):
    pivot_index = start
    pivot = elements[pivot_index]
    
    while start < end:
        while start < len(elements) and elements[start] <= pivot:
            start += 1

        while elements[end] > pivot:
            end -=1
        #will only swap when start is less then end    
        if start <= end:
            swap(start, end, elements)

    swap(pivot_index, end, elements)
    return end

def q_sort(elements, start, end):
    #itterations
    if start < end:
        pi = partition(elements, start, end) 
        q_sort(elements, start, pi -1) #left partition
        q_sort(elements, pi +1, end) #right partition

if __name__=='__main__':
    # new data
    kiwi_weight= kiwi_list['Weight(kg)'].copy()
    elements = list(kiwi_weight)
    #show sorted results
    q_sort(elements, 0, len(elements)-1)
    print(f'sorted array: {elements}')
        
    executetime = (time.time()- starttime)
    print ("Pivot Sort time: " + str(executetime))
