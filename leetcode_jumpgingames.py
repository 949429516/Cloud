"""
给你一个非负整数数组 nums ，你最初位于数组的第一个位置。
数组中的每个元素代表你在该位置可以跳跃的最大长度。
你的目标是使用最少的跳跃次数到达数组的最后一个位置。
假设你总是可以到达数组的最后一个位置。

示例 1:

输入: nums = [2,3,1,1,4]
输出: 2
解释: 跳到最后一个位置的最小跳跃数是 2。
     从下标为 0 跳到下标为 1 的位置，跳 1 步，然后跳 3 步到达数组的最后一个位置。
示例 2:

输入: nums = [2,3,0,1,4]
输出: 2
"""

class Solution:
    def jump(self, nums):
        List_Index_Max = len(nums) - 1
        # 跳跃次数
        JumpSteps = 0
        # 当前最远可以跳跃到的下标位置
        criticalValue_index = 0
        middle_index = 0
        for i in range(List_Index_Max):
            # 当前列表对应下标的值可以跳跃到的位置
            criticalValue_index = max(criticalValue_index, nums[i] + i)
            if i == middle_index:
                middle_index = criticalValue_index
                JumpSteps += 1
        return JumpSteps


nums = [2, 3, 1, 1, 4]
A = Solution()
print(A.jump(nums))
