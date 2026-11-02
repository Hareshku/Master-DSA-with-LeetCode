# 1. Two Sum

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        n =len(nums)
        dict1= {}
        
        for i in range(n):
            rem = target-nums[i]
            if rem in dict1:
                return [dict1[rem], i]
            dict1[nums[i]]=i





# 349. Intersection of Two Arrays

class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        set1 = set(nums1)
        set2 = set(nums2)

        return list(set1&set2)