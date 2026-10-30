# 2520. Count the Digits That Divide a Number


class Solution:
    def countDigits(self, num: int) -> int:

        temp = num
        count =0
        while temp>0:
            r = temp%10
            if num %r==0:
                count+=1
            temp//=10
        return count


        
# 1365. How Many Numbers Are Smaller Than the Current Number

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:

        ans = []

        for i in nums:
            counter =0
            
            for j in nums:
                if j<i:
                    counter+=1
            ans.append(counter)

        return ans

        

# 9. Palindrome number 

class Solution:
    def isPalindrome(self, x: int) -> bool:
        temp = x
        reverse =0

        while temp>0:
            r = temp%10
            reverse = reverse*10+r
            temp//=10

        return reverse==x



# 1281. Subtract the Product and Sum of Digits of an Integer
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        sum_ =0
        product= 1

        while n >0:
            r = n%10
            sum_ += r
            product *=r

            n//=10

        return product- sum_
        


# 7. Reverse Integer

class Solution:
    def reverse(self, x: int) -> int:
        reverse =0
        while x>0:
            r = x%10
            reverse= reverse*10+r
            x//=10
        return reverse
        