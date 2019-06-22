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
        res=[]
        def backtrack(combination, next_digits):
            if len(next_digits)==0:
                res.append(combination)

            else:
                for letter in dict[next_digits[0]]:
                    backtrack(combination+letter, next_digits[1:])
                    # print(combination)

        if digits:
            backtrack('',digits)
        return res
if __name__=="__main__":
    s = Solution()
    res = s.letterCombinations('23')
    print(res)