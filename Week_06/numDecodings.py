class Solution:
    def numDecodings(self, s: str) -> int:
        size = len(s)
        if size == 0:
            return 0
        dp = [0] * (size + 1)
        dp[0] = 1

        for i in range(1, size + 1):
            t = int(s[i - 1])
            if 1 <= t <= 9:
                # 最后一个数字解密成一个字母
                dp[i] += dp[i - 1]
            if i >= 2:
                # 至少要两个字符
                t = int(s[i - 2]) * 10 + int(s[i - 1])
                if 10 <= t <= 26:
                    dp[i] += dp[i - 2]
        return dp[-1]


if __name__ == '__main__':
    s = Solution()
    print(s.numDecodings('226'))
