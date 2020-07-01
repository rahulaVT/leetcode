class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        ## METHOD 1: Hashmap
        # count = collections.Counter(words)
        # candidates = list(count.keys())
        # candidates.sort(key=lambda x:(-count[x],x))
        # return candidates[:k]
        
        ## METHOD 2: min heap
        count = collections.Counter(words)
        heap = [(-freq,word) for word,freq in count.items()]
        heapq.heapify(heap)
        return [heapq.heappop(heap)[1] for i in range(k)]
