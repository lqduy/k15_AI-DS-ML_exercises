from collections import deque

file = open('wordsEn.txt', 'r')
words = [word.strip() for word in file.readlines() if len(word.strip()) > 2]

word_dict = {}
for word in words:
    prefix = word[:2]
    if prefix not in word_dict:
        word_dict[prefix] = [word]
    else:
        word_dict[prefix].append(word)


def find(str, target):
    q = deque([(str, [str])])
    visited = {str}
    while q:
        cur_word, arr = q.popleft()
        if cur_word == target:
            return arr
        suf = cur_word[-2:]
        if suf in word_dict:
            for n_word in word_dict[suf]:
                if n_word not in visited:
                    visited.add(n_word)
                    q.append((n_word, arr + [n_word]))
    return None

s1, s2 = input().split(' ')

ans = '\n'.join(find(s1,s2))

print(ans)