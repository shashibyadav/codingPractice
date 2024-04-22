class Solution:
    def helper(self, nums1, start1, end1, nums2, start2, end2):
        if start1 == end1:
            median1 = nums1[start1]
            sub = end2 - start2
            med_index2 = start2 + (sub // 2)
            length = sub + 1
            median2 = (
                nums2[med_index2]
                if length % 2 != 0
                else (nums2[med_index2] + nums2[med_index2 + 1]) / 2
            )
            return (median1 + median2) / 2
        if start2 == end2:
            median2 = nums2[start2]
            sub = end1 - start1
            med_index1 = start1 + (sub // 2)
            length = sub + 1
            median1 = (
                nums1[med_index1]
                if length % 2 != 0
                else (nums1[med_index1] + nums1[med_index1 + 1]) / 2
            )
            return (median1 + median2) / 2

        med_index1 = start1 + (end1 - start1) // 2
        med_index2 = start2 + (end2 - start2) // 2
        median1 = nums1[med_index1]
        median2 = nums2[med_index2]
        if median1 == median2:
            return median1
        elif median1 > median2:
            return self.helper(nums1, start1, med_index1, nums2, med_index2, end2)
        else:
            return self.helper(nums1, med_index1, end1, nums2, start2, med_index2)

    def findMedianSortedArrays(self, nums1, nums2):
        start1 = 0
        start2 = 0
        end1 = len(nums1) - 1
        end2 = len(nums2) - 1
        return self.helper(nums1, start1, end1, nums2, start2, end2)


nums1 = [1, 2]
nums2 = [3, 4]

print(Solution().findMedianSortedArrays(nums1, nums2))
