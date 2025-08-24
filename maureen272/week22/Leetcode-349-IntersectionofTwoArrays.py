class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        answer = [] 
        for i in nums1:
            for j in nums2:
                if i == j:
                    if i not in answer:
                        answer.append(i)
        return answer
                    
        