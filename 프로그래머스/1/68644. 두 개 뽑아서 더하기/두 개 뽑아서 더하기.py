def solution(numbers):
    answer = []
    n=len(numbers)
    for i in range(n-1):
        for j in range(n-i-1):
            res1=numbers[i]+numbers[j+i+1]
            answer.append(res1)
    answer=sorted(set(answer))
    return answer