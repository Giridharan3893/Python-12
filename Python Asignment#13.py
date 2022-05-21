#!/usr/bin/env python
# coding: utf-8

# In[1]:


##Answer1:

test_list = [(5, 6), (5, 7), (6, 8), (6, 10), (7, 13)]

print("The original list is : " + str(test_list))

res = []
for sub in test_list:                                           
    if res and res[-1][0] == sub[0]:              
        res[-1].extend(sub[1:])                        
    else:
        res.append([ele for ele in sub])     
res = list(map(tuple, res))

print("The extracted elements : " + str(res)) 


# In[2]:


##Answer2:

from itertools import chain

test_list = [(15, 3), (3, 9), (1, 10), (99, 2)]

print("The original list is : " + str(test_list))

temp = map(lambda ele: str(ele), chain.from_iterable(test_list))
res = set()
for sub in temp:
    for ele in sub:
        res.add(ele)

print("The extracted digits : " + str(res))


# In[3]:


##Answer3:

test_tuple1 = (4, 5)
test_tuple2 = (7, 8)

print("The original tuple 1 : " + str(test_tuple1))
print("The original tuple 2 : " + str(test_tuple2))

res =  [(a, b) for a in test_tuple1 for b in test_tuple2]
res = res +  [(a, b) for a in test_tuple2 for b in test_tuple1]

print("The filtered tuple : " + str(res))


# In[4]:


##Answer4:

test_list = [(4, 5), (4, ), (8, 6, 7), (1, ), (3, 4, 6, 7)]

print("The original list : " + str(test_list))

K = 1

res = [ele for ele in test_list if len(ele) != K]

print("Filtered list : " + str(res))


# In[6]:


##Answer5:

def Sort_Tuple(tup):
    lst = len(tup)
    for i in range(0, lst):
         
        for j in range(0, lst-i-1):
            if (tup[j][1] > tup[j + 1][1]):
                temp = tup[j]
                tup[j]= tup[j + 1]
                tup[j + 1]= temp
    return tup

tup =[('gets', 24), ('going', 10), ('going', 28),
      ('When the', 5), ('the tough', 20), ('gets tough', 15)]
       
print(Sort_Tuple(tup))


# In[8]:


##Answer6:

test_list = [('gets going', 3), ('gets tough', 9), ('the tough', 10), ('When the going', 2)]
print("The original list is : " + str(test_list))
ord_list = ['When the going', 'gets tough', 'the tough', 'gets going']

temp = dict(test_list)
res = [(key, temp[key]) for key in ord_list]

print("The ordered tuple list : " + str(res)) 


# In[9]:


##Answer7:

test_tuple = ([5, 6], [6, 7, 8, 9], [3])

print("The original tuple : " + str(test_tuple))

res = tuple(sum(test_tuple, []))

print("The flattened tuple : " + str(res))


# In[11]:


##Answer8:

test_tuple = ((4, 'RCB', 10), (3, 'is', 8), (6, 'Best', 10))

print("The original tuple : " + str(test_tuple))

res = [{'key': sub[0], 'value': sub[1], 'id': sub[2]} 
                               for sub in test_tuple]

print("The converted dictionary : " + str(res))


# In[12]:


##Answer9:

def binary_search(arr, low, high, x):

    if high >= low:
 
        mid = (high + low) // 2
 
        if arr[mid] == x:
            return mid

        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)

        else:
            return binary_search(arr, mid + 1, high, x)
 
    else:

        return -1

arr = [ 2, 3, 4, 10, 40 ]
x = 10

result = binary_search(arr, 0, len(arr)-1, x)
 
if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")


# In[15]:


##Answer10:

def linear_Search(list1, n, key):  
  
    # Searching list1 sequentially  
    for i in range(0, n):  
        if (list1[i] == key):  
            return i  
    return -1  
  
  
list1 = [1 ,3, 5, 4, 7, 9]  
key = 7  
  
n = len(list1)  
res = linear_Search(list1, n, key)  
if(res == -1):  
    print("Element not found")  
else:  
    print("Element found at index: ", res)  


# In[16]:


##Answer11:

def insertionSort(arr):

    for i in range(1, len(arr)):
  
        key = arr[i]

        j = i-1
        while j >=0 and key < arr[j] :
                arr[j+1] = arr[j]
                j -= 1
        arr[j+1] = key

arr = [12, 11, 13, 5, 6]
insertionSort(arr)
print ("Sorted array is:")
for i in range(len(arr)):
    print ("%d" %arr[i])


# In[ ]:




