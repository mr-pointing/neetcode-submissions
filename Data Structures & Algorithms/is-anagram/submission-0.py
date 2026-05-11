class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_list = {}
        for letter in s:
            if letter not in char_list:
                char_list[letter] = 1
            else:
                char_list[letter] += 1
        char_list2 = {}
        for letter in t:
            if letter not in char_list2:
                char_list2[letter] = 1
            else:
                char_list2[letter] += 1
        return char_list == char_list2