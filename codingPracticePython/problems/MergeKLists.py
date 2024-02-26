import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class MergeKLists:

    def run(self):
        lists = []
        min_heap = []

        for link_l in lists:
            temp = link_l
            while temp != None:
                heapq.heappush(min_heap, temp.val)
                temp = temp.next

        result = temp = None

        while len(min_heap) > 0:
            poped = heapq.heappop(min_heap)
            temp2 = ListNode(val=poped)
            if result is None:
                result = temp2
                temp = temp2
            else:
                temp.next = temp2
                temp = temp2
        print(result)
        return result