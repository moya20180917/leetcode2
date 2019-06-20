class Solution:
    def maxArea(self, height):
        volume = []
        length = len(height)
        for i in range(length):
            for j in range(i+1,length):
                width = min(height[i], height[j])
                chang = j-i
                volume.append(width*chang)
        return max(volume)


if __name__=="__main__":
    s = Solution()
    res,resList = s.maxArea([1,8,6,2,5,4,8,3,7])
    print(res)
    print(resList)

