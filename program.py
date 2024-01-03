class Solution(object):
    def numberOfBeams(self, bank):
        nums = []
        for row in bank:
            count = 0
            for cell in row:
                count += 1 if cell == '1' else 0
            if count > 0:
                nums.append(count)

        ans = 0
        for i in range(0, len(nums) - 1):
            ans += nums[i] * nums[i + 1]
        
        return ans

solution = Solution()
ans = solution.numberOfBeams(["011001","000000","010100","001000"])
print(ans)