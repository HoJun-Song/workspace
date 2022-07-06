#2022-07-06 1차 시도
def solution(clothes):
    clothesType = []
    clothesType.append([clothes[0][1], 1])
    
    for i in range(1, len(clothes)):
        tmp = clothes[i][1]
        flag = 0
        
        for j in range(len(clothesType)):
            if tmp in clothesType[j][0]:
                flag = 1
                clothesType[j][1] += 1
                
        if flag == 0:
            clothesType.append([tmp, 1])
    
    print(clothesType)
    
    if len(clothesType) > 1:
        tmp = 1
        for i in clothesType:
            tmp *= (i[1] + 1)   
        answer = tmp - 1
        
    else:
        answer = clothesType[0][1]
        
    return answer