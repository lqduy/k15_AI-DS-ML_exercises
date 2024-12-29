# Ex1: Write a program to count positive and negative numbers in a list
data1 = [-10, -21, -4, -45, -66, 93, 11, -4, -6, 12, 11, 4]

def count_positive(data) -> int:
    count = 0
    for i in data:
        if i > 0:
            count += 1
    return count

def count_negative(data) -> int:
    count = 0
    for i in data:
        if i < 0:
            count += 1
    return count

if __name__ == "__main__":
    positive = count_positive(data1)
    negative = count_negative(data1)
    print(f"There are {positive} positive numbers and {negative} negative numbers in the list")

