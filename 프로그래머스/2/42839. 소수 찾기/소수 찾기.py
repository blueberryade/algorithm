from itertools import permutations
def solution(numbers):
    answer = set()
    numbers = list(numbers)
    
    def isPrime(x):
        if x < 2:
            return False 
        for i in range(2,int(x**0.5)+1):
            if x%i ==0:
                return False
        
        return True
    
    temp = []
    for i in range(1,len(numbers)+1):
        temp += list(permutations(numbers,i))
    temp = [int(''.join(t)) for t in temp]
        
    for t in temp:
        if isPrime(t):
            answer.add(t)
        
    return len(answer)