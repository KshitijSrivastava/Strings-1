
# Custom Sort String (https://leetcode.com/problems/custom-sort-string/)


class Solution:
    def customSortString(self, order: str, s: str) -> str:
        
        #storing the string in hash map
        d_s = {}
        for char in s:
            if char not in d_s:
                d_s[char] = 0
            d_s[char] += 1
            
        out = []
        idx = 0
        
        #looping through order and if the word in order is also in hashmap add to output
        while idx < len(order):
            if order[idx] in d_s and d_s[ order[idx] ] > 0:
                out.append( order[idx] )
                d_s[ order[idx] ] -= 1
            else:
                idx += 1
        
        #add the rest of the values
        for key, value in d_s.items():
            for i in range(value):
                out.append(key)
        return "".join(out)