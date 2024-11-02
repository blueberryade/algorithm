n = int(input())

def drawStar(n):
    if n == 1:
        return ['*']
    stars = drawStar(n//3)
    lst = []

    for star in stars:
        lst.append(star*3)
    for star in stars:
        lst.append(star+' '*(n//3)+star)
    for star in stars:
        lst.append(star*3)
        
    return lst

print('\n'.join(drawStar(n)))