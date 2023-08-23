def solution(numbers):
    num = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    i=0
    for word in num:
        numbers = numbers.replace(word,str(i))
        i+=1
    return int(numbers)