def solution(arr, k):
    return [e*k if k%2==1 else e+k for e in arr]