import shapefile
# path_shp = "../data/pl_distribution_map/liqpt.shp"

r = shapefile.Reader("../data/pl_distribution_map/liqpt.shp")

w = shapefile.Writer("../data/pl_distribution_map/liqpt_copy.shp")
w.fields = r.fields[1:] # skip first deletion field

# adding existing Shape objects
for shaperec in r.iterShapeRecords():
    w.record(*shaperec.record)
    w.shape(shaperec.shape)

# or GeoJSON dicts
for shaperec in r.iterShapeRecords():
    w.record(*shaperec.record)
    w.shape(shaperec.shape.__geo_interface__)

w.close()	