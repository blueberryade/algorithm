n = int(input())

for _ in range(n):
    s = input()
    result = s[0].upper() + s[1:]
    print(result)