# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = []
        length = 0
        while head != None:
            node.append(head)
            head = head.next
            length += 1
        return node[length // 2]
        