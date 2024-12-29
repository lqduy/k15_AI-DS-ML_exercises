from collections import deque

def get_en_words_list() -> set:
    MIN_WORD_LENGTH = 3
    with open('wordsEn.txt', 'r') as file:
        return {line.strip() for line in file.readlines() if len(line.strip()) >= MIN_WORD_LENGTH}

def input_words(en_words: set) -> list:
    words = []
    words_valid = False
    while not words_valid:
        word_1 = input("Enter the first word: ").strip()
        word_2 = input("Enter the second word: ").strip()
        if word_1 in en_words and word_2 in en_words:
            words.append(word_1)
            words.append(word_2)
            words_valid = True
        else:
            print("\n--- Invalid input ---\n")
    return words

def get_next_words(current_word: str, en_words: set) -> list:
    next_words = []
    current_end = current_word[-2:]
    for word in en_words:
        if word != current_word and word[:2] == current_end:
            next_words.append(word)
    return next_words

def find_shortest_chain(start_word: str, end_word: str, words: set) -> list:
    queue = deque([(start_word, [start_word])])
    visited = set()
    visited.add(start_word)

    while queue:
        current_word, path = queue.popleft()

        if current_word == end_word:
            return path

        next_words = get_next_words(current_word, words)
        for next_word in next_words:
            if next_word not in visited:
                visited.add(next_word)
                queue.append((next_word, path + [next_word]))
    return []

def main():
    en_words = get_en_words_list()
    start_word, end_word = input_words(en_words)

    chain = find_shortest_chain(start_word, end_word, en_words)

    if chain:
        print("Shortest chain:", " -> ".join(chain))
    else:
        print("No valid chain found.")

if __name__ == "__main__":
    main()
