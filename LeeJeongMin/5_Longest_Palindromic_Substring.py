class Solution:
    def longestPalindrome(self, s: str) -> str:
        # 문자열이 주어지고 그 안에서 가장 긴 팰린드롬을 출력하라

        # This dictionary keeps track of each unique letter in s and the index it last
        # appeared at.
        letter_to_index = {}
        max_length = 0

        # This pointer marks the beginning of the current substring without
        # repeating characters in s. It should never move backwards.
        substr_begin = 0

        # For each char c in s, if c is in the dict, move the substring beginning
        # pointer forward to the index after the one where c was last at. Put c and
        # the current index into the dict and update the length of the longest substring
        # without repeating chars along the way.
        for i, c in enumerate(s):
            if c in letter_to_index:
                substr_begin = max(letter_to_index[c] + 1, substr_begin)
            letter_to_index[c] = i
            max_length = max(max_length, i + 1 - substr_begin)

        return max_length


s = Solution()
print(s.longestPalindrome("babad"))
# print(s.longestPalin고rome("cbbd"))
