from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(first=0):
            if first == n:
                res.append(nums[:])
            for i in range(first, n):
                # 动态维护数组
                nums[first], nums[i] = nums[i], nums[first]

                # 继续递归填充下一个数
                backtrack(first + 1)

                # 撤销操作
                nums[first], nums[i] = nums[i], nums[first]

        n = len(nums)
        backtrack()
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.permute([1, 2, 3]))
