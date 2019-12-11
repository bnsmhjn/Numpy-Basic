import numpy as np

########################################################################################################################
'''
# converting to lowercase
arr = np.array(['GEEKS', 'FOR'])
print(np.char.lower(arr))

'''
########################################################################################################################

'''
# splitting a string
print(np.char.split('geeks  forgeeks'))
print(np.char.split('geeks| for| geeks', sep = '|'))

'''
########################################################################################################################
'''
#equal/not equal
in_arr1 = np.array('benish')
print ("1st Input array : ", in_arr1)

in_arr2 = np.array('benish')
print ("2nd Input array : ", in_arr2)

# checking if they are equal 
out_arr = np.char.equal(in_arr1, in_arr2)
print ("Output array: ", out_arr)  

------------------------------------------------------------------------------------------------------------------------
in_arr1 = np.array(['benish', 'maharjan'])
print ("1st Input array : ", in_arr1)

in_arr2 = np.array(['besish', 'mjn'])
print ("2nd Input array : ", in_arr2)

# checking if they are equal
out_arr = np.char.not_equal(in_arr1, in_arr2)
print ("Output array: ", out_arr)

'''
########################################################################################################################
