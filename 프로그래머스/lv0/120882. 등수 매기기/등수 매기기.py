def solution(score):
    rank = sorted([sum(i) for i in score], reverse = True)
    return [rank.index(sum(i))+1 for i in score]