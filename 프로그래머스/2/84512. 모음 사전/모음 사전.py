def solution(word):
    answer = 0
    vowels = ["A","E","I","O","U"]
    lst = [5**i for i in range(5)]
    
    for i in range(len(word)-1,-1,-1):
        idx = vowels.index(word[i])
        for j in range(5-i):
            answer+=lst[j]*idx
        answer+=1
    return answer