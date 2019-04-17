"""
@author: acfromspace
"""

"""
We're given an array with various numbers which need to equal a "target" variable.

What we could do is compare the [n] element to the array itself (avoiding the same element).

seen = {} # this is a set

Python sets:

>>> basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
>>> print(basket) # show that duplicates have been removed
{'orange', 'banana', 'pear', 'apple'}

We need duplicates to be removed because we don't want the conflict of [n] element touching itself.

enumerate(): takes in a data structure and "enumerates" it
    my_list = ['apple', 'banana', 'grapes', 'pear']
    for c, value in enumerate(my_list, 1):
        print(c, value)

    # Output:
    # 1 apple
    # 2 banana
    # 3 grapes
    # 4 pear

To approach this problem:

1. Create an empty set
2. With the array, enumerate it so properly pass
3. Get the difference from target minus [number]
4. If difference is in the set (which it won't be for the first tries) return the solution
5. Else keep going through the enumerate
"""


class Solution:

    def two_sum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen = {}
        for index, num in enumerate(nums):
            print("{}: " + str(seen))
            print("index, num: " + str(index), str(num))
            other = target - num
            print("other: " + str(other))
            if other in seen:
                print("SOLUTION: " + str([seen[other], index]))
                return [seen[other], index]
            else:
                print("{}: " + str(seen))
                print("DO AGAIN!")
                seen[num] = index
        return []


test_object = Solution()
nums = [2, 7, 11, 15]
target = 26
print("Stages of the solution:")
print("nums: " + str(nums))
print("target: " + str(target))
test_object.two_sum(nums, target)

"""
Time complexity : O(n)
We traverse the list containing "n" elements only once. Each look up in the table costs only O(1) time.

Space complexity : O(n)
The extra space required depends on the number of items stored in the hash table, which stores at most "n" elements.
"""
