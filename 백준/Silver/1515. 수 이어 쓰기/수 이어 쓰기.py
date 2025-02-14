numbers = list(input())

result = 0
idx = 0

while True:
    result+=1
    for s in str(result):
        if numbers[idx]==s:
            idx+=1
            if idx >= len(numbers):
                print(result)
                exit()