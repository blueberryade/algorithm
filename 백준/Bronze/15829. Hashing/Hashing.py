l = int(input())
s = input()
m = 1234567891
r = 31
result = 0

for i in range(len(s)):
    num = ord(s[i])-96
    result += num * (r**i)
print(result%m)    