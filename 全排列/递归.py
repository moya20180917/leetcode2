import itertools
result = []
def permutation(arr, position, end):
    if(position==end):
        print(arr)
        result.append(arr)
    else:
        for i in range(position, end):
            arr[i], arr[position] = arr[position], arr[i]
            permutation(arr, position+1, end)
            arr[i], arr[position] = arr[position], arr[i]


arr = ["a","b","c","d"]
permutation(arr, 0, 2)
print(result)


s=[1,2,3]
resultList = list(itertools.permutations(s))
print(resultList)