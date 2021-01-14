# 1 自己 字典记录以每个位置结尾的子串的所有字符
# 520/45  5/5
# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         if not s : return 0
#         s = list(s)
#         window_dic = {0: [s[0]]}
#         max_lens = [0 for _ in range(len(s))]
#         max_lens[0] = 1

#         for i in range(1, len(s)):

#             if s[i] not in window_dic[i - 1]:

#                 max_lens[i] = max_lens[i - 1] + 1

#                 window_dic[i] = list(window_dic[i - 1]) + [s[i]]

#             else:
#                 # 在以上一个字符结束的子串中存过当前字符
#                 # 往前遍历，查到上次出现当前字符的位置，即可得出以当前字符为结束的最长子串
#                 j = i - 1
#                 window_dic[i] = [s[i]]
#                 while s[j] != s[i]:
#                     window_dic[i].append(s[j])
#                     j -= 1
#                 max_lens[i] = i - j

#         return max(max_lens)


# 2 一个字典存储对应字符上一次出现的索引
# 108/15 16/5
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s: return 0

        s = list(s)
        char_pre_idx = {}
        pre_max_len = 1
        char_pre_idx[s[0]] = 0

        max_len = 1

        for i in range(1, len(s)):
            if s[i] not in list(char_pre_idx.keys()):
                # 之前没出现过
                pre_max_len += 1

            else:
                # 之前出现过
                if (i - char_pre_idx[s[i]]) > pre_max_len:
                    # 当前字符上一次不出现在以前一个字符为结束的最长子串中
                    pre_max_len += 1
                else:
                    pre_max_len = i - char_pre_idx[s[i]]

            if max_len < pre_max_len:
                max_len = pre_max_len
                # 不管之前出没出现过，都要更新最新出现位置
            char_pre_idx[s[i]] = i

        return max_len

s = Solution()

print(s.lengthOfLongestSubstring("bbbbb"))