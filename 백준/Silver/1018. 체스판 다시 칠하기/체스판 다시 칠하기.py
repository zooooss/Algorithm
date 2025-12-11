n,m=map(int,input().split())
chess = [list(input().strip())for _ in range(n)]
answer=float('inf')
for i in range(n-7):
    for j in range(m-7):
        countW = 0
        countB = 0
        
        for x in range(8):
            for y in range(8):
                current = chess[i + x][j + y]
                if (x + y) % 2 == 0:
                    if current != 'W':
                        countW += 1
                    if current != 'B':
                        countB += 1
                else:
                    if current != 'B':
                        countW += 1
                    if current != 'W':
                        countB += 1
        answer = min(answer,countW,countB)
print(answer)