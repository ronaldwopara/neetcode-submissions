class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        y = 0
        s_hash = dict.fromkeys(s, y)
        t_hash = dict.fromkeys(t, y)
        for s_let in s:
            s_hash[s_let] += 1
        for t_let in t:
            t_hash[t_let] += 1
        return s_hash == t_hash
        
            

            
            
         
        