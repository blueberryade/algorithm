import sys
input = sys.stdin.readline

def CCW(x1,y1,x2,y2,x3,y3):
    temp = (x1*y2 + x2*y3 + x3*y1) - (x2*y1+x3*y2+x1*y3)
    if temp > 0:
        return 1
    elif temp < 0:
        return -1
    else:
        return 0

def isOverlab(x1, y1, x2, y2, x3, y3, x4, y4):
    if min(x1, x2) <= max(x3, x4) and min(x3, x4) <= max(x1, x2) and min(y1, y2) <= max(y3, y4) and min(y3, y4) <= max(y1, y2):
        return True
    return False

def isCross(x1, y1, x2, y2, x3, y3, x4, y4):
    abc = CCW(x1, y1, x2, y2, x3, y3) 
    abd = CCW(x1, y1, x2, y2, x4, y4)
    cda = CCW(x3, y3, x4, y4, x1, y1) 
    cdb = CCW(x3, y3, x4, y4, x2, y2) 
    
    if abc * abd == 0 and cda * cdb == 0:  
        return isOverlab(x1, y1, x2, y2, x3, y3, x4, y4) 
        
    elif abc * abd <= 0 and cda * cdb <= 0:  
        return True
          
    return False
   
def isInside(x,y,xmin,ymin,xmax,ymax):
    return xmin <= x <= xmax and ymin <=y<=ymax


def check(x1,y1,x2,y2,xmin,ymin,xmax,ymax):
    if isInside(x1,y1,xmin,ymin,xmax,ymax) or isInside(x2,y2,xmin,ymin,xmax,ymax):
        return True

    edges = [
        (xmin,ymin,xmin,ymax),
        (xmax,ymin,xmax,ymax),
        (xmin,ymin,xmax,ymin),
        (xmin,ymax,xmax,ymax)
    ]

    for x3,y3,x4,y4 in edges:
        if isCross(x1,y1,x2,y2,x3,y3,x4,y4):
            return True


    return False
    

T = int(input())
for _ in range(T):
    x1,y1,x2,y2,xmin,ymin,xmax,ymax = map(int,input().split())

    xmin,xmax = min(xmin,xmax),max(xmin,xmax)
    ymin,ymax = min(ymin,ymax),max(ymin,ymax)

    if check(x1,y1,x2,y2,xmin,ymin,xmax,ymax):
        print('T')
    else:
        print('F')