class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        table = {}

        for word in strs:
            count = [0] * 26

            for c in word:
                count[ord(c) - ord('a')] += 1

            key = tuple(count)

            if key not in table:
                table[key] = []

            table[key].append(word)

        return list(table.values())

    


        