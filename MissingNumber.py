class MissingNumber:
    # Constraints
    # n == nums.length
    # 1 <= n <= 104
    # 0 <= nums[i] <= n
    # All the numbers of nums are unique.

    # attributes for testing the program
    testcase1 = [3, 0, 1]
    testcase2 = [0, 1]
    testcase3 = [9, 6, 4, 2, 3, 5, 7, 0, 1]
    testcase4 = []
    testcase5 = [0]

    def missingNumber(self, nums):
        n = len(nums);
        expectedArray = []
        for i in range(n+1):
            expectedArray.append(i)
            if i not in nums:
                print(f"The missing number in the array is: {i}")

        print("The expected numbers that should be in the array is :", expectedArray)




# Driver code
checkMissingNumber = MissingNumber()
print("The testing array is: ", checkMissingNumber.testcase2)
print(checkMissingNumber.missingNumber(checkMissingNumber.testcase2))
