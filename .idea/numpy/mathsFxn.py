import numpy as np
import  math

#https://www.geeksforgeeks.org/numpy-mathematical-function/
#There are many mathematical functions in numpy like sin, cos, conj, clip, round etc.
########################################################################################################################
'''
#sine cosine tan etc.
in_array = [0, math.pi / 2, np.pi / 3, np.pi]
print ("Input array : \n", in_array)

Sin_Values = np.sin(in_array)
print ("\nSine values : \n", Sin_Values)
'''
########################################################################################################################
'''

#Rounding up
#This mathematical function helps user to evenly round array elements to the given number of decimals.

in_array = [.5, 1.5, 2.5, 3.5, 4.5, 10.1]
print ("Input array : \n", in_array)

round_off_values = np.around(in_array)
print ("\nRounded values : \n", round_off_values)


in_array = [.53, 1.54, .71]
print ("\nInput array : \n", in_array)

round_off_values = np.around(in_array)
print ("\nRounded values : \n", round_off_values)

in_array = [.5538, 1.33354, .71445]
print ("\nInput array : \n", in_array)

round_off_values = np.around(in_array, decimals = 3)
print ("\nRounded values : \n", round_off_values)
'''
########################################################################################################################

'''
#Clip function
This function is used to Clip (limit) the values in an array.
Given an interval, values outside the interval are clipped to the interval edges. 
For example, if an interval of [0, 1] is specified, values smaller than 0 become 0, and values larger than 1 become 1.

in_array = [1, 2, 3, 4, 5, 6, 7, 8 ]
print ("Input array : ", in_array)
 
out_array = np.clip(in_array, a_min = 2, a_max = 6)
print ("Output array : ", out_array)

'''
########################################################################################################################
