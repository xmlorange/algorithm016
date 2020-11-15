# -*- coding: utf-8 -*-
"""
    正则表达式匹配
    1. 递归 + 缓存
    2. 动态规划
"""
import functools


class Solution:

    # 递归
    @functools.lru_cache()
    def isMatch(self, s: str, p: str) -> bool:
        if not p:
            return not s
        first_match = (len(s) > 0 and p[0] in {s[0], '.'})

        # 先处理 *
        if len(p) >= 2 and p[1] == '*':
            # 匹配 0 或者 多个
            return self.isMatch(s, p[2:]) or (first_match and self.isMatch(s[1:], p))

        # 处理 . 匹配一个
        return first_match and self.isMatch(s[1:], p[1:])

    # 动态规划
    def isNewMatch(self, s: str, p: str) -> bool:
        s_len = len(s)
        p_len = len(p)
        memory = {}

        def dp(i, j):
            if (i, j) in memory:
                return memory[(i, j)]
            if j == p_len:
                return i == s_len
            pre = i < s_len and p[j] in {s[i], '.'}

            if j <= p_len - 2 and p[j + 1] == '*':
                tmp = dp(i, j + 2) or pre and dp(i + 1, j)
            else:
                tmp = pre and dp(i + 1, j + 1)
            memory[(i, j)] = tmp
            return tmp

        return dp(0, 0)


if __name__ == '__main__':
    s = 'aaa'
    p = 'a.*'

    ss = Solution()
    print(ss.isMatch(s, p))

    print(ss.isNewMatch(s, p))
