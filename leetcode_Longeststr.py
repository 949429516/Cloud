"""
给定一个字符串 s ，请你找出其中不含有重复字符的 最长子串 的长度。

示例 1:

输入: s = "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
示例 2:

输入: s = "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
示例 3:

输入: s = "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
示例 4:

输入: s = ""
输出: 0
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = 0
        # 存储值
        middlesave = ''
        # 计算最终的长度
        L = []
        strlen = len(s)
        # 循环遍历
        while n < strlen:
            if s[n] not in middlesave:
                middlesave += s[n]
                n += 1
                L.append(middlesave)
            # 如果有重复则将中间值后移动一个下标，继续while循环，若下次还重复则继续移动
            else:
                # midlesave的顺序和原本s顺序一致
                middlesave = middlesave[1:]
        if s == "":
            return 0
        else:
            return len(max(L, key=len))

s = "kfkv"
a = Solution()
print(a.lengthOfLongestSubstring(s))
