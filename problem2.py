
# Longest Substring Without Repeating Characters

# (https://leetcode.com/problems/longest-substring-without-repeating-characters/)


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        max_length = 0
        d = set()
        
        i = 0
        j = 0
        
        while j < n:
            
            #if element not in set, add to the set
            if s[j] not in d:
                d.add( s[j] )
                j += 1
                
                max_length = max( len(d),  max_length)
            else:#if element in the set then remove the ith char
                d.remove( s[i] )
                i += 1
                
        return max_length
                