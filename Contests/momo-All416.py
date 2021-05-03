class Solution:
    def canPartition(self, nums):
        # write code here
        sumList = sum(nums)
        if sumList % 2 != 0: return False
        nums.sort()

        i = 0

        numsLen = len(nums)
        while i < numsLen-1:
            numCount = 1
            j = i+1
            while j < numsLen:
                if nums[j] == nums[i]:
                    numCount += 1
                    j += 1
                else:
                    if numCount % 2 == 0:
                        nums = nums[0:i]+nums[j:]
                        numsLen = len(nums)
                        break
                    else:
                        i += 1
                        break


        if len(nums) == 0: return True
        curSum = 0
        halfSum = sumList / 2
        for i in range(len(nums) - 1):
            curSum += nums[i]
            curSumTmp = curSum
            for j in range(len(nums) - 1, i, -1):

                curSum += nums[j]

                if curSum < halfSum:
                    continue
                elif curSum == halfSum:
                    # 判断
                    if sum(nums[i + 1:j]) == halfSum:
                        return True
                    break
                else:
                    break
            curSum = curSumTmp

        return False

s = Solution()

print(s.canPartition([2,3,2,3,1,1]))
