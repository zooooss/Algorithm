from itertools import combinations

arr=[int(input()) for _ in range(9)]
for comb in combinations(arr, 7):
    if sum(comb) == 100:
        result = sorted(comb)
        break
for n in result:
    print(n)