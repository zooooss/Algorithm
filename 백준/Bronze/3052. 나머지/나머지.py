numbers = []
for _ in range(10):
    n = int(input())
    numbers.append(n)
    
for i in range(10):
    numbers[i]=numbers[i]%42

result = set(numbers)
print(len(result))