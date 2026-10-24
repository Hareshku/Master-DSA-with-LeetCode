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

        