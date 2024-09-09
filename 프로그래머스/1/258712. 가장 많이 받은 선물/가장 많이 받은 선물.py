def solution(friends, gifts):
    l = len(friends)
    answer = [0]*l
    data = [[0]*l for _ in range(l)]
    gift_index = [0]*l
    
    for gift in gifts:
        a,b = gift.split()
        a_idx = friends.index(a)
        b_idx = friends.index(b)
        data[a_idx][b_idx]+=1
        gift_index[a_idx]+=1
        gift_index[b_idx]-=1
    
    
    for i in range(l):
        for j in range(l):
            if i == j:
                continue
            if data[i][j] > data[j][i]:
                answer[i]+=1
            elif data[i][j]==data[j][i]:
                if gift_index[i] > gift_index[j]:
                    answer[i]+=1
    
    
    return max(answer)