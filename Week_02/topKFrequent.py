# 给定一个非空的整数数组，返回其中出现频率前 k 高的元素。
#
#
#
#  示例 1:
#
#  输入: nums = [1,1,1,2,2,3], k = 2
# 输出: [1,2]
#
#
#  示例 2:
#
#  输入: nums = [1], k = 1
# 输出: [1]
#
#
#
#  提示：
#
#
#  你可以假设给定的 k 总是合理的，且 1 ≤ k ≤ 数组中不相同的元素的个数。
#  你的算法的时间复杂度必须优于 O(n log n) , n 是数组的大小。
#  题目数据保证答案唯一，换句话说，数组中前 k 个高频元素的集合是唯一的。
#  你可以按任意顺序返回答案。
#
#  Related Topics 堆 哈希表
#  👍 520 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def topKFrequent(self, nums: list, k: int) -> list:
        # 1. 利用python自带的计数器，调用most_common方法
        # from collections import Counter
        # return [e[0] for e in Counter(nums).most_common(k)]

        # 2. 利用dict 模拟哈希统计词频，对产生的dictionary 的 value 进行升序，返回前 K 个key
        hash_map = {}

        for i in nums:
            if i in hash_map:
                hash_map[i] = hash_map.get(i, 0) + 1
            else:
                hash_map[i] = 1
        return [i[0] for i in sorted(hash_map.items(), key=lambda x: x[1], reverse=True)[:k]]

    # leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    s = Solution()
    print(s.topKFrequent([4, 1, -1, 2, -1, 2, 3], 2))
