def solution(strArr):
    return [e.lower() if i%2 ==0 else e.upper() for i,e in enumerate(strArr)]