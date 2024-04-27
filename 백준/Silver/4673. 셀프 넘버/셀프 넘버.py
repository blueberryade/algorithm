numbers = set(range(1,10001))
remove_set = set()

for num in numbers:
    for n in str(num):
        num+=int(n)
    remove_set.add(num)

self_number = sorted(numbers-remove_set)
for i in self_number:
    print(i)
