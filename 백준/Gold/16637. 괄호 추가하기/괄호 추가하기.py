import sys
input = sys.stdin.readline

n = int(input())
data = list(input().rstrip())
result = -1 * sys.maxsize

def calculate(a,op,b):
    if op == '+':
        return a+b
    elif op == '-':
        return a-b
    elif op == '*':
        return a*b

def dfs(idx,value):
    global result

    if idx == n-1:
        result = max(result,value)
        return
    
    if idx+2 < n:
        dfs(idx+2, calculate(value, data[idx+1],int(data[idx+2])))

    if idx+4 < n:
        dfs(idx+4,calculate(value,data[idx+1],calculate(int(data[idx+2]),data[idx+3],int(data[idx+4]))))

dfs(0,int(data[0]))
print(result)