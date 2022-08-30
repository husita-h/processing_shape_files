import shapefile
import pandas as pd

path_shp = "../data/pl_distribution_map/liqpt.shp"

def read_shapefile(shp_path):
	sf = shapefile.Reader(shp_path)
	fields = [x[0] for x in sf.fields][1:]

	records =[list(i) for i in sf.records()]
	shps = [s.points for s in sf.shapes()]

	df = pd.DataFrame(columns=fields, data=records)
	df = df.assign(coords=shps)

	return df

print(read_shapefile(path_shp).encode("shift_jis"))

