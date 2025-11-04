nums=[]
for _ in range(9):
    n=int(input())
    nums.append(n)
result1=max(nums)
for i in range(9):
    if nums[i]==result1:
        result2=i+1
print(result1)
print(result2)