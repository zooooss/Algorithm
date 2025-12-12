def solution(array, commands):
    answer = []
    for i in range(len(commands)):
        m = commands[i][0]
        n = commands[i][1]
        k=commands[i][2]
        new_array=array[m-1:n]
        new_array.sort()
        answer.append(new_array[k-1])
    return answer