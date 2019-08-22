class Solution:
    def strStr(self, haystack, needle):
        for i in range(len(haystack)-len(needle)+1):
            if haystack[i:i+len(needle)]==needle:
                return i
        return -1
if __name__=="__main__":
    s = Solution()
    haystack = "hello"
    needle = "00"
    res = s.strStr(haystack, needle)
    print(res)