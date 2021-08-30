class Solution(object):
    def divide(self, dividend, divisor):
        ans = 0
        while dividend > divisor:
            a = divisor
            temp = 1
            while (dividend - a) > a:
                a += a
                temp += temp
            ans += temp
            dividend = dividend - a
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.divide(10, 3))
