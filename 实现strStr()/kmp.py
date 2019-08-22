class Solution:
    def strStr(self,haystack, needle):
        if not needle:
            return 0
        _next = [0]*len(needle)

        def getNext(needle, _next):
            _next[0] = -1
            i = 0
            j = -1
            while i < len(needle)-1:
                if j == -1 or needle[i] == needle[j]:
                    i += 1
                    j += 1
                    _next[i] = j
                else:
                    j = _next[j]
        getNext(needle, _next)
        i=0
        j=0
        while i<len(haystack) and j<len(needle):
            if j==-1 or haystack[i]==needle[j]:
                i+=1
                j+=1
            else:
                j = _next[j]
        if j==len(needle):
            return i-j
        return -1

s = Solution()
haystack = "hello"
needle = "ll"
res = s.strStr(haystack, needle)
print(res)

