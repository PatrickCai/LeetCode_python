class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        first = 0
        last = len(nums) - 1
        while first < last:
            middle = (first + last) / 2
            if (nums[middle] == target):
                return middle
            elif target > nums[middle]:
                first = middle + 1
            elif target < nums[middle]:
                last = middle - 1
        else:
            if target > nums[first]:
                return first + 1
            else:
                return first
dd = [1, 3, 5, 6]
a = Solution()
print(a.searchInsert(dd, 5))
