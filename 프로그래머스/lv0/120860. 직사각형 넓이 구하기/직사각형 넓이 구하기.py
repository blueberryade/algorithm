def solution(dots):
    dots.sort()
    width = abs(dots[0][0]-dots[2][0])
    height = abs(dots[0][1]-dots[1][1])
    return width*height

