def solution(num_list):
    a = int(''.join([str(i) for i in num_list if i%2 ==0]))
    b = int(''.join([str(i) for i in num_list if i%2 ==1]))
    return a+b