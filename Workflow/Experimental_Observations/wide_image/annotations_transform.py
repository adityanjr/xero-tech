f = open("1.txt", "r")
f_1 = open("CROP/1_1.txt", "w")
f_2 = open("CROP/1_2.txt", "w")
f_3 = open("CROP/1_3.txt", "w")
f_4 = open("CROP/1_4.txt", "w")
count = 0
a = f.read().split("\n")
for i in a:
	count+=1
	print(count)
	c, x, y, h, w  = list(map(float, i.split()))
	if x<0.5 and y<0.5:
		n_x = 2*x
		n_y = 2*y
		n_h = 2*h
		n_w = 2*w
		f_1.write(" ".join(list(map(str, [int(c), n_x, n_y, n_h, n_w]))))
		f_1.write("\n")
	elif x>0.5 and y<0.5:
		n_x = x-0.5
		n_x = 2*n_x
		n_y = 2*y
		n_h = 2*h
		n_w = 2*w
		f_2.write(" ".join(list(map(str, [int(c), n_x, n_y, n_h, n_w]))))
		f_2.write("\n")
	elif x<0.5 and y>0.5:
		n_y = y-0.5
		n_x = 2*x
		n_y = 2*n_y
		n_h = 2*h
		n_w = 2*w
		f_3.write(" ".join(list(map(str, [int(c), n_x, n_y, n_h, n_w]))))
		f_3.write("\n")
	else:
		n_x = x-0.5
		n_y = y-0.5
		n_x = 2*n_x
		n_y = 2*n_y
		n_h = 2*h
		n_w = 2*w
		f_4.write(" ".join(list(map(str, [int(c), n_x, n_y, n_h, n_w]))))
		f_4.write("\n")
f_1.close()
f_2.close()
f_3.close()
f_4.close()

