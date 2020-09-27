from typing import List
import itertools


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # 1. 工具类实现
        # return [list(i) for i in itertools.combinations(range(1, n + 1), k)]
        # return list(itertools.combinations(range(1, n + 1), k))

        # 2. 递归
        # k如果等于2就是两层循环，第二层循环的起始就是上一层的数+1
        if not k:
            return []
        if k == 1:
            return [[i] for i in range(1, n + 1)]
        res = []

        def helper(up, depth):
            if depth == k:
                res.append(up)
                return
            for i in range(up[-1] + 1, n + 2 + depth - k):
                helper(up + [i], depth + 1)

        for i in range(1, n + 2 - k):
            helper([i], 1)
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.combine(4, 2))
