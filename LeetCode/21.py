"""iterative"""
def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    dummy = ListNode()  # purpose: val=None, but next=head of merged list
    tail = dummy # to keep track of the last node added to merged list
    while list1 and list2: # while both heads are nontrivial:
        if list1.val > list2.val: # ensure list1.val <= list2.val so i don't have to repeat code
            list1, list2 = list2, list1
        tail.next = list1
        tail = list1
        list1 = list1.next
    # if one of the nodes is trivial:
    # we can just add the other node (if nontrivial) to the tail of the merged list
    # so we'll get the rest of it's 'lineage' as well
    if list1:
        tail.next = list1
    else:
        tail.next = list2
    return dummy.next


"""recursive"""
def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    if not list1 or not list2:
        return list1 if list1 else list2
    else:
        if list1.val > list2.val:
            list1, list2 = list2, list1
        list1.next = self.mergeTwoLists(list1.next, list2)
        return list1