class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import Counter 
        seen = {}
        
        for j in strs:
            x = Counter(j)
            sort = tuple(sorted(x.items()))
            if sort in seen: 
                seen[sort] += [j]
            else:
                seen[sort] = [j]
        return list(seen.values())


                




        