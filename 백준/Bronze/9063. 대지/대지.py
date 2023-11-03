n = int(input())
x_lst = []
y_lst = []
for i in range(n):
    x,y = map(int,input().split())
    x_lst.append(x)
    y_lst.append(y)

x_num = max(x_lst) - min(x_lst)
y_num = max(y_lst) - min(y_lst)
print(x_num*y_num)