def arrayOfProducts(array):
    """
    Time: O(n) where n is the length of the input array
    Space: O(n)
    """
    products = [1 for _ in range(len(array))]

    left_product = 1
    for i in range(len(array)):
        products[i] = left_product
        left_product *= array[i]

    right_product = 1
    for i in reversed(range(len(array))):
        products[i] *= right_product
        right_product *= array[i]

    return products
