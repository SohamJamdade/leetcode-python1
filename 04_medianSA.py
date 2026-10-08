class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):

        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m = len(nums1)
        n = len(nums2)

        half =(m + n + 1) //2

        left = 0
        right = m  

        while left <= right:

            partition1 = (left + right) //2

            partition2 = half - partition1     
            

            left1 = float('-inf') if partition1  == 0 else nums1[ partition1 - 1]
            right1 = float('inf') if partition1  == m else nums1[ partition1]

            left2 = float('-inf') if partition2 == 0 else nums2[partition2 - 1]
            right2 = float('inf') if partition2 == n else nums2[partition2]


            if left1 <= right2 and left2 <= right1 :


                if (m + n) % 2 == 1:
                    return max(left1 ,left2)

                return (max(left1, left2) + min(right1, right2 )) / 2.00

            elif left1 > right2:
                right = partition1 - 1

            else : 
                left = partition1 + 1         

# So here we are doing a binary search on the smaller array to find the correct partition point.
# The goal is to ensure that all elements on the left side of the partition are less than or equal to all elements on the right side.
#
# Binary Search Partition:
#
# 1. Binary search smaller array.
# 2. leftSize = (m+n+1)//2
# 3. partition2 = leftSize - partition1
# 4. Get:
#        left1, right1
#        left2, right2
# 5. Valid partition:
#        left1 <= right2
#        left2 <= right1
# 6. Odd:
#        max(left1,left2)
# 7. Even:
#        (max(left1,left2) + min(right1,right2)) / 2
# 8. If left1 > right2 -> move partition LEFT
#    Else              -> move partition RIGHT
#
# No merging.
# Time: O(log(min(m,n)))
# Space: O(1)
   