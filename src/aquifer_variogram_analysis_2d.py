#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 15:27:47 2022

@author: fhesse
"""

import numpy as np
import gstools as gs
import matplotlib.pyplot as plt
import pandas as pd

def get_data():
    
    #read in data from a file
#    K_data_df = pd.read_csv("../sites/Bouteldja_aquifer_ALG/K_values.csv")
    #K_data_df = pd.read_csv("../sites/Hawaii_aquifers_US/K_values.csv")
    #K_data_df = pd.read_csv("../sites/San_Augustin_Basin_aquifer_MEX/K_ values.csv")
#    K_data_df = pd.read_csv("../sites/Snake_River_aquifer_US/K_ values.csv")
    K_data_df = pd.read_csv("../data/aquifer_T.csv")
#    K_data_df = pd.read_csv("../sites/Kuwait_aquifer_KUW/T_values.csv")
    
    
#    x = K_data_df["X_m"]
#    y = K_data_df["Y_m"]
#    x = K_data_df["Longitude_NAD83"]
#    y = K_data_df["Latitude_NAD83"]
#    x = K_data_df["Northing depth"]
#    y = K_data_df["Easting"]
    x = K_data_df["East UTM km"]
    y = K_data_df["North UTM km"]
    
    #field = K_data_df["K_log transformed"]
#    field = np.log(K_data_df["Hydraulic_conductivity_m/d"])
    field = np.log(K_data_df["T m2/d"])
    
    return x, y, field

def get_empirical_variogram(x, y, field):
    
    # estimate the empirical variogram of the field
    bin_center, gamma = gs.vario_estimate((x, y), field)
    return bin_center, gamma

def fit_model_variogram(bin_center, gamma):
    
    # fit the variogram variogram with a stable model. (no nugget fitted)
    fit_model = gs.Stable(dim=2)
    fit_model.fit_variogram(bin_center, gamma, nugget=False)
    return fit_model

if __name__ == '__main__':
    
    x, y, field = get_data()
    
    bin_center, gamma = get_empirical_variogram(x, y, field)
#    fit_model = fit_model_variogram(bin_center, gamma)
    
    # output
#    ax = fit_model.plot(x_max=max(bin_center))
    plt.scatter(bin_center, gamma)
    plt.show()
#    print(fit_model)