class Solution:
    def romanToInt(self, s: str) -> int:
        lookup = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }
        result = 0

        for char in reversed(s):
            if char in lookup.keys():
                num = lookup[char]
                if (num >= lookup[char]):
                    result = result + num
                else:
                    result = result - num
        
        return result


app = Solution()
print(app.romanToInt("MCMXCIV"))


             
             
             
             
             