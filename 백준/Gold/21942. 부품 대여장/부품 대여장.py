import sys
from datetime import datetime, timedelta
from collections import defaultdict
input = sys.stdin.readline

DATE_FORMAT = "%Y-%m-%d %H:%M"

N,L,F = input().rstrip().split()
N,F = int(N),int(F)

D, T = L.split("/")
H,M = map(int,T.split(":"))
D = int(D)
limit_duration = timedelta(days=D, hours=H, minutes=M)

rent_records = defaultdict(list)

for _ in range(N):
    date, time, item, user = input().split()
    timestamp = datetime.strptime(f"{date} {time}", DATE_FORMAT)
    rent_records[(user, item)].append(timestamp)

result = defaultdict(int)

for (user, item), timestamps in rent_records.items():
    if len(timestamps) < 2:
        continue  

    
    for i in range(0,len(timestamps),2):
        rent_time = timestamps[i]
        return_time = timestamps[i+1]
        duration = return_time - rent_time

        if duration > limit_duration:
            overtime_minutes = (duration - limit_duration).total_seconds() // 60
            result[user] += int(overtime_minutes * F) 

if result:
    for user in sorted(result):
        print(user, result[user])
else:
    print(-1)
