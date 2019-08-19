arr = [1,2,3,4,5]
length = len(arr)
visit = [True] * length
temp = ["" for x in range(0, length)]
result = []

def dfs(position):
    if position == length:
        print(temp)
        # result.append(temp)
        return

    for index in range(0, length):
        if visit[index] == True:
            temp[position] = arr[index]
            print("temp",position,temp[position])
            visit[index] = False
            dfs(position + 1)
            visit[index] = True



dfs(0)
print(result)
# print(len(result))
