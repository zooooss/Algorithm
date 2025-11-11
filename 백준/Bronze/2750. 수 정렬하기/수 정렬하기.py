num = int(input())
arr=[]
for _ in range(num):
    numbers=int(input())
    arr.append(numbers)
for i in range(num):
    for j in range(i+1,num):
        if(arr[i]>arr[j]):
            arr[i],arr[j]=arr[j],arr[i]
for i in range(num):
    print(arr[i])