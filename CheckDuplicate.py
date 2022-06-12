class CheckDuplicate:
    # attributes for testing the program
    testCase1 = [1, 2, 3, 1]
    testCase2 = [1, 2, 3, 4]
    testCase3 = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]


    # Method to check if an array has duplicate value
    def containsDuplicate(self):
        for i in range(0, len(self.testCase3)):
            for j in range(i + 1, len(self.testCase3)):
                if self.testCase3[i] == self.testCase3[j]:
                    print("The duplicate numbers are at [index,value]: [", i, ",", self.testCase3[i], "],", "[", j, ",",
                          self.testCase3[j], "]");
                    return True;
                    break;
                else:
                    return False;


# Driver code
# Object instantiation
Test1 = CheckDuplicate()

# Accessing class attributes
# and method through objects
print("The testing array is: ", Test1.testCase3)
print(Test1.containsDuplicate())
