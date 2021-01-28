# 1 自己 字典记录以每个位置结尾的子串的所有字符   动态规划 + 线性遍历
# 520/45  5/5
# 时间复杂度 O(N^2):其中 N 为字符串长度，动态规划需遍历计算 dp 列表，占用 O(N),每轮计算dp[j]时搜索i需要遍历j个字符，占用 O(N)


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


# 2 自己 动态规划+哈希表   一个字典存储对应字符上一次出现的索引
# 108/15 16/5
# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         if not s: return 0


#         s = list(s)
#         char_pre_idx = {s[0]:0}

#         pre_max_len, max_len = 1, 1


#         for i in range(1, len(s)):
#             if s[i] not in list(char_pre_idx.keys()) or (i - char_pre_idx[s[i]]) > pre_max_len:
#                 # 之前没出现过 或 当前字符上一次不出现在以前一个字符为结束的最长子串中
#                 pre_max_len += 1

#             else:
#                 # 之前出现在以上一个字符结尾的最长子串中
#                 pre_max_len = i - char_pre_idx[s[i]]

#             max_len = max(max_len, pre_max_len)
#             # 不管之前出没出现过，都要更新最新出现位置
#             char_pre_idx[s[i]] = i

#         return max_len

# 3 大佬 动态规划+哈希表
# 时间复杂度 O(N)： 其中 N 为字符串长度，动态规划需遍历计算 dp 列表。
# 空间复杂度 O(1)： 字符的 ASCII 码范围为 0 ~ 127 ，哈希表 dic 最多使用 O(128)=O(1) 大小的额外空间。

# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         dic = {}
#         res = tmp = 0
#         for j in range(len(s)):
#             i = dic.get(s[j], -1) # 获取索引 i
#             dic[s[j]] = j # 更新哈希表
#             tmp = tmp + 1 if tmp < j - i else j - i # dp[j - 1] -> dp[j]
#             res = max(res, tmp) # max(dp[j - 1], dp[j])
#         return res


# 4 自己 双指针  60/15  93/5
# 时间复杂度：O(n^2)空间复杂度：O(1)，使用了 head，tail，res。
# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         if not s : return 0
#         head, tail, max_len = 0, 1, 1

#         while tail < len(s):
#             if s[tail] in s[head:tail]:
#                 while s[head] != s[tail]:
#                     head += 1
#                 head += 1

#             tail += 1 # 保证tail永远指向window最后一个字符的下一个字符

#             #本来tail是包含在当前window的，但是包含进去之后
#             max_len = max(max_len, tail-head)


#         return max_len


# 5  双指针+哈希表  64/14.7  84/32
# 时间复杂度：O(n)，遍历了一遍 s，哈希表中查找的时间复杂度为O(1)。
# 空间复杂度：O(n)，使用了哈希表。


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2: return len(s)
        head, tail, max_len, hashmap = 0, 0, 1, {}

        while tail < len(s):
            if s[tail] in hashmap:
                # !!!
                head = max(hashmap[s[tail]] + 1, head)
            max_len = max(max_len, tail - head + 1)
            hashmap[s[tail]] = tail
            tail += 1

        return max_len


















