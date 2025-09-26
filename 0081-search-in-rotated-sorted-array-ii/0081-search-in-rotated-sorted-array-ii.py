class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        """
        Searches for the target in a rotated sorted array that may contain duplicates.
        This approach uses a single modified Binary Search to handle the pivot and duplicates.
        """
        
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = left + (right - left) // 2
            
            if nums[mid] == target:
                return True
            
            # --- Handling Duplicates (The Crucial Step for Array II) ---
            # If nums[left], nums[mid], and nums[right] are the same, we cannot definitively tell 
            # which half is sorted. The safe O(N) worst-case move is to shrink the boundaries.
            if nums[left] == nums[mid] and nums[mid] == nums[right]:
                left += 1
                right -= 1
                continue # Skip the rest of the checks and re-calculate mid
            
            # --- Standard Rotated Array Binary Search Logic ---
            
            # 1. Check if the LEFT HALF is sorted (from left to mid)
            if nums[left] <= nums[mid]:
                # If the left half is sorted, check if target is within that range
                if nums[left] <= target and target < nums[mid]:
                    right = mid - 1 # Target is in the left sorted half
                else:
                    left = mid + 1  # Target must be in the right (unsorted/rotated) half
            
            # 2. Else, the RIGHT HALF is sorted (from mid to right)
            else: # nums[left] > nums[mid]
                # If the right half is sorted, check if target is within that range
                if nums[mid] < target and target <= nums[right]:
                    left = mid + 1  # Target is in the right sorted half
                else:
                    right = mid - 1 # Target must be in the left (unsorted/rotated) half

        return False

        