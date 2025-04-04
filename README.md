## solutions to common coding problems

### [merge_two_sorted_linked_lists](./merge_two_sorted_linked_lists.py)

**ListNode Class:**

* Defines the structure of a node in a singly linked list.
* Each node has a value (`val`) and a pointer to the next node (`next`).

**mergeTwoLists(list1, list2) Function:**

* Takes the heads of the two sorted linked lists (`list1` and `list2`) as input.
* Creates a dummy node (`dummy`) to simplify the merging process. The dummy node is not part of the final merged list; it's just a convenient starting point.
* Creates a `tail` pointer, initialized to the dummy node. The `tail` pointer is used to keep track of the last node in the merged list as we build it.
* Iterates while both `list1` and `list2` have nodes:
    * Compares the values of the current nodes in `list1` and `list2`.
    * Appends the node with the smaller value to the merged list by setting `tail.next` to the appropriate node.
    * Moves the pointer of the list from which the node was taken to the next node.
    * Moves the `tail` pointer to the newly added node.
* After the loop, one of the lists might still have remaining nodes. Appends the remaining nodes from the non-empty list to the merged list.
* Returns the `next` of the dummy node, which is the head of the actual merged list.

**list_to_linked_list(lst) Function:**

* A helper function to convert a Python list to a linked list.
* Takes a Python list `lst` as input.
* Creates a linked list with the values from the Python list.
* Returns the head of the created linked list.

**linked_list_to_list(head) Function:**

* A helper function to convert a linked list to a Python list.
* Takes the head of a linked list as input.
* Traverses the linked list and stores the value of each node in a Python list.
* Returns the Python list.

**main() Function:**

* Demonstrates the usage of the `mergeTwoLists` function with three examples.
* Uses the helper functions `list_to_linked_list` and `linked_list_to_list` to convert between Python lists and linked lists for easier testing.
