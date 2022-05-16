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

from geostat_db_tools import io

def get_meta_data(site_id, direction = "x"):
    
    #read in data from a file
    variogram_data_df = pd.read_csv("../data/aquifer_variogram.csv")
    
    df = variogram_data_df[variogram_data_df['site_id']==site_id]
    df = df[df['direction']==direction]
  
    return df.iloc[0]


def get_empirical_variogram(site_id, direction = "x"):
    
    #read in data from a file
    variogram_data_df = pd.read_csv("../data/aquifer_variogram.csv")
    
    df = variogram_data_df[variogram_data_df['site_id']==site_id]
    df = df[df['direction']==direction]
    
    bin_center = df["lag_m"].to_numpy()
    gamma = df["gamma"].to_numpy()
  
    return bin_center.astype(np.float), gamma.astype(np.float)


def fit_model_variogram(bin_center, gamma):
    
    # fit the variogram variogram with a stable model. (no nugget fitted)
    fit_model = gs.Stable(dim=2)
    fit_model.fit_variogram(bin_center, gamma, nugget=True)
    return fit_model


if __name__ == '__main__':
    
    df = io.init_df()
    
    site_id = "Aa_river"
    direction = "x"
    meta_data = get_meta_data(site_id, direction)
    bin_center, gamma = get_empirical_variogram(site_id, direction)
    fit_model = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    max_scale = bin_center[-1])
    direction = "z"
    meta_data = get_meta_data(site_id, direction)
    bin_center, gamma = get_empirical_variogram(site_id = site_id, 
                                                direction = direction)
    fit_model = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    max_scale = bin_center[-1])
    
    site_id = "Dammam_aquifer"
    meta_data = get_meta_data(site_id = site_id)
    bin_center, gamma = get_empirical_variogram(site_id = site_id)
    fit_model = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    max_scale = bin_center[-1])

    io.write_df(df)
    
    
    # output
    ax = fit_model.plot(x_max=max(bin_center))
    plt.scatter(bin_center, gamma)
    plt.show()
#    print(fit_model)
    