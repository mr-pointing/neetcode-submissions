class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mp = defaultdict(list)
        for num in nums:
            if num not in mp.keys():
                mp[num] = 1
            else:
                mp[num] += 1
        mp = sorted(mp.items(),key=lambda x:x[1], reverse=True)

        return_list = []
        for i in range(0, k):
            return_list.append(mp[i][0])
        return return_list
        #return list(mp[0:k])