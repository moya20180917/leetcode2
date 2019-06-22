class Solution:
    def letterCombinations(self,digits):
        dict={'2':['a','b','c'],'3':['d','e','f'],'4':['g','h','i'],'5':['j','k','l'],'6':['m','n','o'],'7':['p','q','r','s'],'8':['t','u','v'],'9':['w','x','y','z']}
        res=[]
        value=[]
        for i in range(len(digits)):
            if digits[i] != '1':
                tmp = dict[digits[i]]
                value.append(tmp)

        if len(digits)==1:
            return dict[digits[0]]
        for i in range(len(value)):
            for j in range(i+1, len(value)):
                for m in range(len(value[i])):
                    for n in range(len(value[j])):
                        res.append(value[i][m]+value[j][n])

        # res = list(set(res))
        return res

if __name__=="__main__":
    s = Solution()
    res = s.letterCombinations('234')
    print(res)

