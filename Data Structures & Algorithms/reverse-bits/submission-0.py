class Solution:
    def reverseBits(self, n: int) -> int:
        print(5 ^ 2 )
        result = 0 
        for i in range(32):
            num =  n & 1 
            result = (result << 1) | num 
            n >>= 1
            

        return result            
