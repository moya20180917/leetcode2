arr = [1,2,3,4]
length = len(arr)
visit = [True] * length
temp = ["" for x in range(0, length)]
result = []
count = 0

def dfs(position):
    if position == length:
        print(temp)
        # count = count + 1
        # result.append(temp)
        return

    for index in range(0, length):
        if visit[index] == True:
            temp[position] = arr[index]
            print("temp",position,temp[position],'index', index)

            visit[index] = False
            dfs(position + 1)
            visit[index] = True



dfs(0)
# print(result)
# print(len(result))
