class Solution(object):
    def isPalindrome(self, x):
        # Negative numbers and numbers ending in 0 (except 0 itself) are not palindromes
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        reversed_num = 0
        while x > reversed_num:
            reversed_num = (reversed_num * 10) + (x % 10)
            x //= 10

        # Equal if length is even; drop middle digit if length is odd
        return x == reversed_num or x == reversed_num // 10