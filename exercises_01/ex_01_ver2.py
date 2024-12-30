# Ex1: Write a program to count positive and negative numbers in a list
data1 = [-10, -21, -4, -45, -66, 93, 11, -4, -6, 12, 11, 4]

def main() -> None:
    positive = 0
    negative = 0
    for i in data1:
        if i > 0:
            positive += 1
        elif i < 0:
            negative += 1
    print(f"There are {positive} positive numbers and {negative} negative numbers in the list")

if __name__ == "__main__":
    main()