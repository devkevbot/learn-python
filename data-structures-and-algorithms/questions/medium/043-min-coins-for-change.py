def minNumberOfCoinsForChange(n, denoms):
    """
    Time: O(n * d) where n is the input value and d is the number of coin denominations
    Space: O(n)
    ---
    Hints needed: 2/2
    Time: 30 mins
    """
    combinations = [float("inf") for _ in range(n + 1)]
    combinations[0] = 0

    for denom in denoms:
        for amount in range(n + 1):
            if denom <= amount:
                new_amount_of_coins = combinations[amount - denom] + 1
                curr_amount_of_coins = combinations[amount]
                combinations[amount] = min(new_amount_of_coins, curr_amount_of_coins)

    return combinations[n] if combinations[n] != float("inf") else -1
