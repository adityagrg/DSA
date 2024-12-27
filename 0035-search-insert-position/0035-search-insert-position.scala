object Solution {
    def searchInsert(nums: Array[Int], target: Int): Int = {
        if (nums.length == 1) {
            if (target > nums(0)) {
                return 1
            } else {
                return 0
            }
        }
        var l = 0
        var r = nums.length - 1

        while (l <= r) {
            val mid = l + (r - l) / 2

            if (nums(mid) > target) {
                if (mid == 0) {
                    return 0
                }
                if (nums(mid - 1) < target) {
                    return mid
                }
                
                r = mid - 1
                
            }
            else if (nums(mid) < target) {
                if (mid == nums.length - 1) {
                    return nums.length
                }
                if (nums(mid + 1) > target) {
                    return mid + 1
                }
                
                l = mid + 1
            }
            else {
                return mid
            }
        }
        // -1
        if (l == r && r == nums.length - 1) {
            return nums.length
        }
        else {
            return 0
        }
    }
}