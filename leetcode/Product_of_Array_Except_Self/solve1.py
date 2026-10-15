class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        nums = nums
        n = len(nums)
        result = [1]*n

        prefix = 1
        for i in range(n):
            result[i] = prefix
            prefix *= nums[i]

        suffix = 1
        for i in range(n-1,-1,-1):
        #n-1 から初めて、-1の手前まで、－1ずつ。
            result[i] *= suffix
            suffix *= nums[i]

        return result

