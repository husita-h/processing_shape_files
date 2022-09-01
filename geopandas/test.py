# https://github.com/geopandas/geopandas
# https://geopandas.org/en/stable/docs/user_guide/io.html?highlight=geojson
# https://geopandas.org/en/stable/docs/reference/api/geopandas.read_file.html
# https://geopandas.org/en/stable/docs/reference/api/geopandas.GeoDataFrame.to_file.html

import geopandas as gpd

path_shp_pl_distribution_map = "../data/pl_distribution_map/liqpt.shp"
gdf = gpd.read_file(path_shp_pl_distribution_map)
gdf.to_file("./data_pl_distribution_map/output_utf-8.geojson", driver='GeoJSON', encoding="utf-8")
gdf.to_file("./data_pl_distribution_map/output_shift-jis.geojson", driver='GeoJSON', encoding="shift-jis")
gdf.to_csv("./data_pl_distribution_map/output_utf-8.csv")
gdf.to_csv("./data_pl_distribution_map/output_shift-jis.csv")

path_shp_liquefaction_forecast_map = "../data/liquefaction_forecast_map/eqliq.shp"
gdf = gpd.read_file(path_shp_liquefaction_forecast_map)
gdf.to_file("./data_liquefaction_forecast_map/output_utf-8.geojson", driver='GeoJSON', encoding="utf-8")
gdf.to_file("./data_liquefaction_forecast_map/output_shift-jis.geojson", driver='GeoJSON', encoding="shift-jis")
gdf.to_csv("./data_liquefaction_forecast_map/output_utf-8.csv")
gdf.to_csv("./data_liquefaction_forecast_map/output_shift-jis.csv")
