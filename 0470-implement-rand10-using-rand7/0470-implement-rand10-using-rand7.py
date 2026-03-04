# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        while True:
            i = rand7()
            j = rand7()
            if (i - 1) * 7 + j <= 40:
                return ((i - 1) * 7 + j) % 10 + 1

        