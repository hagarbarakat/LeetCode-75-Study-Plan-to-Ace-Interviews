class Solution:
    def longestPalindrome(self, s: str) -> int:
        hashset = set()
        for c in s:
            if c not in hashset:
                hashset.add(c)
            else:
                hashset.remove(c)
        return len(s) - len(hashset) + 1 if len(hashset) > 0 else len(s)
