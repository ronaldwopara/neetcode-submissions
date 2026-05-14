class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): # Early exit if charcters dont match
            return False

        y = 0 # The intial value for all letter the dictionary
        s_hash = dict.fromkeys(s, y) # This creates a dictionary for the s letters all with the value 0  
        t_hash = dict.fromkeys(t, y) # This creates a dictionary for the t letters all with the value 0 

        for s_let in s:
            s_hash[s_let] += 1 # This loops s letters and updates their frequency

        for t_let in t: 
            t_hash[t_let] += 1 # This loops t letters and updates their frequency

        return s_hash == t_hash
        
            

            
            
         
        