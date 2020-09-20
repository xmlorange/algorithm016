class Solution:
    def groupAnagrams(self, strs: list) -> list:
        hash_map = {}

        for i in strs:
            tmp = "".join(sorted(i))

            if tmp in hash_map:
                hash_map.get(tmp, []).append(i)
            else:
                hash_map[tmp] = [i]
        return list(hash_map.values())


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    s = Solution()
    print(s.groupAnagrams(strs=["eat", "tea", "tan", "ate", "nat", "bat"]))
