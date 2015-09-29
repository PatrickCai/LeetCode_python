class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def firstMissingPositive(self, nums):
        i = 0
        while i < len(nums):
            a_p = nums[i] - 1
            if nums[i] > 0 and nums[i] <= len(nums) and nums[i] != nums[a_p]:
                nums[i], nums[a_p] = nums[a_p], nums[i]
            else:
                i += 1
        print(nums)
        for num, value in enumerate(nums):
            if num + 1 != value:
                return num + 1
        else:
            return len(nums) + 1

nums = [3, 2, 4, -1, 1, 6]
# A = [1, 2, 3]
a = Solution()
print(a.firstMissingPositive(nums))
