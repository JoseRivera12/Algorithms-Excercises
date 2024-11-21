
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # with O(n) space using aux list
        # res = []
        # while head:
        #     res.append(head.val)
        #     head = head.next
        
        # low, high = 0, len(res) - 1
        # while low < high:
        #     if res[low] != res[high]:
        #         return False
        #     low += 1
        #     high -= 1
        # return True
        # constant space reverse linked list two times
        first_half_end = self.findMid(head)
        second_half_start = self.reverseList(first_half_end)

        result = True
        first = head
        second_position = second_half_start
        while result and second_position:
            if first.val != second_position.val:
                result = False
            first = first.next
            second_position = second_position.next

        first_half_end.next = self.reverseList(second_half_start)
        return result
    
    def findMid(self, head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        return slow
    
    def reverseList(self, head):
        prev = None
        current = head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        return prev
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # with O(n) space using aux list
        # res = []
        # while head:
        #     res.append(head.val)
        #     head = head.next
        
        # low, high = 0, len(res) - 1
        # while low < high:
        #     if res[low] != res[high]:
        #         return False
        #     low += 1
        #     high -= 1
        # return True
        # constant space reverse linked list two times
        first_half_end = self.findMid(head)
        second_half_start = self.reverseList(first_half_end)

        result = True
        first = head
        second_position = second_half_start
        while result and second_position:
            if first.val != second_position.val:
                result = False
            first = first.next
            second_position = second_position.next

        first_half_end.next = self.reverseList(second_half_start)
        return result
    
    def findMid(self, head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        return slow
    
    def reverseList(self, head):
        prev = None
        current = head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        return prev
