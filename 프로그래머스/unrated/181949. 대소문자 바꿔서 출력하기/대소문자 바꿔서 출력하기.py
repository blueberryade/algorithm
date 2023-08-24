str = input()
s = ''
for i in str:
    if i.isupper():
        s+=i.lower()
    else:
        s+=i.upper()
print(s)        
