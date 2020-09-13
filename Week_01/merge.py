class Solution:
    def merge(self, nums1: list, m: int, nums2: list, n: int) -> None:

        """
            Do not return anything, modify nums1 in-place instead.
        """
        # 1. 最粗暴的方式
        nums1[:] = sorted(nums1[:m] + nums2)

        # 2. 双指针
        while n:
            if m == 0:
                nums1[n - 1] = nums2[n - 1]
                n -= 1
                continue
            if nums1[m - 1] < nums2[n - 1]:
                nums1[m + n - 1] = nums2[n - 1]
                n -= 1
            else:
                nums1[m + n - 1] = nums1[m - 1]
                m -= 1


if __name__ == '__main__':
    nums1 = [1, 2, 3, 0, 0, 0]
    nums2 = [2, 5, 6]
    s = Solution()
    s.merge(nums1, 3, nums2, 3)
