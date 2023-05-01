import numpy
import rasterio
from rasterio.mask import mask
import geopandas as gpd

# inshp = input('Input Shapefile: ')#'D:/Dr. Izadi/Iran_Shapefiles/Ostan.shp'
# inRas = input('Input Raster: ')#'D:/Dr. Izadi/2-Risk/EW_WRF_20190318_1days.tif'
# outDir = input('Output Directory: ')#'D:/Dr. Izadi/Output/'
inshp = 'src/Ostan.shp'
inRas = 'items/EW_WRF_20190318_1days.tif'
outDir = 'items/output/'




Vector = gpd.read_file(inshp)
Risk_R_Area = {}

for i in range(len(Vector['name_en'])):

    Vector_i = Vector[Vector['name_en'] == Vector['name_en'][i]]

    with rasterio.open(inRas) as src:
        Vector_i = Vector_i.to_crs(src.crs)
        out_image, out_transform = mask(src, Vector_i.geometry, crop = True)
        out_meta = src.meta.copy() # copy the metadata of the source DEM

        out_meta.update({
            'driver':'Gtiff',
            'height':out_image.shape[1], # height starts with shape[1]
            'width':out_image.shape[2], # width starts with shape[2]
            'transform':out_transform
        })

    outRas = outDir + 'Out_Rast_Risk_' + str(i + 1) + '.tif'
    
    with rasterio.open(outRas,'w',**out_meta) as dst:
        dst.write(out_image)

    new_out_image = out_image[out_image!=-9999]
    n_tot = len(new_out_image)

    Risk_R_Area[Vector['name_en'][i]] = [0, 0, 0, 0, 0]

    for j in range(5):
        Risk_R_Area[Vector['name_en'][i]][j] = len(new_out_image[new_out_image == j+1]) / n_tot
        
        

