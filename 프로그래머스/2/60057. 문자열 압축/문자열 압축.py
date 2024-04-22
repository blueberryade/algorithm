def solution(s):
    answer = []

    if len(s) == 1:
        return 1

    for i in range(1, len(s)//2 + 1):
        result = ''
        temp = s[:i]
        cnt = 1
        
        for j in range(i, len(s), i):
            if temp == s[j:j+i]:
                cnt += 1
            else:
                if cnt > 1:
                    result += str(cnt) + temp
                else:
                    result += temp
                cnt = 1
                temp = s[j:j+i]
        if cnt > 1:
            result += str(cnt) + temp
        else:
            result += temp
        answer.append(len(result))
    return min(answer)