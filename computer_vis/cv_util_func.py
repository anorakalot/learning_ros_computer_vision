def aspect_ratio(w,h,new_width,new_height):
	dim = tuple()
	if (new_width== 0 and new_height ==0):
		pass
	elif (new_width > 0 and new_height > 0):
		pass
	elif (new_width > 0 and new_height == 0):
		aspect_ratio = new_width / w
		h *= aspect_ratio
		h = int(h)
		w = new_width
		dim = (w,h)
	elif(new_width == 0 and new_height > 0):
		aspect_ratio = new_height / h
		w *= aspect_ratio
		w = int(w)
		h = new_width
		dim = (w,h)
	return dim
	
	
