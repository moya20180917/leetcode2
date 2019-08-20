def median(arr1, arr2):
    m, n = len(arr1), len(arr2)
    if m>n:
        arr1, arr2, m, n = arr2, arr1, n, m
    if n==0:
        raise ValueError

    imin, imax, half = 0, m, (m+n+1)//2
    #pay attention that should be less and equal than imax
    while imin<=imax:
        i = (imin+imax)//2
        j = half-i
        if i<m and arr2[j-1]>arr1[i]:
            # i is too small, should increase
            imin = i+1
        elif i>0 and arr1[i-1]>arr2[j]:
            # i is too large, should decrease
            imax = i-1
        else:
            # i is perfect
            #先选择左边的最大值
            if i==0:
                max_of_left = arr2[j-1]
            elif j==0:
                max_of_left = arr1[i-1]
            else:
                max_of_left = max(arr1[i-1],arr2[j-1])

            if (m+n)%2==1:
                return max_of_left

            if i==m:
                min_of_right = arr2[j]
            elif j==n:
                min_of_right = arr1[i]
            else:
                min_of_right = min(arr1[i],arr2[j])

            return (max_of_left+min_of_right)/2.0

if __name__=="__main__":
    A=[1,2,3]
    B=[4,5,6]
    med = median(A,B)
    print(med)