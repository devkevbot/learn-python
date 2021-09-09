"""
Array of coins is given e.g. [1, 10, 3]
Find the minimum amount of change that cannot be created with the coins given.
"""


def nonConstructibleChange(coins):
    """
    Time complexity: O(nlogn) because we sort the coin array.
    Space complexity: O(1) because we do not allocate additional memory.
    """
    coins.sort()
    min_change = 1

    for coin in coins:
        if coin > min_change:
            return min_change
        elif coin <= min_change:
            min_change += coin

    return min_change
