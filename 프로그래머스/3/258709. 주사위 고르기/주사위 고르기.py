from itertools import combinations, product
from bisect import bisect_left

def solution(dice):
    dic = {}
    n = len(dice)
    for A_index in combinations(range(n),n//2):
        B_index = [i for i in range(n) if i not in A_index]
        
        A,B = [],[]
        
        for p in product(range(6),repeat=n//2):
            A.append(sum(dice[i][j] for i,j in zip(A_index,p)))
            B.append(sum(dice[i][j] for i,j in zip(B_index,p)))
            
        B.sort()
        
        wins = sum(bisect_left(B,num) for num in A)
        dic[wins] = list(A_index)
        
    max_key = max(dic.keys())
    
    return [x+1 for x in dic[max_key]]