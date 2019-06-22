class Solution:
    def letterCombinations(self,digits):
        dict = {
            '2':list('abc'),
            '3':list('def'),
            '4': list('ghi'),
            '5': list('jkl'),
            '6': list('mno'),
            '7': list('pqrs'),
            '8': list('tuv'),
            '9': list('wxyz'),
        }

        if not digits:
            return []

        res = ['']
        for one in digits:
            res = [x + y for x in res for y in dict[one]]
            print(res)
        # for one in digits:
        #     for y in dict[one]:
        #         for x in res:
        #             res.append(x+y)
        return res
if __name__=="__main__":
    s = Solution()
    res = s.letterCombinations('23')
    print(res)
