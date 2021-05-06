"""
未知 整数数组 arr 由 n 个非负整数组成。

经编码后变为长度为 n - 1 的另一个整数数组 encoded ，其中 encoded[i] = arr[i] XOR arr[i + 1] 。例如，arr = [1,0,2,1] 经编码后得到 encoded = [1,2,3] 。

给你编码后的数组 encoded 和原数组 arr 的第一个元素 first（arr[0]）。

请解码返回原数组 arr 。可以证明答案存在并且是唯一的。

示例 1：

输入：encoded = [1,2,3], first = 1
输出：[1,0,2,1]
解释：若 arr = [1,0,2,1] ，那么 first = 1 且 encoded = [1 XOR 0, 0 XOR 2, 2 XOR 1] = [1,2,3]
示例 2：

输入：encoded = [6,2,7,3], first = 4
输出：[4,2,0,7,4]

解题思路：
异或^ arr = [1,0,2,1]
1 ^ 0 = 1
0 ^ 2 = 2
2 ^ 1 = 3
encoded = [1,2,3]
反向^就可以得到之前的值,已知列表第一个数值first,实际就是arr列表的最后一个值list[-1]按顺序和encoded列表执行异或操作
"""

class Solution:
    def decode(self, encoded, first):
        myList = [first]
        append = myList.append
        for i in encoded:
            append(myList[-1] ^ i)
        return myList

mysolution = Solution()

print(mysolution.decode(encoded=[6, 2, 7, 3], first=4))
