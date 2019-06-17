class Solution:
    def addBinary(self,a,b):
        return bin(int(a,2)+int(b,2))[2:]




if __name__=="__main__":
    s = Solution()
    res = s.addBinary('11','1')
    print(res)