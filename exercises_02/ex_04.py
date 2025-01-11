# Ex4: Read the entire file story.txt and write a program to print out top 100 words occur most
# frequently and their corresponding appearance. You could ignore all
# punction characters such as comma, dot, semicolon, ...
# Sample output:
# house: 453
# dog: 440
# people: 312
# ...

import re
from collections import Counter

def read_file(filename):
    with open(filename, "r") as file:
        data = file.read()
    return data

def count_words(data, top_n=100):
    # Loại bỏ các ký tự không phải chữ cái và chuyển thành chữ thường
    cleaned_data = re.sub(r"[^\w\s]", "", data).lower()

    # Tách thành danh sách các từ
    words = cleaned_data.split()

    # Đếm tần suất xuất hiện của từng từ
    word_counts = Counter(words)

    # Trả về top N từ xuất hiện nhiều nhất
    return word_counts.most_common(top_n)

if __name__ == "__main__":
    # Đọc dữ liệu từ file
    data = read_file("story.txt")

    # Đếm từ và lấy top 100 từ xuất hiện nhiều nhất
    top_words = count_words(data, top_n=100)

    # In kết quả
    print("Top 100 từ xuất hiện nhiều nhất và số lần xuất hiện:")
    for word, count in top_words:
        print(f"{word}: {count}")
