
def intersect(nums1: list[int], nums2: list[int]) -> list[int]:
        nums1.sort()
        nums2.sort()
        # print(nums1,nums2)
        ans = []
        i, j = 0, 0
        n, m = len(nums1), len(nums2)
        print(n,m)

        while i < n and j < m:
            if nums1[i] == nums2[j]:
                ans.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
        return ans

0



nums1 = [1,2,2,1]
nums2 = [2]

print(intersect(nums1,nums2))