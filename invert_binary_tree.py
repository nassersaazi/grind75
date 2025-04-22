# Definition for a binary tree node.  
class TreeNode(object):  
    def __init__(self, val=0, left=None, right=None):  
        self.val = val  
        self.left = left  
        self.right = right  

class Solution(object):  
    def invertTree(self, root):  
        """  
        :type root: Optional[TreeNode]  
        :rtype: Optional[TreeNode]  
        """  
        # Base case: if the tree is empty  
        if root is None:  
            return None  
        
        # Swap the left and right children  
        root.left, root.right = root.right, root.left  
        
        # Invert the subtrees  
        self.invertTree(root.left)  
        self.invertTree(root.right)  
        
        return root  

# Function to print the tree in pre-order traversal  
def print_tree(root):  
    if root is not None:  
        print(root.val, end=' ')  
        print_tree(root.left)  
        print_tree(root.right)  

# Example usage:  
if __name__ == "__main__":  
    # Build the example tree [4,2,7,1,3,6,9]  
    root = TreeNode(4)  
    root.left = TreeNode(2)  
    root.right = TreeNode(7)  
    root.left.left = TreeNode(1)  
    root.left.right = TreeNode(3)  
    root.right.left = TreeNode(6)  
    root.right.right = TreeNode(9)  

    solution = Solution()  
    # Invert the tree  
    inverted_root = solution.invertTree(root)  

    # Print the inverted tree  
    print("Inverted tree (pre-order):")  
    print_tree(inverted_root)  # Expected output: 4 7 6 9 2 3 1   