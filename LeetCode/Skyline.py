def skyline(buildings):
	left = min(b[LEFT] for b in buildings)
	right = max(b[RIGHT] for b in buildings)
	last_height = None
	output = []
	for i in range(left, right + 1):
		heights = [b[HEIGHT] for b in buildings if b[LEFT] <= i < b[RIGHT]]
		height = max(heights) if heights else 0
		if height != last_height:
			output += [i, height]
			last_height = height
	return output
