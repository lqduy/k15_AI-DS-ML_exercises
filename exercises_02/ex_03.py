# Ex3: Write a NumPy program to find the indices of the maximum and minimum values along the given axis of an array
# Input Array: [1, 6, 4, 8, 9, -4, -2, 11]

import numpy as np

def find_max_min_indices(data):
    max_index = np.argmax(data)
    min_index = np.argmin(data)
    return max_index, min_index

if __name__ == "__main__":
    data = np.array([1, 6, 4, 8, 9, -4, -2, 11])

    max_index, min_index = find_max_min_indices(data)

    print(f"The index of the maximum value is: {data[max_index]}")
    print(f"The index of the minimum value is: {data[min_index]}")
