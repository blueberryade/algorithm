def solution(number, k):
    answer = []
    for i in range(len(number)):
        while answer and k > 0 and answer[-1] < number[i]:
            answer.pop()
            k-=1
        answer.append(number[i])
    return ''.join(answer[:len(answer)-k])