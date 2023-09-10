def solution(quiz):
    answer = []
    for i in quiz:
        l,r = i.split(' = ')
        a,op,b = l.split()
        if op == '+':
            result = 'O' if int(a)+int(b) == int(r) else 'X'
            answer.append(result)
        else:
            result = 'O' if int(a)-int(b) == int(r) else 'X'
            answer.append(result)
    return answer