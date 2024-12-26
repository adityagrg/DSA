object Solution {
    def removeDuplicates(nums: Array[Int]): Int = {
        var pointer1 = 1
        var prev = 0
        var pointer3 = 1

        var k = 1

        while (pointer3 < nums.length) {
            if (nums(prev) != nums(pointer3)) {
                nums(pointer1) = nums(pointer3)
                pointer1 += 1
                k += 1
            }

            prev = pointer3
            pointer3 += 1
        }
        k
    }
}