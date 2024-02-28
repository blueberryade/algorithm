import sys
input = sys.stdin.readline

s,p = map(int,input().split())
string = list(str(input()))
lst = list(map(int,input().split()))
check = {'A':lst[0],'C':lst[1],'G':lst[2],'T':lst[3]}

dic = {'A':0,'C':0,'G':0,'T':0}
result = 0

for i in range(s-p+1):
    flag = True
    if i == 0:
        for j in range(p):
            dic[string[j]]+=1
    else:
        dic[string[i+p-1]]+=1
        dic[string[i-1]]-=1
    for i in ('A','C','G','T'):
        if dic[i]<check[i]:
            flag = False
            break
    if flag:
        result+=1
print(result)    