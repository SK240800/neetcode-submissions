class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list)
        for i in strs:
            SortedS= ''.join(sorted(i))
            dic[SortedS].append(i)
        return list(dic.values())

        