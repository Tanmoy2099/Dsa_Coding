class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        nums1.extend(nums2)
        nums1.sort()
        
        mid = len(nums1)//2
        if (len(nums1)&1)==0:
            return (nums1[mid] + nums1[mid-1])/2
        return nums1[mid]/1


answer = Solution()
nums1 = [1,3]

nums2 = [2,7]

print(answer.findMedianSortedArrays(nums1, nums2))

nums1.extend(nums2)
print(nums1)