import random

def gen_num(scale,minv,maxv):
	data = []
	for i in range(0,scale):
		data.append(random.randint(minv,maxv))
	return data
