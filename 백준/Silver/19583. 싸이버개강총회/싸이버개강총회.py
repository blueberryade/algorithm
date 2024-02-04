import sys
input = sys.stdin.readline

s,e,q = map(str,input().split())
s = int(s[:2]+s[3:])
e = int(e[:2]+e[3:])
q = int(q[:2]+q[3:])
member = set()
cnt = 0

while True:
    try:
        time,name = input().split()
        time = int(time[:2]+time[3:])
        if time<=s:
            member.add(name)
        elif e<=time<=q and name in member:
            member.remove(name)
            cnt+=1
    except:
        break
print(cnt)