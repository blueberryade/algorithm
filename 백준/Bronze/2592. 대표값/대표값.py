lst = []
for _ in range(10):
    lst.append(int(input()))
print(sum(lst)//10)
print(max(lst,key=lst.count))