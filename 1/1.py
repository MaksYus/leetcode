class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]


def main():
    nums = [3, 2, 4]  # list(map(int,input().split()))
    target = 6  # int(input())
    sol = Solution()
    print(sol.twoSum(nums=nums, target=target))


main()
