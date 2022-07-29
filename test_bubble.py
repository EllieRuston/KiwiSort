# Unit Test
import pytest
# sorting methods to test
from BubbleSort import b_sort #algarithem to test
#data pints - Kiwi
#import pandas as pd
#kiwi_list= pd.read_csv('data.csv')
#kiwi_weight= kiwi_list['Weight(kg)'].copy()
#roandom
from random import randint, random
from time import time

averagecase= [randint( 1,10000)for _ in range(1000)]
#averagecase = kiwi_weight
bestcase=sorted(averagecase)
worstecase=sorted(averagecase, reverse=True)

def test_BubbleWorse():
    start=time()
    assert b_sort(worstecase) == bestcase
    print(time()-start)

def test_BubbleBest():
    start= time()
    assert b_sort(bestcase) == bestcase
    print (time()-start)

def test_BubbleAvg():
    start= time()
    assert b_sort(averagecase) == bestcase
    print(time()-start)