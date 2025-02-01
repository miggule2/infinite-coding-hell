class Solution(object):
    def mergeTwoLists(self, list1, list2):
        lst1 = list1
        lst2 = list2
        if (not lst1) or (lst2 and lst1.val > lst2.val):
            lst1,lst2 = lst2, lst1
        if lst1:
            lst1.next = self.mergeTwoLists(lst1.next, lst2)
        return lst1
        