class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        i = 0
        j = 0
        k = -1
        len1 = len(nums1)
        len2 = len(nums2)
        merge = []
        res = -1
        while(i < len1 and j< len2):
            if(nums1[i] <= nums2[j] ):
                merge.append(nums1[i])
                i+=1
                k+=1
            else:
                merge.append(nums2[j])
                j+=1
                k+=1
            if (len1+len2)//2 == k and  (len1+len2)%2 != 0:
                return merge[-1]
            if (len1+len2)//2 == k and  (len1+len2)%2 == 0  :
                return (merge[-1] + merge[-2])/2          
        while(i < len1 ):
            merge.append(nums1[i])
            i+=1
            k+=1 
            if (len1+len2)//2 == k and  (len1+len2)%2 != 0:
                return merge[-1]
            if (len1+len2)//2 == k and  (len1+len2)%2 == 0  :
                return (merge[-1] + merge[-2])/2 
        while(j < len2 ):
            merge.append(nums2[j])
            j+=1
            k+=1 
            if (len1+len2)//2 == k and  (len1+len2)%2 != 0:
                return merge[-1]
            if (len1+len2)//2 == k and  (len1+len2)%2 == 0  :
                return (merge[-1] + merge[-2])/2     
            