'''
Name: 219. Contains Duplicate II
Link: https://leetcode.com/problems/contains-duplicate-ii/
Time: 11/25/2020
'''

class Solutions:
    def containsNearbyDuplicate(self, nums, k):
        # Use a window to record interval k
        window = set([])
        for num in range(len(nums)):
            if num > k:
                window.discard(nums[num-k-1])
            if nums[num] in window:
                return True
            else:
                window.add(nums[num])

if __name__ == '__main__':
    s = Solutions()
    print(s.containsNearbyDuplicate([1,2,3,1,2,3], 2))