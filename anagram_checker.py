class Solution(object):  
    def isAnagram(self, s, t):  
        """  
        :type s: str  
        :type t: str  
        :rtype: bool  
        """  
        # Step 1: Check if lengths are equal  
        if len(s) != len(t):  
            return False  
        
        # Step 2: Initialize count dictionary  
        count = {}  
        
        # Count each character in string s  
        for char in s:  
            count[char] = count.get(char, 0) + 1  
        
        # Step 3: Decrease the count based on characters in 't'  
        for char in t:  
            if char not in count:  
                return False  
            count[char] -= 1  
            if count[char] < 0:  
                return False  

        # Step 4: Check if all counts are zero  
        return all(value == 0 for value in count.values())  

# Example test cases  
if __name__ == "__main__":  
    solution = Solution()  

    # Test case 1: anagrams  
    s1 = "listen"  
    t1 = "silent"  
    print(solution.isAnagram(s1, t1))  # Output: True  

    # Test case 2: not anagrams  
    s2 = "hello"  
    t2 = "world"  
    print(solution.isAnagram(s2, t2))  # Output: False  

    # Test case 3: same characters, different order  
    s3 = "evil"  
    t3 = "vile"  
    print(solution.isAnagram(s3, t3))  # Output: True  

    # Test case 4: empty strings  
    s4 = ""  
    t4 = ""  
    print(solution.isAnagram(s4, t4))  # Output: True  

    # Test case 5: different lengths  
    s5 = "test"  
    t5 = "tests"  
    print(solution.isAnagram(s5, t5))  # Output: False  