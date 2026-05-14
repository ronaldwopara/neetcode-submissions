class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Indices for the search boundaries
        m = len(matrix) - 1 # Last Row Index
        n = len(matrix[0]) - 1 # Last Column Index

        top_row = 0
        bottom_row = m
        target_row = -1
        
        # PHASE 1: Binary Search for the correct row (O(log m))
        while top_row <= bottom_row:
            mid_row = (top_row + bottom_row) // 2
            
            # Case 3: Target is within the bounds of this row
            if matrix[mid_row][0] <= target <= matrix[mid_row][n]:
                target_row = mid_row
                break 

            # Case 1: Target is too small (must be above)
            elif target < matrix[mid_row][0]:
                bottom_row = mid_row - 1
            
            # Case 2: Target is too large (must be below)
            else: # target > matrix[mid_row][n]
                top_row = mid_row + 1
        
        # Check for row search failure
        if target_row == -1:
            return False

        # PHASE 2: Binary Search within the target_row (O(log n))
        arr = matrix[target_row]
        low_col = 0
        high_col = n 

        while low_col <= high_col:
            mid_col = (low_col + high_col) // 2

            if arr[mid_col] == target:
                return True # Found it!
            elif arr[mid_col] < target:
                low_col = mid_col + 1
            else:
                high_col = mid_col - 1
        
        # If column search finishes without finding the target
        return False