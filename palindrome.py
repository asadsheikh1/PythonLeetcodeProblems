class Solution:
    def isPalindrome(self, x: int) -> bool:
        temp = x
        reverse = 0
        i = 0

        while (temp > 0):
            digit = temp % 10
            reverse = (reverse * 10) + digit
            temp = temp // 10
            i += 1

        if (reverse == x):
            return True
        return False


app = Solution()
print(app.isPalindrome(121))
