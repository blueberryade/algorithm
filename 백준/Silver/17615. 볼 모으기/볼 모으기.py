N = int(input())
data = list(input())

left_r = 0
left_b = 0
for ball in data:
    if ball == 'R':
        left_r += 1
    else:
        break
for ball in data:
    if ball == 'B':
        left_b += 1
    else:
        break

right_r = 0
right_b = 0

for ball in reversed(data):
    if ball == 'R':
        right_r += 1
    else:
        break
for ball in reversed(data):
    if ball == 'B':
        right_b += 1
    else:
        break

total_r = data.count('R')
total_b = data.count('B')    

result = min(
    total_r - left_r,  
    total_r - right_r, 
    total_b - left_b,  
    total_b - right_b  
)

print(result)