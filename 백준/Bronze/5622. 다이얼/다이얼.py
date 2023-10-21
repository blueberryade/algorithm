lst = ['ABC', 'DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
word = input()
time = 0
for i in word:
    for j in lst:
        if i in j:
            num = lst.index(j)+3
            time += num
print(time)
