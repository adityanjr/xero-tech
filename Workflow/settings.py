from dotenv import load_dotenv
import os

def load_global_variables():
	load_dotenv()
	fps=os.getenv("fps")
	num_lines=os.getenv("num_lines")
	line_co_ordinates=os.getenv("line_co_ordinates")
	num_droi=os.getenv("num_droi")
	droi_co_ordinates=os.getenv("droi_co_ordinates")
	location_to_store_csv=os.getenv("location_to_store_csv")
	folder_containing_videos=os.getenv("folder_containing_videos")
	return [fps,num_lines, line_co_ordinates, num_droi, droi_co_ordinates, location_to_store_csv, folder_containing_videos]
