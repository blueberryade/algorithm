def solution(arr, intervals):
    a,b = intervals[0]
    c,d = intervals[1]
    one = arr[a:b+1]
    two = arr[c:d+1]
    return one+two