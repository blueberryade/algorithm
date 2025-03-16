N = int(input())
books = {}
for _ in range(N):
    title = input().rstrip()
    if title not in books:
        books[title] = 1
    else:
        books[title]+=1

max_num = max(books.values())

result = []

for k,v in books.items():
    if v == max_num:
        result.append(k)

result.sort()

print(result[0])

