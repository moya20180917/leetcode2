arr=[1, 2, 3, 4]
length = len(arr)
visit = [True]*length
temp = ["" for x in range(length)]

def dfs(step):
    if (step==length):
        print(temp)
        return

    for i in range(length):
        if visit[i] == True:
            temp[step] = arr[i]
            visit[i] = False
            dfs(step+1)
            visit[i] = True

dfs(0)