import sys 
input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split()))
arr.sort()

start = 0
end  = n-1

num = sys.maxsize
result = []


while start < end:
    s = arr[start]+arr[end]

    if abs(s) < num:
        num = abs(s)
        result = [arr[start],arr[end]]
    if s < 0:
        start+=1
    elif s > 0:
        end-=1
    else:
        break

result.sort()
print(result[0],result[1])