"""
给你一个字符串 s，找到 s 中最长的回文子串。
示例 1：

输入：s = "babad"
输出："bab"
解释："aba" 同样是符合题意的答案。
示例 2：

输入：s = "cbbd"
输出："bb"
示例 3：

输入：s = "a"
输出："a"
示例 4：

输入：s = "ac"
输出："a"
"""
class Solution:
    def longestPalindrome(self, s):
        mysrtlen = len(s)
        # 字典存储最长找到的回文，最后返回最长
        d = {}
        if mysrtlen == 1:
            return s
        elif mysrtlen == 2:
            if self.mystr(s):
                return s
        else:
            if self.mystr(s):
                return s
        for i in range(mysrtlen):
            for j in range(i + 2, mysrtlen + 1):
                ret = s[i:j]
                if self.mystr(ret):
                    d[len(ret)] = ret
        # 找最长的回文返回
        if len(d) == 0:
            return s[0]
        else:
            return d.get(max(d))

    def mystr(self, mys):
        if mys == mys[::-1]:
            return True
        else:
            return False


s = "aacabdkacaa"
a = Solution()
print(a.longestPalindrome(s))
