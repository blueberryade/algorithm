import sys
input = sys.stdin.readline

def is_palindrome(s):
    return s==s[::-1]

s = list(input().strip())
l = len(s)

if not is_palindrome(s):
    print(l)
elif len(set(s)) == 1:
    print(-1)
else:
    print(l-1)