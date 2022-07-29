# Merge Test
# sorting methods to test
from MergeSort import * #code to test
#tests to run
from random import randint, random
from time import time

averagecase= [randint(1, 1000) for _ in range(1000)]
bestcase=sorted(averagecase)
worstecase=sorted(averagecase, reverse=True)

def test_MergeWorse():
    start=time()
    assert m_sort(worstecase) == bestcase
    print(time()-start)

def test_MergeBest():
    start= time()
    assert m_sort(bestcase) ==bestcase
    print (time()-start)

def test_MergeAvg():
    start= time()
    assert m_sort(averagecase) == bestcase
    print(time()-start)