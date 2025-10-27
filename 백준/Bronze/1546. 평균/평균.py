num = int(input())
a = list(map(int,input().split()))

max_score = max(a)

for i in range(num):
    a[i] = a[i] / max_score * 100
    
total = sum(a) / num
print(total)