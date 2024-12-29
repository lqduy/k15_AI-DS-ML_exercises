# Ex6:  Write a program which will find all such numbers which are divisible by 7
# but are not a multiple of 5, between 2000 and 3200 (both included).
# The numbers obtained should be printed in a comma-separated sequence on a single line.

def divisible_by_num(num: int, divisor: int) -> bool:
    if divisor == 0:
        return False
    return num % divisor == 0


if __name__ == "__main__":
    NUMBERS = range(2000, 3201)
    result = [i for i in NUMBERS if divisible_by_num(i, 7) and not divisible_by_num(i, 5)]
    print(f"The numbers are: {', '.join(map(str, result))}")
