def solution(a, b):
    answer = 0
    if a-b<0:
        gap = a-b-1
        for _ in range(-gap):
            answer+=b
            b-=1
    elif a-b>0:
        gap = a-b+1
        for _ in range(gap):
            answer+=a
            a-=1
    else:
        gap = 1
        answer = a
    return answer