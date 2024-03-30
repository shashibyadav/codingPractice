class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val) + ", " + str(self.next)


class PartitionList:
    def print(self, head):
        print()

    def run(self):
        head = ListNode(
            1, ListNode(4, ListNode(3, ListNode(2, ListNode(5, ListNode(2)))))
        )
        x = 3
        first_head = first_p = None
        second_head = second_p = None

        iterator = head

        while iterator is not None:
            if iterator.val < x:
                if first_head is None:
                    first_head = iterator
                    first_p = iterator
                else:
                    first_p.next = iterator
                    first_p = iterator
            else:
                if second_head is None:
                    second_head = iterator
                    second_p = iterator
                else:
                    second_p.next = iterator
                    second_p = iterator
            iterator = iterator.next
            if first_p is not None:
                first_p.next = None
            if second_p is not None:
                second_p.next = None

        first_p.next = second_head
        print(first_p)
