# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        count = 0
        dummy = ListNode()
        dummy2 = ListNode()
        curr = head
        curr2 = head
        
        if not head:
            return false
        
        while curr:
            curr = curr.next
            count += 1
        
        if count == 1:
            return True
        
        iterations = int(count / 2)
        
        for i in range(iterations):
            prev = curr2
            curr2 = curr2.next
            
        prev.next = dummy
        
        dummy2.next = curr2
        
        while curr2:
            temp = curr2.next
            curr2.next = dummy2
            dummy2 = curr2
            curr2 = temp
        
        for i in range(iterations):
            if head.val != dummy2.val:
                return False
            head = head.next
            dummy2 = dummy2.next
        
        return True
        
        
            
            
        
        
        
        
        
            
            
        
        
            
        