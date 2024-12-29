# Ex3: find the strongest neighbour. Given an array of N positive integers.
# The task is to find the maximum for every adjacent pair in the array.
data3 = [4, 5, 6, 7, 3, 9, 11, 2, 10]

def get_strongest_neighbour(data) -> list:
    result = []
    for i in range(len(data) - 1):
        result.append(max(data[i], data[i + 1]))
    return result

if __name__ == "__main__":
    result = get_strongest_neighbour(data3)
    print(f"The strongest neighbours are: {result}")