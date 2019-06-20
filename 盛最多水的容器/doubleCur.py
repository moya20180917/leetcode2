class Solution:
    def maxArea(self, height):

        left = 0
        right = len(height)-1
        area = 0

        while left<right:
            cur = min(height[left],height[right])*(right-left)
            if cur>area:
                area = cur

            if height[left]<height[right]:
                left += 1
            else:
                right-=1
        return area

if __name__=="__main__":
    s = Solution()
    res = s.maxArea([1,8,6,2,5,4,8,3,7])
    print(res)
