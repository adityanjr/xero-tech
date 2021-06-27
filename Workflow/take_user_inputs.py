# Taking User Inputs
def taking_inputs_and_update_env() :
	fps = int(input())
	num_lines = int(input())
	line_co_ordinates = []
	num_droi = int(input())
	droi_co_ordinates = []
	location_to_store_csv = input()
	folder_containing_videos = input()
	
	for z in range(num_lines):
		label = input()
		x1 = int(input())
		y1 = int(input())
		x2 = int(input())
		y2 = int(input()) 
		line_co_ordinates.append({'label':label, 'line': [(x1,y1),(x2,y2)]})
		
	for z in range(num_droi):
		x = int(input())
		y = int(input())
		droi_co_ordinates.append((x,y))
		

# Storing user inputs in .env file
	with open(".env", "w") as f :
		f.write("fps="+str(fps)+"\n")
		f.write("num_lines="+str(num_lines)+"\n")
		f.write("line_co_ordinates="+str(line_co_ordinates)+"\n")
		f.write("num_droi="+str(num_droi)+"\n")
		f.write("droi_co_ordinates="+str(droi_co_ordinates)+"\n")
		f.write("location_to_store_csv="+location_to_store_csv+"\n")
		f.write("folder_containing_videos="+folder_containing_videos)
	f.close()
