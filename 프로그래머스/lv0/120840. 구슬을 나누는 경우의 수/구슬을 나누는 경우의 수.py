def solution(balls, share):
    def factorial(num):
        f = 1
        for i in range(1,num+1):
            f*=i
        return f
    return factorial(balls)/(factorial(balls-share)*factorial(share))