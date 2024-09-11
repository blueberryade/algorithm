from itertools import combinations
import sys
input = sys.stdin.readline

def count_read_word(selected,words):
    count = 0
    for word in words:
        if word.issubset(selected):
            count+=1
    return count

n,k = map(int,input().split())
essential = set(['a', 'n', 't', 'i', 'c'])

if k >=5 :
    words = []
    for _ in range(n):
        temp = set(input().rstrip()[4:-4]) - essential
        words.append(temp)

    available = set(chr(i) for i in range(97,123))-essential

    max_count = 0

    for c in combinations(available,k-5):
        selected = essential.union(set(c))
        max_count = max(max_count,count_read_word(selected,words))

    print(max_count)

else:
    print(0)