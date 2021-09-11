"""
Given two arrays of integers, return the pair of elements (one from each
array) which have the smallest difference.
"""


def smallestDifference(arrayOne, arrayTwo):
    """
    Time: O(nlog(n) + mlog(m)), where n is the length of arrayOne and m is the length of arrayTwo
    Space: O(1)
    """
    arrayOne.sort()
    arrayTwo.sort()

    arrayOnePtr = 0
    arrayTwoPtr = 0

    smallestDifferenceAmount = float("inf")
    smallestElements = []

    while arrayOnePtr < len(arrayOne) and arrayTwoPtr < len(arrayTwo):
        arrayOneValue = arrayOne[arrayOnePtr]
        arrayTwoValue = arrayTwo[arrayTwoPtr]

        currentDifference = abs(arrayOneValue - arrayTwoValue)

        if currentDifference < smallestDifferenceAmount:
            smallestDifferenceAmount = currentDifference
            smallestElements = [arrayOneValue, arrayTwoValue]

        if arrayOneValue > arrayTwoValue:
            arrayTwoPtr += 1
        else:
            arrayOnePtr += 1

    return smallestElements
