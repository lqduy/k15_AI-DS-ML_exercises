# Ex2: Given a list, extract all elements whose frequency is greater than k.
data2 = [4, 6, 4, 3, 3, 4, 3, 4, 3, 8]
k = 3

def get_frequent(data) -> dict:
    freq = {}
    for i in data:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    return freq

if __name__ == "__main__":
    freq = get_frequent(data2)
    result_numbers = [i for i in freq if freq[i] > k]
    print(f"The list has the following numbers with frequency greater than {k}: {result_numbers}")