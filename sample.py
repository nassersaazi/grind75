
'''
clear list of any none alphanumeric characters

init left pointer -> cl[0]

init right pointer-> cl[len(cl) - 1]

ip = true

while left pointer <= right pointer
    if rp = lp
        return ip
    if cl[lp] != cl[rp]
        ip = false
        return ip
    else
        lp += 1
        rp -= 1

return ip
'''

def isPalindrome(s):
    cl = [c.lower() for c in s if c.isalnum()]
    lp = 0  # left pointer initialized to first index
    rp = len(cl) - 1  # right pointer initialized to last index
    ip = True  # initial condition

    while lp <= rp:
        if rp == lp:
            return ip
        if cl[lp] != cl[rp]:
            ip = False
            return ip
        else:
            lp += 1
            rp -= 1

    return ip

def main():
    """
    Main function to demonstrate the usage of the isPalindrome function.
    """
    # Example 1
    s1 = "A man, a plan, a canal: Panama"
    print(f"Example 1: s = \"{s1}\", Result = {isPalindrome(s1)}")  # Output: True

    # Example 2
    s2 = "race a car"
    print(f"Example 2: s = \"{s2}\", Result = {isPalindrome(s2)}")  # Output: False

    # Example 3
    s3 = " "
    print(f"Example 3: s = \"{s3}\", Result = {isPalindrome(s3)}")  # Output: True

    # Example 4
    s4 = "Was it a car or a cat I saw?"
    print(f"Example 4: s = \"{s4}\", Result = {isPalindrome(s4)}") # Output: True

    s5 = "Madam, I'm Adam!"
    print(f"Example 5: s = \"{s5}\", Result = {isPalindrome(s5)}") # Output: True

    s6 = "121"
    print(f"Example 6: s = \"{s6}\", Result = {isPalindrome(s6)}") # Output True

    s7 = "123210"
    print(f"Example 7: s = \"{s7}\", Result = {isPalindrome(s7)}") # Output False

if __name__ == "__main__":
    main()
