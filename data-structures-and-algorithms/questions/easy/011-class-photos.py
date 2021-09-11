"""
A class with an even amount of students is preparing for photo day.
Exactly half the class is wearing red shirts, half blue shirts. To take
the photo, the class arranges into two rows. Each row must consist of
students with the same coloured shirts and students in the back row must
be strictly taller than the student directly in front of them.

Given two arrays of heights representing students wearing red and blue
shirts, respectively, determine if a photo can be taken that matches
these constraints.
"""


def classPhotos(redShirtHeights, blueShirtHeights):
    """
    Time: O(nlogn) - array is sorted, n is the number of students
    Space: O(1) - no new arrays are allocated
    """
    redShirtHeights.sort()
    blueShirtHeights.sort()

    shortest_red_shirt = redShirtHeights[0]
    shortest_blue_shirt = blueShirtHeights[0]

    if shortest_red_shirt == shortest_blue_shirt:
        return False

    red_in_front = shortest_red_shirt < shortest_blue_shirt

    for index in range(0, len(redShirtHeights)):
        if red_in_front and (redShirtHeights[index] >= blueShirtHeights[index]):
            return False

    return True
