import sys
input = sys.stdin.readline

while True:
    try:
        x = int(input())*10000000
        n = int(input())
        lego = [int(input()) for _ in range(n)]
        lego.sort()
        answer = []

        left,right = 0,n-1
        while left < right:
            if lego[left]+lego[right] < x:
                left+=1
            elif lego[left]+lego[right] > x:
                right-=1
            else:
                answer = [lego[left],lego[right]]
                break
        
        if answer:
            print("yes",answer[0],answer[1])
        else:
            print("danger")

    except:
        break
    