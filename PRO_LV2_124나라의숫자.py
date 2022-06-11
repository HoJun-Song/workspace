#2022-05-29 1차 시도
def solution(n):
    
    answer = ''
    arr = []
    n = int(n)
    
    while n >= 1:
        tmp = int(n % 3)
        arr.append(tmp)
        n = int(n / 3)
        
    arr.reverse()
    
    for i in arr:
        answer += str(i)
    
    return answer