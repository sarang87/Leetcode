class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        
        # get prefix sum
        def get_prefix_sum(ary):
            n = len(ary)
            pre_sum = [ary[0]] * n
            for i in range(1,n):
                pre_sum[i] = pre_sum[i-1] + ary[i]
            return pre_sum

        
        # get the sum of each row
        def sum_row(matrix, c1, c2):
            ary = []
            for r in range(len(matrix)):
                res = 0
                for c in range(c1,c2+1):
                    res += matrix[r][c]
                ary.append(res)
            return ary
                
		# sum of elements for each row 
		
        # x x x x x x    y
        # x x x x x x    y   i
        # x x x x x x    y
        # x x x x x x    y   j
        # x x x x x x    y
        
        # prefix_sum[j] - prefix_sum[i] <= k
        # prefix_sum[i] >= prefix_sum[j] - k
        
        # find max sum of subarray that no larger than k
        def helper(ary, k):
            prefix_sum = get_prefix_sum(ary)
            res = float('-inf')
            prefix_sum = [0] + prefix_sum
            n = len(prefix_sum)
            
            # # find max sum of subarray using two loops
            # # this will lead a Time Limit Exceeded
            # # find prefix_sum[i] - prefix_sum[j] <= k
            # for i in range(n):
            #     for j in range(i+1,n):
            #         if prefix_sum[i] - prefix_sum[j] == k:
            #             return k
            #         if prefix_sum[i] >  prefix_sum[j] - k:
            #             res = max(prefix_sum[j] - prefix_sum[i], res)
            # return res
            
            
            # find max sum of subarray using a single loop
            # use biset.bisect perform a binary search on a list
            # the list is create by using bisect.insot() so that it is ascending order
            
            # looking for prefix_sum[right] - prefix_sum[left] <= k
            # prefix_sum[right] - k <= prefix_sum[left]
            # then for each iteration, i, if prefix_sum[i] != k, try to find
            # the smallest element in prefix_ascd
            # (some previous prefix_sum[i] which is prefix_sum[left] ) that larger than 
            # the current prefix_sum[i] - k which is prefix_sum[right] - k
            # 
            prefix_ascd = [0]
            for i in range(1,n):
                if prefix_sum[i] == k:
                    return k
                # find prefix_ascd[idx] >= prefix_sum[i] - k
                # which means prefix_sum[left] >= prefix_sum[right] - k
                idx = bisect.bisect_left(prefix_ascd, prefix_sum[i] - k)
                if 0 <= idx < len(prefix_ascd):
                    res = max(res, prefix_sum[i] - prefix_ascd[idx])
                bisect.insort(prefix_ascd, prefix_sum[i])
            return res
                
        
        row = len(matrix)
        col = len(matrix[0])
        res = float('-inf')
        for c1 in range(col):
            for c2 in range(c1,col):
                ary = sum_row(matrix, c1, c2)
                res = max(res, helper(ary,k))
        return res