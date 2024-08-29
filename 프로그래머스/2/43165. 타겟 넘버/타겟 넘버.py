def dfs(numbers,i,n,target):
    result = 0
    if i == len(numbers):
        if n == target:
            return 1
        else:
            return 0
    
    result += dfs(numbers,i+1,n+numbers[i],target)
    result += dfs(numbers,i+1,n-numbers[i],target)
    return result

def solution(numbers, target):
    answer = dfs(numbers,0,0,target)
    return answer