def solution(num_list):
    odd = 0
    even = 0
    for i,e in enumerate(num_list):
        if (i+1)%2 == 0:
            even +=e
        else:
            odd +=e
    return max(odd,even)
    