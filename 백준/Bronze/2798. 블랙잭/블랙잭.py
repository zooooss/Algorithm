from itertools import combinations

num, aim = map(int, input().split())
array1 = map(int,input().split())

array2 = [sum(comb) for comb in combinations(array1, 3)]
array2.sort(reverse=True)

result = 0
for n in array2:
    if n <= aim:
        result = n
        break
print(result)