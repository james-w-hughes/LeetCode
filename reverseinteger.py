class Solution:
    def reverse(self, x: int) -> int:
       

        if (x >= 0) and (x <= (2**31 - 1)):
            sign = 1
            stringx = str(abs(x))
            rev = stringx[::-1]
            y = int(rev)
            
        
            answer = y
            if (answer >= (2**31 - 1)):
                return 0
            else:
                return answer
        elif (x <= 0) and (x >= -((2**31) + 1) ):
            stringx = str(abs(x))
            rev = stringx[::-1]
            y = int(rev)
        
            answer = (-y)
            if (answer <= -(2**31 - 1)):
                return 0
            else:
                return answer
        else:
            return 0
        
