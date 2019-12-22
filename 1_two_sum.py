class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        c = len(nums)

        if c <= 1:
            return None

        for i in range(0, c):
            num_2 = target - nums[i]
            try:
                index_2 = nums.index(num_2)
                if index_2 != i:
                    return [i, index_2]
            except:
                continue
        return None