# 1480. Running Sum of 1d Array 

class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        result = []
        total = 0

        for num in nums:
            total += num
            result.append(total)

        return result
        


# 26. Remove Duplicates from Sorted Array 


class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        n = len(nums)
        start =0
        for i in range(1, n):
            if nums[i]!=nums[start]:
                start+=1
                nums[start]=nums[i]
        return start+1