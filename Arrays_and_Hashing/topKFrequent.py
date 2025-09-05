from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(freq) + 1)]
        res = []
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        for num, cnt in count.items():   # Reverse the dictionary count and store it as [count: num]
            freq[cnt].append(num)
        for i in range(len(freq) - 1, 0, -1):      # we only go till 0 since the number of times an element is seen 0 times is of no value to us. And in the case that there are no items/num in the nums List, the algo would return an empty list.
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res