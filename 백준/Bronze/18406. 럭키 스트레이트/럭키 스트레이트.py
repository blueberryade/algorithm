N = input()

l = len(N)//2
left = sum([int(i) for i in N[:l]])
right = sum([int(i) for i in N[l:]])

	
print('LUCKY' if left == right else 'READY')