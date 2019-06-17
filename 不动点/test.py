a='11'
b='1'

len1 = len(a)
len2 = len(b)
sum1 = 0
sum2 = 0
for i in range(len1-1):

    sum1 += (int(2**(len-1-i))*int(a[i]))

for j in range(len2-1):
    sum2 += (int(2**(len2-1-j))*int(b[i]))

twoSum = sum1+sum2
binSum = bin(twoSum)[2:]
print(binSum)