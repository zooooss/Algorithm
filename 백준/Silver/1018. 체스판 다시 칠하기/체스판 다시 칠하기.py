m,n=map(int,input().split())
chess=[list(input().strip())for _ in range(m)]
res=float('inf')
for i in range(m-7):
    for j in range(n-7):
        countW,countB=0,0
        for x in range(8):
            for y in range(8):
                first = chess[i+x][j+y]
                if (x+y)%2==0:
                    if first != 'W':
                        countW+=1
                    if first != 'B':
                        countB+=1
                else:
                    if first != 'W':
                        countB+=1
                    if first != 'B':
                        countW+=1
        res = min(res,countW,countB)
print(res)