class  Solution:
    def generateParenthesis(self,n):
        if n == 0:
            return []
        total_list = []
        total_list.append([None])
        total_list.append(["()"])
        # print(total_list)
        for i in range(2,n+1):
            l = []
            for j in range(i):
                now_list1= total_list[j]
                print("now_list1:",now_list1)
                now_list2 = total_list[i-1-j]
                print("now_list1:", now_list2)
                for k1 in now_list1:
                    for k2 in now_list2:
                        if k1 == None:
                            k1 = ""
                        if k2 == None:
                            k2 = ""
                        el = "("+k1+")"+k2
                        print("el",el)
                        l.append(el)
            total_list.append(l)
        return total_list[n]



if __name__=="__main__":
    s = Solution()
    res = s.generateParenthesis(2)
    print(res)