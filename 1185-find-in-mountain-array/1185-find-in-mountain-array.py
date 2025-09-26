# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
 #   def get(self, index: int) -> int:
 #   def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        n = mountainArr.length()
        def peak(mountainArr):
            left, right = 0, n-1
            while left<=right:
                mid = left+(right-left)//2
                if mountainArr.get(mid) < mountainArr.get(mid + 1):
                    left=mid+1
                else:
                    right=mid-1
            return left
        
        def search_des(mountainArr, target, peak):
            left, right = peak, n-1
            ans = -1
            while left<=right:
                mid=left+(right-left)//2
                if mountainArr.get(mid)==target:
                    ans=mid
                    right=mid-1
                elif mountainArr.get(mid)<target:
                    right=mid-1
                else:
                    left=mid+1
            return ans
            
        def search_asc(mountainArr, target, peak):
            left, right= 0, peak
            ans = -1
            while left<=right:
                mid=left+(right-left)//2
                if mountainArr.get(mid)==target:
                    ans=mid
                    right=mid-1
                elif mountainArr.get(mid)<target:
                    left=mid+1
                else:
                    right=mid-1
            return ans
        peak = peak(mountainArr)
        ans1 = search_des(mountainArr, target, peak)
        ans2 = search_asc(mountainArr, target, peak)
        if ans2!=-1:
            return ans2
        else:
            return ans1