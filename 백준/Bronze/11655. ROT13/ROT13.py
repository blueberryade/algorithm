word = input()
for i in word:
    if i.isupper():
        if ord(i)+13 <=90:
            print(chr(ord(i)+13),end='')
        else:
            print(chr(ord(i)-13),end='')
    elif i.islower():
        if ord(i)+13<=122:
            print(chr(ord(i)+13),end='')
        else:
            print(chr(ord(i)-13),end='')
    else:
        print(i,end='')