class Solution:
    def isPalindrome(self, x: int) -> bool:
        string = str(x)
        #print(x)
        y = str(1234)
        t = y[::-1]
        #print(t)
        rev = string[::-1]
        #print (rev)
        if rev == x:
            return 0
        else:
            return 1
