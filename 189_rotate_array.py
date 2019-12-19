class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        assert isinstance(nums, list)
        len_array = len(nums)

        if k > len_array:
            k = k % len_array

        nums[:] = nums[-k:] + nums[:-k]

        return nums

class Solution1(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        assert isinstance(nums, list)
        len_array = len(nums)

        if k > len_array:
            k = k % len_array

        for i in range(k):
            nums.insert(0, nums[-1])
            nums.pop()

        return nums
