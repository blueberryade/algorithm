n = int(input())
arr = list(map(int,input().split()))
m = max(arr)
newArr = [ i/ m * 100 for i in arr ]
print(sum(newArr)/n)