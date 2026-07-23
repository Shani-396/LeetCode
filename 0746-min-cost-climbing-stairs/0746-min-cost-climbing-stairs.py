class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        step_1 = cost[len(cost) - 2]
        step_2 = cost[len(cost) - 1]
        for i in range(len(cost) - 3, -1, -1):
            step_1, step_2 = min(step_1, step_2) + cost[i], step_1
        return min(step_1, step_2)