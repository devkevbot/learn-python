"""
Two groups of bicycle riders exist: red shirts and blue shirts. Each
bicycle is operated by one red shirt and one blue shirt.

The max speed of bicycle is determined by the fastest rider on it. Given
the speeds of red shirt riders and blue shirt riders, pair up each group
of riders (one red, one blue) such that the group speed is maximized
when fastest == True or that the group speed is minimized when fastest
== False
"""

def tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest):
	"""
	Time: O(nlogn) - Arrays are sorted, n = len of redShirtSpeeds or blueShirtSpeeds
	Space: O(1) - No new arrays are created.
	"""
	redShirtSpeeds.sort()
	blueShirtSpeeds.sort()

	red_max_index = len(redShirtSpeeds) - 1
	blue_max_index = len(blueShirtSpeeds) - 1

	speed_sum = 0

	for _ in range(0, len(redShirtSpeeds)):
		next_max_red = redShirtSpeeds[red_max_index]
		next_max_blue = blueShirtSpeeds[blue_max_index]

		if fastest:
			red_faster = next_max_red >= next_max_blue
			if red_faster:
				speed_sum += next_max_red
				red_max_index -= 1
			else:
				speed_sum += next_max_blue
				blue_max_index -= 1
		else:
			speed_sum += max(next_max_red, next_max_blue)
			red_max_index -= 1
			blue_max_index -= 1

	return speed_sum


