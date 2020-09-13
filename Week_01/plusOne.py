class Solution:
    def plusOne(self, digits: list) -> list:
        # 1. 把数字转字符串拼接后，再转数字+1 ，得到的数字转成字符串遍历转成数字返回
        # return [int(i) for i in str(int("".join([str(i) for i in digits])) + 1)]

        # 2. 定一个常数，把数字按照数组位数保存，保存后的值 + 1 再转成str，再遍历 str 转成int
        # sums = 0
        # for i in digits:
        #     sums = sums * 10 + i
        # return [i for i in map(int, list(str(sums + 1)))]

        # 3. 通过倒序找 9 ，如果是 9 赋值为 0 ，前一位 +1
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] = digits[i] + 1
                break
            if digits[0] == 0:
                digits.insert(0, 1)
        return digits


if __name__ == '__main__':
    s = Solution()
    # ret = s.plusOne([4, 3, 2, 9, 9])
    ret = s.plusOne([9, 9, 9])
    print(ret)
