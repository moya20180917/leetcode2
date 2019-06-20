# class Solution:
#     def uncommonFromSentences(self,a,b):
#         list_a = a.split()
#         list_b = b.split()
#         res_list1=[]
#         for item in list_b:
#             if item not in list_a:
#                 res_list1.append(item)
#
#         res_list2 = []
#         for item in list_a:
#             if item not in list_b:
#                 res_list2.append(item)
#         res=[]
#         for one in res_list1:
#             res.append(one)
#         for one in res_list2:
#             res.append(one)
#
#         return list(set(res))

class Solution:
    def uncommonFromSentences(self,a,b):
        list_a = a.split()
        list_b = b.split()
        dict1 = {}
        for one in list_a:
            if one not in dict1.keys():
                dict1[one] = 1
            else:
                dict1[one] += 1

        for one in list_b:
            if one not in dict1.keys():
                dict1[one] = 1
            else:
                dict1[one] += 1

        res = []
        for key,value in dict1.items():
            if value==1:
                res.append(key)
        return res


if __name__ == "__main__":
    s = Solution()
    res = s.uncommonFromSentences("this apple is sweet","this apple is sour")
    #"this apple is sweet","this apple is sour"
    #"apple apple","banana"
    print(res)