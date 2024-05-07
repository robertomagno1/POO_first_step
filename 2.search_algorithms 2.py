"""This file contains an implementation of a
sequential search and a binary search in an ordered list"""

import time

def sequential_search_with_ordered_list_(l, k):
    i = 0
    while i < len(l):
        if l[i] == k:
            return True
        if l[i] > k:
            return False
        i = i + 1
    return False



def binary_search(l, k):

    low=0
    high = len(l)-1

    while low <= high:
        middle = (low+high) // 2
        if l[middle]==k:
            return True
        if k < l[middle]:
            high = middle - 1
        else:
            low = middle + 1

    return False



"""-------Entry point-------"""

#requirement: my_list should be an ordered list
my_list=[-10, -6, -2, 0, 1, 2, 3, 5, 12, 16, 22, 23, 25, 29, 30, 38]
value = 23
print("Input list: ", my_list)

start_time = time.time()

#please, select the algorithm to be used by removing # in one the two following lines
found = sequential_search_with_ordered_list_(my_list, value)
#found = binary_search(my_list, value)

end_time = time.time()

print("Found: ", found)
print("Elapsed time:", round(1000* (end_time - start_time), 6), "milliseconds")





def binary_search(l, k):

    low=0
    high = len(l)-1

    while low <= high:
        middle = (low+high) // 2
        if l[middle]==k:
            return middle
        if k < l[middle]:
            high = middle - 1
        else:
            low = middle + 1

    return -1



# NON MODIFICARE
def test(a, b):
    print(binary_search(a,b))d


   
   
###classe punto

import math 

class Punto:
    
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    def dist(self,p):
        dx = self.x - p.x
        dy = self.y - p.y
    
        return math.sqrt(dx**2+dy**2)
        
    
