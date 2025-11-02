word = input()
alphabet = "abcdefghijklmnopqrstuvwxyz"
result = [-1] * 26

for i in range(len(word)):
    index = ord(word[i])-ord('a')
    if result[index]==-1:
        result[index]=i

print(*result)