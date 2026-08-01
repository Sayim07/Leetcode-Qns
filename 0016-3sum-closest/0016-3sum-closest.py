class Solution(object):
    def threeSumClosest(self, a, target):
        a.sort()
        n = len(a)
        max_diff = float('inf')
        r_sum = 0

        for i in range(n - 2):
            left = i + 1
            right = n - 1
            while left < right:
                sum = a[i] + a[left] + a[right]
                diff = abs(sum - target)
                
                if diff < max_diff:
                    max_diff = diff
                    r_sum = sum  
                    
                if sum == target:
                    return r_sum
                elif sum < target:
                    left += 1   
                else:
                    right -= 1  

        return r_sum            