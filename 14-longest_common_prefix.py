"""https://leetcode.com/problems/longest-common-prefix/description/"""

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ""

        prefix = strs[0]
        for string in strs:
            if len(string) < len(prefix):
                prefix = prefix[:len(string)]
            for i, char in enumerate(string):
                if i >= len(prefix):
                    break

                if char != prefix[i]:
                    prefix = prefix[:i]
                    break
            if not prefix:
                break
        return prefix

if __name__ == "__main__":
    sol = Solution()
    strs = ["ab", "ab", "acb"]
    print(sol.longestCommonPrefix(strs))