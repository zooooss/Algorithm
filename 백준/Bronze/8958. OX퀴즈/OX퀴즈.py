num = int(input())
for _ in range(num):
    line = input()
    score = 0
    consecutive = 0
    for i in range(len(line)):
        if line[i]=='O':
            consecutive+=1
            score+=consecutive
        else:
            consecutive=0
    print(score)