import numpy as np
#https://www.geeksforgeeks.org/numpy-iterating-over-array/
########################################################################################################################
'''
a = np.arange(12).reshape(3,4)

print('Original array is:')
print(a)

print('Modified array in C-style order:')

for x in np.nditer(a, order = 'C'):
    print(x)

#order K = keep it in the same order

print('Modified array in F-style order:')

for x in np.nditer(a, order = 'F'):
    print(x)

'''
########################################################################################################################
'''

#Modifying array values using iterator
a = geek.arange(12)

# shape array with 3 rows and 
# 4 columns 
a = a.reshape(3,4)
print('Original array is:')
print(a)
print()

# modifying array values
for x in geek.nditer(a, op_flags = ['readwrite']):
    x[...] = 5*x
print('Modified array is:')
print(a)
'''
########################################################################################################################

'''
#Flag Parameters in nditer
#externan_loop

a = np.arange(12)
a = a.reshape(3,4)

print('Original array is:')
print(a)
print()

print('Modified array is:')
for x in np.nditer(a, flags = ['external_loop'], order = 'C'):
    print(x)

'''
########################################################################################################################
'''
#index of iterator
a = np.arange(6)
a = a.reshape(2,3)

print('Original array is:')
print(a)
print()

it = np.nditer(a, flags=['f_index'])
while not it.finished:
    print("%d <%d>" % (it[0], it.index), end=" ")
    it.iternext()
'''
########################################################################################################################

'''
# Broadcasting Iteration:
# If two arrays are broadcastable, a combined nditer object is able to iterate upon them concurrently. 
#Assuming that an array a has dimension 3X4, and there is another array b of dimension 1X4, the iterator of following type
 is used (array b is broadcast to size of a).

a = np.arange(12)
a = a.reshape(3,4)

print('First array is:')
print(a)
print()

print('Second array is:')
b = np.array([5, 6, 7, 8], dtype = int)
print(b)
print()

print('Modified array is:')
for x,y in np.nditer([a,b]):
    print("%d:%d" % (x,y))
'''