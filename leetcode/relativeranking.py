class Solution:
    def findRelativeRanks(self, score: list[int]) -> list[str]:
        rank = ["Gold Medal", "Silver Medal", "Bronze Medal"] + list(map(str, range(4, len(score) + 1)))
        
        place = sorted(score, reverse = True)
        d = dict(zip(place, rank))
        print(d)

        return [d.get(s) for s in score]
    


score = [5,4,3,2,1]

run = Solution()

print(run.findRelativeRanks(score))
# print(list(map(str, range(4, len(score) + 1))))