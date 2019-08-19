def permutation(arr, position, end):
    if position==end:
        print(arr)
    else:
        for i in range(position, end):
            arr[i], arr[position] = arr[position], arr[i]
            permutation(arr, position+1, end)
            arr[position], arr[i] = arr[i], arr[position]


arr = [1,2,3,4]
permutation(arr,0,4)