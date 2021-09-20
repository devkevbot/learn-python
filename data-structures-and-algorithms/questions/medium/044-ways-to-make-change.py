def numberOfWaysToMakeChange(n, denoms):
    """
    Time: O(n * d)
    Space: O(n)
    ---
    Hints needed: 1/2
    Time: 5 min
    """

    ways_to_make_change = [0 for _ in range(n + 1)]
    ways_to_make_change[0] = 1

    for denom in denoms:
        for amount in range(1, n + 1):
            if denom <= amount:
                remaining_change = amount - denom
                ways_to_make_change[amount] += ways_to_make_change[remaining_change]

    return ways_to_make_change[n]
