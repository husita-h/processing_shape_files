# https://github.com/geopandas/geopandas

import geopandas as gpd
path_shp = "./N03-20210101_20_GML/N03-21_20_210101.shp"

gdf = gpd.read_file(path_shp)
gdf.head()