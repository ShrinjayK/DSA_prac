from typing import Optional
class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        gap_begin = gap_end = dummy = ListNode(0, head)
        for i in range(n + 1):
            gap_end = gap_end.next
        while gap_end:
            gap_begin = gap_begin.next
            gap_end = gap_end.next
        gap_begin.next = gap_begin.next.next
        return dummy.next