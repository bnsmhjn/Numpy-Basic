import numpy as np

#https://www.geeksforgeeks.org/numpy-sorting-searching-and-counting/

########################################################################################################################
'''
#sorting
a = np.array([[3, 4, 1], [4, 1, 0]])
print ("array\n",a)

arr1 = np.sort(a, axis = 0)
print ("\nAlong y-axis : \n", arr1)


arr2 = np.sort(a, axis = -1)
print ("\nAlong x-axis : \n", arr2)

arr1 = np.sort(a, axis = None)
print ("\nAlong none axis : \n", arr1)
'''

########################################################################################################################

'''
#argsort (gives the sorted indices of the original array)

a = np.array([7,6,5,4,3,2,1])

print('Original array:\n', a)

b = np.argsort(a)
print('Sorted indices of original array->', b)

c = np.zeros(len(b), dtype = int)
for i in range(0, len(b)):
    c[i]= a[b[i]]
print('Sorted array->', c)

'''
########################################################################################################################

