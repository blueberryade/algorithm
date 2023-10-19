# 1번째 줄엔 제출하지 않은 학생의 출석번호 중 가장 작은 것을 출력하고, 2번째 줄에선 그 다음 출석번호를 출력한다.
arr = list(range(1,31))
for _ in range(28):
    i = int(input())
    arr.remove(i)
print(min(arr))
print(max(arr))