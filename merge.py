# Definition for singly-linked list.  
class ListNode(object):  
    def __init__(self, val=0, next=None):  
        self.val = val  
        self.next = next  

class Solution(object):  
    def mergeTwoLists(self, list1, list2):  
        # Create a dummy node to act as the starting point of the merged list  
        dummy = ListNode()  
        tail = dummy  # This pointer will help us build the new list  
        
        # Traverse both lists until one is empty  
        while list1 and list2:  
            if list1.val < list2.val:  # Compare values of nodes  
                tail.next = list1  # Attach current node of list1  
                list1 = list1.next  # Move to the next node in list1  
            else:   
                tail.next = list2  # Attach current node of list2  
                list2 = list2.next  # Move to the next node in list2  
            tail = tail.next  # Move the tail to the end of the merged list  
        
        # At this point, at least one of the lists is now empty  
        if list1:  # If list1 has leftover nodes  
            tail.next = list1  # Attach the rest of list1 to merged list  
        elif list2:  # If list2 has leftover nodes  
            tail.next = list2  # Attach the rest of list2 to merged list  
        
        # Return the merged list, which starts after the dummy node  
        return dummy.next

# Example usage:
def print_list(node):
    while node:
        print(node.val, end=" -> ")
        node = node.next
    print("None")

list1 = ListNode(1, ListNode(3, ListNode(5)))
list2 = ListNode(2, ListNode(4, ListNode(6)))

solution = Solution()
merged_head = solution.mergeTwoLists(list1, list2)

print("Merged List:")
print_list(merged_head)  