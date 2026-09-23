class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}
        for num in nums: 
            if num in seen:
                seen[num] += 1
            else:
                seen[num] = 1

        freq = []
        for key, value in seen.items():
            freq.append((value, key))

        freq.sort(reverse=True)

        final_list = []
        for i in range(k):
            final_list.append(freq[i][1])

        return final_list


            
            