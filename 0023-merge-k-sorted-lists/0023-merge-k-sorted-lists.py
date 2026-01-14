# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        for i, list in enumerate(lists):
            if list != None:
                heap.append((list.val, i))
        
        heapq.heapify(heap)
        merge_list = current = ListNode()

        while heap:
            val, i = heapq.heappop(heap)
            current.next = lists[i]
            current = lists[i]
            if lists[i].next != None:
                lists[i] = lists[i].next
                heapq.heappush(heap, (lists[i].val, i))

        return merge_list.next