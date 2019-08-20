class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        l = 0
        r = 0
        result=[]
        length1 = len(nums1)
        length2 = len(nums2)
        while(l<length1 and r<length2):
            if nums1[l]<nums2[r]:
                result.append(nums1[l])
                l+=1
            else:
                result.append(nums2[r])
                r+=1
        result+=nums1[l:]
        result+=nums2[r:]
        print(result)

        length3 = len(result)
        print(length3)
        if length3%2==0:
            median = (result[(int)(length3/2)]+result[(int)((length3/2)-1)])/2
        else:
            median = result[length3//2]
        return median


if __name__=="__main__":
    s = Solution()
    arr1 = [1,2]
    arr2 = [3,4]
    median = s.findMedianSortedArrays(arr1,arr2)
    print(median)