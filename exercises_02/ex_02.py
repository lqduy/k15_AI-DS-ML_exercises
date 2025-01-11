# Ex2: Write a NumPy program to test whether each element of a 1-D array is also present in a second array
# Input Array1: [0, 10, 20, 40, 60]
#       Array2: [10, 30, 40]

import numpy as np

def check_array_is_in_array(array1, array2):
    return np.isin(array1, array2)

if __name__ == "__main__":
    array1 = np.array([0, 10, 20, 40, 60])
    array2 = np.array([10, 30, 40])

    result = check_array_is_in_array(array1, array2)

    print(f"The result is: {result}")
