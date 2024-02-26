class FindMedianSortedArrays:

    def findMedian(self, arr1, arr2, start1, end1, start2, end2):
        mid1 = int((start1 + end1) / 2)
        mid2 = int((start2 + end2) / 2)
        length1 = end1 - start1 + 1
        length2 = end2 - start2 + 1
        isEven1 = length1 % 2 == 0
        isEven2 = length2 % 2 == 0
        if length1 == 1 and length2 == 1:
            return (arr1[mid1] + arr2[mid2]) / 2
        if start1 > end1:
            if isEven2:
                return (arr2[mid2] + arr2[mid2 + 1]) / 2
            else:
                return arr2[mid2]
        if start2 > end2:
            if isEven1:
                return (arr1[mid1] + arr1[mid1 + 1]) / 2
            else:
                return arr1[mid1]

        median1 = (arr1[mid1] + arr1[mid1 + 1]) / 2 if isEven1 else arr1[mid1]
        median2 = (arr2[mid2] + arr2[mid2 + 1]) / 2 if isEven2 else arr2[mid2]

        if median1 < median2:
            return self.findMedian(arr1, arr2, mid1 + 1 if isEven1 else mid1, end1, start2, mid2 if isEven2 else mid2 - 1)
        elif median1 > median2:
            return self.findMedian(arr1, arr2, start1, mid1 if isEven1 else mid1 - 1, mid2 + 1 if isEven2 else mid2, end2)
        else:
            return median1
    def run(self):
        # nums1 = [1,3]
        # nums2 = [2]
        # nums1 = [1,2]
        # nums2 = [3,4]
        nums1 = [1,2]
        nums2 = [-1,3]
        print(self.findMedian(nums1, nums2, 0, len(nums1) - 1, 0, len(nums2) - 1))
        # return self.findMedian(nums1, nums2)

