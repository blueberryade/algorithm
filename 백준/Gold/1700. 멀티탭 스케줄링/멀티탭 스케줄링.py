n,k = map(int,input().split())
lst = list(map(int,input().split()))

cnt = 0
multitap = []

for i in range(k):
    if lst[i] in multitap:
        continue

    if len(multitap) < n:
        multitap.append(lst[i])
        
    else:
        last_usage_index = -1
        unplug = -1
        for device in multitap:
            if device not in lst[i:]:
                unplug = device
                break
            else:
                next_usage_index = lst[i:].index(device)
                if next_usage_index > last_usage_index:
                    last_usage_index = next_usage_index
                    unplug = device
        multitap.remove(unplug)
        multitap.append(lst[i])
        cnt+=1

print(cnt)