t = int(input())
for _ in range(t):
	lst = list(map(str,input().split()))
	result = float(lst[0])
	for i in range(1,len(lst)):
		if lst[i] == '@':
			result*=3
		elif lst[i] == '%':
			result+=5
		elif lst[i] == '#':
			result-=7
	print('%.2f' % result)