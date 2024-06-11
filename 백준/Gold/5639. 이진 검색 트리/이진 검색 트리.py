import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

pre = []

while True:
    try:
        x = int(input())
    except:
        break
    pre.append(x)

def postOrder(start,end):
    if start > end:
        return
    mid = end+1

    for i in range(start+1,end+1):
        if pre[start] < pre[i]:
            mid = i
            break


    postOrder(start+1,mid-1)
    postOrder(mid,end)
    print(pre[start])

postOrder(0,len(pre)-1)