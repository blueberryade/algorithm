import math

def solution(arrayA, arrayB):
    
    def gcdList(lst):
        a = lst[0]
        for b in lst[1:]:
            a = math.gcd(a,b)
        return a
    
    def canDiv(array,gcd):
        for i in array:
            if i%gcd == 0:
                return False
        return True
    
    gcdA = gcdList(arrayA)
    gcdB = gcdList(arrayB)
    
    if canDiv(arrayB,gcdA):
        answerA = gcdA
    else:
        answerA = 0
    
    if canDiv(arrayA,gcdB):
        answerB = gcdB
    else:
        answerB = 0
        
    return max(answerA,answerB)