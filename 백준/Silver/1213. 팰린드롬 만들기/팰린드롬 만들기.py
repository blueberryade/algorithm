import sys
from collections import Counter
input = sys.stdin.readline

def make_palindrome(word):
    count = Counter(word)
    odd = ""
    half = []

    for i in sorted(count.keys()):
        if count[i]%2 == 1:
            if odd:
                return "I'm Sorry Hansoo"
            odd = i
        half.append(i*(count[i]//2))

    first_half = "".join(half)
    second_half = first_half[::-1]
    return first_half+odd+second_half


word = input().rstrip()
print(make_palindrome(word))
            