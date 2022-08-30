import shapefile
import pandas as pd
# import pdb; pdb.set_trace()

path_shp = "../data/pl_distribution_map/liqpt.shp"

def read_shapefile(shp_path):
	sf = shapefile.Reader(shp_path)
	fields = [x[0] for x in sf.fields][1:]

	records =[list(i) for i in sf.records()]
	shps = [s.points for s in sf.shapes()]

	df = pd.DataFrame(columns=fields, data=records)
	df = df.assign(recoords=shps)
	return df

data_frame = read_shapefile(path_shp)
print(data_frame)
print(type(data_frame))
print(data_frame.iat[1, 0])
print(data_frame.iat[1, 1]) # b'\x8f\xac\x81i0\x81\x85PL\x81\x835\x81j'
print(data_frame.iat[1, 2])
# pyshp git:(main) ✗ python3 test2.py
#       b'\x83{\x81[\x83\x8a\x83\x93\x83O'  ...                                     coords
# 0                                     48  ...  [[15506403.474048201, 4277369.180382471]]
# 1                                     49  ...  [[15506187.021062562, 4277788.729732586]]
# 2                                     50  ...   [[15505846.879650068, 4278246.43849973]]
# 3                                     53  ...  [[15506248.864678169, 4277636.164440833]]
# 4                                     60  ...  [[15504736.156669786, 4278197.616002802]]

# CSVへの書き出し
data_frame.to_csv("./data/output.csv")