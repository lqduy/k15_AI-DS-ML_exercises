# Ex4: print all Possible Combinations from the three Digits
data4 = [1, 2, 3]

from itertools import permutations

if __name__ == "__main__":
    print("All Possible Combinations from the three Digits:")
    for i in permutations(data4, 3):
        print(i)
