class Solution(object):
    def maxCoins(self, nums):

        nums = [1] + nums + [1]
        n = len(nums)
        dp = [[0] * n for _ in xrange(n)]

        def calculate(i, j):
            if dp[i][j] or j == i + 1:
                return dp[i][j]
            coins = 0
            for k in xrange(i+1, j):
                coins = max(coins, nums[i] * nums[k] * nums[j] + calculate(i, k) + calculate(k, j))
            dp[i][j] = coins
            return coins

        return calculate(0, n-1)

class Solution(object):
        def maxCoins(self, nums):
            nums = [1] + nums + [1] 
            n = len(nums)
            dp = [[0] * n for _ in xrange(n)]
    
            for gap in xrange(2, n):
                for i in xrange(n-gap):
                    j = i + gap
                    for k in xrange(i+1, j):
                        dp[i][j] = max(dp[i][j], nums[i] * nums[k] * nums[j] + dp[i][k] + dp[k][j])
            return dp[0][n-1]