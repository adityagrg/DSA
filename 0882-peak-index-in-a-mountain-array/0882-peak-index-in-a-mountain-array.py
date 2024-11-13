class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        l = 0
        u = len(arr)
        while u > l:
            mid = (l + u)//2
            if arr[mid] > arr[mid -1] and arr[mid] > arr[mid +1]:
                return mid
            elif arr[mid] > arr[mid -1] and arr[mid] < arr[mid +1]:
                l = mid + 1
            else:
                u = mid

        
        return -1