lst = []

for _ in range(5):
    score = list(map(int,input().split()))
    lst.append(sum(score))
    
print(lst.index(max(lst))+1, max(lst))