# Ex7: Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number.
# The numbers obtained should be printed in a comma-separated sequence on a single line.

def is_each_digit_even(num: int) -> bool:
    for i in str(num):
        if int(i) % 2 != 0:
            return False
    return True

def get_numbers_with_even_digits(start: int, end: int) -> list:
    result = []
    for i in range(start, end + 1):
        if is_each_digit_even(i):
            result.append(i)
    return result

if __name__ == "__main__":
    result = get_numbers_with_even_digits(1000, 3000)
    print(f"The numbers are: {', '.join(map(str, result))}")