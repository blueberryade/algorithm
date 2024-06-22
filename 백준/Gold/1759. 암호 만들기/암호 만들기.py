import sys
from itertools import combinations
input = sys.stdin.readline

l,c = map(int,input().split())
alphabet = input().split()
alphabet.sort()


def is_valid(password):
    vowel_count = 0
    constant_count = 0
    for p in password:
        if p in 'aeiou':
            vowel_count+=1
        else:
            constant_count+=1
    return vowel_count>=1 and constant_count>=2




for c in combinations(alphabet,l):
    if is_valid(c):
        print(''.join(c))