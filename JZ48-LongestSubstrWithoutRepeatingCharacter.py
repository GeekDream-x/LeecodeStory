class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        s = list(s)
        window_dic = {0: [s[0]]}
        max_lens = [0 for _ in range(len(s))]
        max_lens[0] = 1

        for i in range(1, len(s)):

            if s[i] not in window_dic[i - 1]:

                max_lens[i] = max_lens[i - 1] + 1

                window_dic[i] = list(window_dic[i - 1]) + [s[i]]

            else:
                # 在以上一个字符结束的子串中存过当前字符
                # 往前遍历，查到上次出现当前字符的位置，即可得出以当前字符为结束的最长子串
                j = i - 1
                window_dic[i] = []
                while s[j] != s[i]:
                    window_dic[i].append(s[j])
                max_lens[i] = i - j

        return max_lens[-1]


s = Solution()

print(s.lengthOfLongestSubstring("abcabcbb"))