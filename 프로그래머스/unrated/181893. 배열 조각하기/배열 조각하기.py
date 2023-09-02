def solution(arr, query):
    for i,e in enumerate(query):
        if i%2==0:
            arr = arr[0:e+1]
        else:
            arr = arr[e:]
    return arr