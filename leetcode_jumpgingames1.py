"""
给定一个非负整数数组 nums ，你最初位于数组的第一个下标 。
数组中的每个元素代表你在该位置可以跳跃的最大长度。
判断你是否能够到达最后一个下标。

示例 1：
输入：nums = [2,3,1,1,4]
输出：true
解释：可以先跳 1 步，从下标 0 到达下标 1, 然后再从下标 1 跳 3 步到达最后一个下标。
示例 2：
输入：nums = [3,2,1,0,4]
输出：false
解释：无论怎样，总会到达下标为3的位置。但该下标的最大跳跃长度是0， 所以永远不可能到达最后一个下标。
"""


class Solution:
    def canJump(self, nums):
        max_index = len(nums) - 1
        current_index = 0
        for index, listnumber in enumerate(nums):
            indexsum = index + listnumber
            if current_index >= index and indexsum > current_index:
                current_index = indexsum
                if current_index > max_index:
                    return True
        return current_index >= index
nums = [3,2,1,0,4]
A = Solution()
print(A.canJump(nums))

"""
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        cover = 0
        if len(nums) == 1:
            return True
        i = 0
        while i <= cover:
            cover = max(i + nums[i], cover)
            if cover >= len(nums) - 1:
                return True
            i += 1
        return False
"""