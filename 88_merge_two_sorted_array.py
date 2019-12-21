class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        j = 0
        for i in range(m, m + n):
            nums1.insert(m, nums2[j])
            j = j + 1

        nums1[:] = nums1[: m + n]
        nums1.sort()


if __name__ == "__main__":
    num1 = [1, 2, 3, 0, 0, 0]
    n1 = 3
    num2 = [2, 5, 6]
    n2 = 3

    s = Solution()
    s.merge(num1, n1, num2, n2)
    print(num1)
