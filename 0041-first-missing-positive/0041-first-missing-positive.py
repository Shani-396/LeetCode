class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # # Solution 1
        # n = len(nums)
        
        # for x in nums:
        #     num = x
        #     while num != None and 1 <= num <= n:
        #         nums[num - 1], num = None, nums[num - 1]
            
        # for i in range(n):
        #     if nums[i] != None:
        #         return i + 1
        
        # return n + 1

        # Solution 2
        n = len(nums)

        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                target_idx = nums[i] - 1
                nums[i], nums[target_idx] = nums[target_idx], nums[i]

        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        
        return n + 1