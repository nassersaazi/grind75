
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(list1, list2):
    """
    Merges two sorted linked lists into one sorted linked list.

    Args:
        list1 (ListNode): The head of the first sorted linked list.
        list2 (ListNode): The head of the second sorted linked list.

    Returns:
        ListNode: The head of the merged sorted linked list.
    """
    # Create a dummy node to start the merged list.
    dummy = ListNode()
    # Create a tail pointer to track the last node in the merged list.
    tail = dummy

    # Iterate until one of the lists is exhausted.
    while list1 and list2:
        # Compare the values of the current nodes in both lists.
        if list1.val < list2.val:
            # If the current node in list1 has a smaller value,
            # append it to the merged list and move to the next node in list1.
            tail.next = list1
            list1 = list1.next
        else:
            # Otherwise, append the current node in list2 to the merged list
            # and move to the next node in list2.
            tail.next = list2
            list2 = list2.next
        # Move the tail pointer to the newly added node.
        tail = tail.next

    # Append the remaining nodes from the non-empty list (if any).
    if list1:
        tail.next = list1
    elif list2:
        tail.next = list2

    # Return the head of the merged list (excluding the dummy node).
    return dummy.next

def list_to_linked_list(lst):
    """
    Helper function to convert a Python list to a linked list.

    Args:
        lst (list): A Python list of integers.

    Returns:
        ListNode: The head of the linked list.
    """
    if not lst:
        return None
    head = ListNode(lst[0])
    tail = head
    for val in lst[1:]:
        tail.next = ListNode(val)
        tail = tail.next
    return head

def linked_list_to_list(head):
    """
    Helper function to convert a linked list to a Python list.

    Args:
        head (ListNode): The head of the linked list.

    Returns:
        list: A Python list of integers.
    """
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

def main():
    """
    Main function to demonstrate the usage of mergeTwoLists function.
    """
    # Example 1
    list1_data = [1, 2, 4]
    list2_data = [1, 3, 4]
    list1 = list_to_linked_list(list1_data)
    list2 = list_to_linked_list(list2_data)
    merged_list = mergeTwoLists(list1, list2)
    print(f"Example 1: Merged List = {linked_list_to_list(merged_list)}")  # Output: [1, 1, 2, 3, 4, 4]

    # Example 2
    list1_data = []
    list2_data = []
    list1 = list_to_linked_list(list1_data)
    list2 = list_to_linked_list(list2_data)
    merged_list = mergeTwoLists(list1, list2)
    print(f"Example 2: Merged List = {linked_list_to_list(merged_list)}")  # Output: []

    # Example 3
    list1_data = []
    list2_data = [0]
    list1 = list_to_linked_list(list1_data)
    list2 = list_to_linked_list(list2_data)
    merged_list = mergeTwoLists(list1, list2)
    print(f"Example 3: Merged List = {linked_list_to_list(merged_list)}")  # Output: [0]

if __name__ == "__main__":
    main()
