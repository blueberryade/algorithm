def solution(myStr):
    answer = [e for e in myStr.replace("b","a").replace("c","a").split("a") if e]
    return ['EMPTY'] if len(answer)==0 else answer