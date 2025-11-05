c = int(input())
for _ in range(c):
    array=list(map(int,input().split()))
    n = array[0]
    scores = array[1:]
    total = sum(scores)
    avg=total/n
    value = 0
    for i in scores:
        if i>avg:
            value+=1
    result = (value / n) * 100
    print("{:.3f}%".format(result))