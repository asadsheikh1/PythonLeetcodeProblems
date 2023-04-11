class Solution:
    def removeStars(self, s: str) -> str:
        stack = ''

        for char in s:
            if char == '*':
                stack = stack[:-1]
            else:
                stack = stack + char
        return stack


app = Solution()
print(app.removeStars("leet**cod*e"))
