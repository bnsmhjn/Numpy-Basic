import numpy as np


#https://www.quora.com/What-are-some-advantages-of-numpy-over-regular-lists-in-Python
#https://www.npsfornps.org/python-numpy/
#https://www.npsfornps.org/indexing-in-numpy/
'''
#multiplying each element by 0
a_list = [1,2,3,4,5,6]
c_list = [1,2,3,4,5,6]
c_list = [ x*0 for x in c_list]
print(c_list)

arr = np.array(c_list)
print(arr*0)

'''

########################################################################################################################
'''
#adding elements between tyo lists/arrays
a_list = [1,2,3,4,5,6]
c_list = [1,2,3,4,5,6]
addList = [e1 + e2 for (e1, e2) in zip(a_list, c_list)]
print(addList)

c=np.array(c_list)
a=np.array(a_list)
addArr = c+a
print(addArr)

#adding 2 3-dimensional arrays would require three nested loops (or reshaping, unless I am missing a simpler solution) in python,
# while it is as simple as above in numpy:

import numpy as np
a = np.array([[[1, 2],
               [3, 4]],
              [[4, 0],
               [2, 6]]])
b = np.array([[[3, 1],
               [6, 4]],
              [[3, 3],
               [5, 1]]])
c = a + b
print(c)
'''
########################################################################################################################
'''

#Slicing
arr = np.array([[-1, 2, 0, 4],
                [4, -0.5, 6, 0],
                [2.6, 0, 7, 8],
                [3, -7, 4, 2.0]])
print("Initial Array: ")
print(arr)

# Printing a range of Array
# with the use of slicing method
sliced_arr = arr[:3, ::2]
print ("Array with first 3 rows and"
       " alternate columns(0 and 2):\n", sliced_arr)


# Printing elements at
# specific Indices
Index_arr = arr[[1, 1, 0, 3],
                [3, 2, 1, 3]]
print ("\nElements at indices (1, 3), "
    "(1, 2), (0, 1), (3, 0):\n", Index_arr)

'''
########################################################################################################################
'''
#forced data type

x = np.array([1, 2])
print("Integer Datatype: ")
print(x.dtype)

# Forced Datatype
x = np.array([1, 2], dtype = np.int64)
print("\nForcing a Datatype: ")
print(x.dtype)

'''
########################################################################################################################
'''
#math operations

# First Array
arr1 = np.array([[4, 7], [2, 6]],
                dtype = np.float64)

# Second Array
arr2 = np.array([[3, 6], [2, 8]],
                dtype = np.float64)

# Addition of two Arrays
Sum = np.add(arr1, arr2)
print("Addition of Two Arrays: ")
print(Sum)

# Addition of all Array elements
# using predefined sum method
Sum1 = np.sum(arr1)
print("\nAddition of Array elements: ")
print(Sum1)


# Square root of Array
Sqrt = np.sqrt(arr1)
print("\nSquare root of Array1 elements: ")
print(Sqrt)

# Transpose of Array
# using In-built function 'T'
Trans_arr = arr1.T
print("\nTranspose of Array: ")
print(Trans_arr)

'''
########################################################################################################################
'''
#Extract() function
array = np.arange(10).reshape(5, 2)
print("Original array : \n", array)

a = np.mod(array, 4) !=0
# This will show element status of satisfying condition
print("\nArray Condition a : \n", a)

# This will return elements that satisy conditon "a" condition
print("\nElements that satisfy conditon a  : \n", np.extract(a, array))



b = array - 4 == 1
# This will show element status of satisfying condition
print("\nArray Condition b : \n", b)

# This will return elements that satisy conditon "b" condition
print("\nElements that satisfy conditon b  : \n", np.extract(b, array))
'''

########################################################################################################################

