class Solution(object):
    def findContentChildren(self, g: list, s: list):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        # 贪心算法
        g.sort()
        s.sort()
        res = 0

        i = j = 0
        g_len = len(g)
        s_len = len(s)

        while i < g_len and j < s_len:
            # 满足胃口 下一个小朋友
            if g[i] <= s[j]:
                res += 1

                i += 1
                j += 1
            # 不满足 下一块饼干
            else:
                j += 1
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.findContentChildren([1, 2, 3], [1, 1]))
