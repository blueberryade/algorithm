def solution(polynomial):
    answer = []
    xnum = 0
    lst = polynomial.split(' + ')
    xlst = [e for e in lst if 'x' in e]
    for e in xlst:
        if e.split('x')[0] =='':
            xnum+=1
        else:
            xnum+= int(e.split('x')[0])
    num = sum([int(e) for e in lst if 'x' not in e])
    if xnum !=0:
        answer.append('x' if xnum == 1 else f'{xnum}x')
    if num !=0:
        answer.append(str(num))
    result = ' + '.join(answer) if answer else '0'
    return result 