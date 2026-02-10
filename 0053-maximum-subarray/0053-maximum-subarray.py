class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currentSum = 0
        maxSum = nums[0]
        for num in nums:
            currentSum = max(currentSum + num, num)
            maxSum = max(maxSum, currentSum)
        return maxSum   