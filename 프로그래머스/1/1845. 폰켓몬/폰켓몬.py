def solution(nums):
    num1 = len(nums)/2
    num2 = len(set(nums))
    return min(num1,num2)