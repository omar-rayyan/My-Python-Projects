class Solution(object):
    def sortArray(self, nums):
        for i in range(len(nums)):
            minimum_value = i
            for x in range(i + 1, len(nums)):
                if nums[x] < nums[minimum_value]:
                    minimum_value = x
            nums[i], nums[minimum_value] = nums[minimum_value], nums[i]
        return nums