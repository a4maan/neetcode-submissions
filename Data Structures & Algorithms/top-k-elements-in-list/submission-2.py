class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        l = list(sorted(Counter(nums).items(), key=lambda item: item[1], reverse = True))
        b = []
        for i in range(k):
            b.append(l[i][0])
        return b
        


        

       