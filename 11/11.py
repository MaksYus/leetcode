class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maxs = -1
        self.make_pyram(height = height)
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

    def make_pyram(self,height):
        indexes = []
        for i in range(1,len(height)):
            if height[i] < height[i-1]: indexes.append(i)
        for i in range(len(indexes),-1,-1):
            height.remove(height[i])


def main():
    height = [1,8,6,2,5,4,8,3,7]  # list(map(int,input().split()))
    sol = Solution()
    #sol.make_pyram(height = height)
    print(sol.maxArea(height=height))


main()