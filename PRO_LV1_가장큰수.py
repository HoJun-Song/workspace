#2022-07-11 1차 시도
def solution(numbers):
    arr = list(map(str, numbers))
    arr.sort(key=lambda x: (x[0:1], x[0:1] if len(x) < 2 else x[1:2], x[1:2] if len(x) < 3 else x[2:3]), reverse=True)
    answer = "".join(arr)
    return answer