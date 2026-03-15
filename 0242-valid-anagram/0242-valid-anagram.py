class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # # Solution 1
        # if len(s) != len(t):
        #     return False
        # my_dict = {}
        # for char in s:
        #     if char in my_dict:
        #         my_dict[char] +=1
        #     else:
        #         my_dict[char] = 1
        # for char in t:
        #     if char in my_dict and my_dict[char] != 0:
        #         my_dict[char] -= 1
        #     else:
        #         return False
        # return True

        # Solution 2
        return Counter(s) == Counter(t)