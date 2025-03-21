import sys
input = sys.stdin.readline

word = list(input().rstrip())
result = ['']*len(word)

def solution(start,word):
    if not word:
        return
    
    min_val = min(word)
    idx = word.index(min_val)
    result[start+idx] = min_val
    print(''.join(result))
    solution(start+idx+1,word[idx+1:])
    solution(start,word[:idx])

solution(0,word)

    