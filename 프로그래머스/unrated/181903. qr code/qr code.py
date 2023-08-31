def solution(q, r, code):
    return ''.join(code[i] for i in range(r,len(code),q))