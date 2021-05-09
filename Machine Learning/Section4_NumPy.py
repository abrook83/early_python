import numpy as np      # standard convention is 'np'

my_list = [1,2,3]
print(type(my_list))

"""Create a basic 1D array"""
my_array = np.array(my_list)
print(my_array)
print(type(my_array))

"""Create a basic matrix"""
my_matrix = [[1,2,3],[4,5,6],[7,8,9]]
matr_array = np.array(my_matrix)
print(matr_array)

"""Create a basic range array"""
range_array = np.arange(0,10)   # 'arange' not 'arrange'!
print(range_array)

"""Create a array of 0's""" # Can also be done with 1's
print(np.zeros(5))          # Outputs as floating point numbers....
print(np.ones((6,6)))       # Important to enter dimensions as a tuple