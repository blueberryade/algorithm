import sys
input = sys.stdin.readline

n = int(input())
def is_palindrome(word, left, right):
    while left < right:
        if word[left] != word[right]:
            return False
        left += 1
        right -= 1
    return True

def palindrome(word):
    left = 0
    right = len(word) - 1
    while left < right:
        if word[left] == word[right]:
            left += 1
            right -= 1
        else:
            if is_palindrome(word,left+1,right) or is_palindrome(word,left,right-1):
                    return 1
            return 2
    return 0

for _ in range(n):
    word = input().rstrip()
    print(palindrome(word))

            
        

