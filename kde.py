"""
Multiple examples of kernel density estimation visualization
"""
import geoplotlib
from geoplotlib.utils import read_csv, BoundingBox, DataAccessObject
import pandas as pd
#import numpy as np
data = pd.read_csv('data/fuel_station.csv', usecols = ['lat', 'lon'],keep_default_na=True).fillna(0)


#geoplotlib.kde(data2, bw=2, cut_below=1e-4)

# lowering clip_above changes the max value in the color scale
geoplotlib.kde(data, bw=7, cut_below=1e-4, clip_above=.1)

# different bandwidths
#geoplotlib.kde(data, bw=20, cmap='PuBuGn', cut_below=1e-4)
#geoplotlib.kde(data, bw=2, cmap='PuBuGn', cut_below=1e-4)

# linear colorscale
#geoplotlib.kde(data2, bw=5, cmap='jet', cut_below=1e-4, scaling='lin')


geoplotlib.show()
