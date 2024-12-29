# Ex5: Given two matrices (2 nested lists), the task is to write a Python program
# to add elements to each row from initial matrix.
# For example: Input : test_list1 = [[4, 3, 5,], [1, 2, 3], [3, 7, 4]], test_list2 = [[1], [9], [8]]
# Output : [[4, 3, 5, 1], [1, 2, 3, 9], [3, 7, 4, 8]]
data5_list1 = [[4, 3, 5, ], [1, 2, 3], [3, 7, 4]]
data5_list2 = [[1, 3], [9, 3, 5, 7], [8]]

def add_elements(list1, list2) -> list:
    result = []
    if len(list1) != len(list2):
        print("The two lists are not of the same size")
        return result

    for i in range(len(list1)):
        result.append(list1[i] + list2[i])
    return result

if __name__ == "__main__":
    result = add_elements(data5_list1, data5_list2)
    print(f"The result is: {result}")