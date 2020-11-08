from typing import List
from collections import Counter


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        # 1. 自定义排序
        # return sorted(arr1, key=lambda x: (0, arr2.index(x)) if x in arr2 else (1, x))

        # 2. 利用哈希
        # 对 arr1 进行计数 生成map
        new_list = []
        counter = Counter(arr1)
        for val in arr2:
            if val in counter:
                cnt = counter.get(val)
                for _ in range(cnt):
                    new_list.append(val)
            # 被存的元素删除掉
            del counter[val]
        # 剩下的元素排序放到末尾
        new_list += sorted(list(counter.elements()))
        return new_list


if __name__ == '__main__':
    arr1 = [2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19]
    arr2 = [2, 1, 4, 3, 9, 6]
    s = Solution()
    print(s.relativeSortArray(arr1, arr2))



