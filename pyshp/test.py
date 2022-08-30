# https://pypi.org/project/pyshp/
import shapefile

path_shp = "../data/pl_distribution_map/liqpt.shp"
src = shapefile.Reader(path_shp, encoding='SHIFT-JIS')
shp = src.shapes()[0]
rec = src.record(0) 

print(src.bbox)
print(src.numRecords)
print(shp.points)
# print(shp.shapeTypeName)
print(shp.__geo_interface__)
print(rec)

# shprecs = src.shapeRecords()
# shp = shprecs[n].shape
# rec = shprecs[n].record

for shprec in src.iterShapeRecords():
    shp = shprec.shape
    rec = shprec.record