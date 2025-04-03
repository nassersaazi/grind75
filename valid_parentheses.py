"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    Every close bracket has a corresponding open bracket of the same type.

 

Example 1:

Input: s = "()"

Output: true

Example 2:

---
Input: s = "()[]{}"

Output: true

Example 3:

Input: s = "(]"

Output: false

Example 4:

Input: s = "([])"

Output: true

 

Constraints:

    1 <= s.length <= 104
    s consists of parentheses only '()[]{}'
"""

"""
- initialise a stack
- dictionary for the data
- iterate through the character list and then processing the dictionary accordingly 
--------------------------------s = "[]({}"

stack = ['(']
# 
stack2 = ['d'] => true return stack 
return not stack2

True True => ++ => + => True
False False =>-- => + => True
False True => -+ => - False
True False => +- => - False

{ =! { 

"""
def isValid(s):
    stack = []
    mapping = {')':'(','}':'{',']':'['}

    for char in s:
        if char in mapping:
            top_element = stack.pop() if stack else # 
            if mapping[char] != top_element
                return False # because there is a mismatch
        else:
            stack.append(char)

    return not stack # return stack


