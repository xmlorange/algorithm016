from typing import List


class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        # 1. DP
        # n = len(nums)
        # f = [[10 ** 18] * (m + 1) for _ in range(n + 1)]
        # sub = [0]
        # for i in nums:
        #     sub.append(sub[-1] + i)
        #
        # f[0][0] = 0
        # for i in range(1, n + 1):
        #     for j in range(1, min(i, m) + 1):
        #         for k in range(i):
        #             f[i][j] = min(f[i][j], max(f[k][j - 1], sub[i] - sub[k]))
        # return f[n][m]

        # 2. 二分查找
        def check(x):
            total, cnt = 0, 1
            for num in nums:
                if total + num > x:
                    cnt += 1
                    total = num
                else:
                    total += num
            return cnt <= m

        left, right = max(nums), sum(nums)
        while left < right:
            mid = (left + right) // 2
            if check(mid):
                right = mid
            else:
                left = mid + 1
        return left


if __name__ == '__main__':
    s = Solution()
    print(s.splitArray([7, 2, 5, 10, 8], 2))
