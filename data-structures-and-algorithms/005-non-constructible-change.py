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
