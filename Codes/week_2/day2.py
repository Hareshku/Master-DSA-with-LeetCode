# Recursion

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # Base Case 
        if n<=0:
            return False
        if n== 1:
            return True
        if n%2!= 0:
            return False
        
        return self.isPowerOfTwo(n//2)


class Solution:
    def fib(self, n: int) -> int:

        # base case 
        if n == 0 or n==1:
            return n
        # recursive case
        return self.fib(n-1)+self.fib(n-2)


class Solution:
    def findPow(self, x, n):
        # Base case 
        if n ==0:
            return 1
        
        # Recursive case 
        a = self.findPow(x, n//2)
        if n%2== 0:
            return a *a
        else:
            return a*a*x
    def myPow(self, x: float, n: int)-> float:
        if n>=0:
            return self.findPow(x,n)
        else:
            return 1/self.findPow(x, n*(-1))