# Check if a given number is power of 2

# class Solution:
#     def isPowerOfTwo(self, n: int) -> bool:
      
#       while n%2==0:
#         n//=2

#       return n==1


# Kids With the Greatest Number of Candies 
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        ans = []
        maxCandies = max(candies)

        for i in candies:
            if (i+extraCandies)>=maxCandies:
                ans.append(True)
            else:
                ans.append(False)
        return ans

    