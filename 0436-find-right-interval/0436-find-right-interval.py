class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        result = []
        
        # Create a list of (start, original_index) and sort it by start
        starts = [(intervals[i][0], i) for i in range(n)]
        starts.sort()
        
        for i in range(n):
            end_i = intervals[i][1]
            
            # Manual binary search to find smallest start >= end_i
            left, right = 0, n - 1
            min_index = -1
            
            while left <= right:
                mid = (left + right) // 2
                if starts[mid][0] >= end_i:
                    min_index = starts[mid][1]  # store original index
                    right = mid - 1  # search left to see if smaller valid start exists
                else:
                    left = mid + 1  # search right
                    
            result.append(min_index)
        
        return result
        