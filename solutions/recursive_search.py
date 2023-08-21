def recursive_search(list, target):

    if len(list) == 0:

        return False
    
    if list[0] == target:

        return True

    return recursive_search(list[1:], target) 
        
if __name__ == '__main__':

    print("Expecting: True")
    print(recursive_search([1, 2, 3], 2))

    print("")

    print("Expecting: False")
    print(recursive_search([3, 2, 1], 4))

    print("")

    print("Expecting: False")
    print(recursive_search([], 7))

    print("")

    print("Expecting: True")
    print(recursive_search([7], 7))

# Please add your pseudocode to this file
############################################################################
# return false if array is empty
# return true if first element of array == target

# return recursive_search(input array - first element, target)
############################################################################

# And a written explanation of your solution
############################################################################
# There are two bases cases for this problem: if we find the target, we should return true
# and stop recursing, and if we go through all of the elements, we should stop recursing
# and return false. This means we need to operate on a subset of the array every time we
# recurse. To do this, we can pass the array minus the first element to the recursive call, 
# and then check if the 0th element in the array is the target. The array will shrink by
# one element on every invocation.
############################################################################