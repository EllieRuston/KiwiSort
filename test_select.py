#Select Sort - unit testing

# sorting methods to test
from SelectSort import s_sort #algarithem to test
from random import randint, random
from time import time

averagecase= [randint( 1,10000)for _ in range(1000)]
bestcase=sorted(averagecase)
worstecase=sorted(averagecase, reverse=True)

def test_SelectWorse():
    start=time()
    assert s_sort(worstecase) == bestcase
    print(time()-start)

def test_SelectBest():
    start= time()
    assert s_sort(bestcase) == bestcase
    print (time()-start)

def test_SelectAvg():
    start= time()
    assert s_sort(averagecase) == bestcase
    print(time()-start)