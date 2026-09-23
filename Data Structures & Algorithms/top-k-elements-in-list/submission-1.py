class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        for i in nums:
            dic[i] = 1+ dic.get(i,0)
        
        heap =[]
        for num in dic.keys():
            heapq.heappush(heap,(dic[num],num))
            if len(heap) > k:
                heapq.heappop(heap)
        
        res=[]
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res
        