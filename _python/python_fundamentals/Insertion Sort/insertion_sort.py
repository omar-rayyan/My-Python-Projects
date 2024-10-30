class Solution(object):
    def sortArray(self, nums):
        for i in range(1, len(nums)):
            current = nums[i]
            last_element = i - 1
            while last_element >= 0 and nums[last_element] > current:
                nums[last_element + 1] = nums[last_element]
                last_element -= 1
            nums[last_element + 1] = current
        return nums