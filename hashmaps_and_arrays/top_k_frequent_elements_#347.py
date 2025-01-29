class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        frequency_buckets = defaultdict(list)
        
        for num, freq in counter.items():
            frequency_buckets[freq].append(num)
        
        result = []
        for freq in range(len(nums), 0, -1):
            if freq in frequency_buckets:
                result.extend(frequency_buckets[freq])
                if len(result) >= k:
                    return result[:k]
        return result