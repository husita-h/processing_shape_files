# https://github.com/geopandas/geopandas
# https://geopandas.org/en/stable/docs/user_guide/io.html?highlight=geojson
# https://geopandas.org/en/stable/docs/reference/api/geopandas.read_file.html
# https://geopandas.org/en/stable/docs/reference/api/geopandas.GeoDataFrame.to_file.html

import geopandas as gpd

path_shp = "../data/pl_distribution_map/liqpt.shp"
gdf = gpd.read_file(path_shp)
gdf.to_file("test.geojson", driver='GeoJSON', encoding="utf-8")
print(gdf).head