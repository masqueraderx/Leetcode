'''
Name: 220. Contains Duplicate III
Link: https://leetcode.com/problems/contains-duplicate-iii/
Time: 11/25/2020
Idea:
step1: divide data into n bucket by nums[i] // (t + 1)
step2: difference bwt neighboring bucket is at most 2 * t + 1
step3: difference bwt same bucket is at most t
'''

class Solution:
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        # # Brute Force(TLE)
        # for i in range(len(nums)):
        #     for j in range(1, k+1):
        #         if i+j >= len(nums):
        #             break
        #         if abs(nums[i+j] - nums[i]) <= t:
        #             return True
        # return False

        # Bucket Sort
        bucket = dict()
        for i in range(len(nums)):
            nth = nums[i] // (t + 1)
            if nth in bucket:
                return True
            if nth - 1 in bucket and abs(nums[i] - bucket[nth - 1]) <= t:
                return True
            if nth + 1 in bucket and abs(nums[i] - bucket[nth + 1]) <= t:
                return True
            bucket[nth] = nums[i]
            if i >= k:
                bucket.pop(nums[i - k] // (t + 1))
        return False

if __name__ == '__main__':
    s = Solution()
    print(s.containsNearbyAlmostDuplicate([1,5,9,1,5,9], 2, 3))