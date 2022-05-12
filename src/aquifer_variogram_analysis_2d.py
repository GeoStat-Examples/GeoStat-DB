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

def get_data(site_id):
    
    #read in data from a file
    T_data_df = pd.read_csv("../data/aquifer_T.csv")
    T_field = np.log(T_data_df["T_m2/d"])
    
    x = T_data_df["East_UTM_km"]
    y = T_data_df["North_UTM_km"]
    
    return x, y, T_field

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
    
    x, y, field = get_data(site_id = "Dammam_aquifer")
    
#    bin_center, gamma = get_empirical_variogram(x, y, field)
#    fit_model = fit_model_variogram(bin_center, gamma)
    
    # output
#    ax = fit_model.plot(x_max=max(bin_center))
#    plt.scatter(bin_center, gamma)
#    plt.show()
#    print(fit_model)