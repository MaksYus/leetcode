class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maxs = -1
        h_len = len(height)
        sorted_h = set(height)
        for elem in sorted_h:
            left = 0
            right = h_len-1
            for i in range(h_len):
                if height[i] >= elem: 
                    left = i
                    break
            for i in range(h_len-1,-1,-1):
                if height[i] >= elem:
                    right = i
                    break 
            if (right - left) * elem > maxs:
                maxs = (right - left) * elem
        return maxs


def main():
    height = [1,8,6,2,5,4,8,3,7]  # list(map(int,input().split()))
    sol = Solution()
    print(sol.maxArea(height=height))


main()