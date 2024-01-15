n = int(input())
no = 0
yes = 0
for _ in range(n):
    c = input()
    if c == '1':
        yes+=1
    else:
        no+=1
print("Junhee is cute!" if yes>no else  "Junhee is not cute!")