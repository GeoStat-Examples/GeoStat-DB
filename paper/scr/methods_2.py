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

#from geostat_db_tools import io

def get_meta_data(site_id, direction = "x", geological_unit = "1/1"):
    
    #read in data from a file
    variogram_data_df = pd.read_csv("../../data_proc/soil_variogram.csv")
    
    df = variogram_data_df[variogram_data_df['site_id']==site_id]
    df = df[df['direction']==direction]
    df = df[df['geological_unit']==geological_unit]
  
    return df.iloc[0]


def get_empirical_variogram(site_id, direction = "x", geological_unit = "1/1"):
    
    #read in data from a file
    variogram_data_df = pd.read_csv("../../data_proc/soil_variogram.csv")
    
    df = variogram_data_df[variogram_data_df['site_id']==site_id]
    df = df[df['direction']==direction]
    df = df[df['geological_unit']==geological_unit]
    
    bin_center = df["lag_m"].to_numpy()
    gamma = df["gamma"].to_numpy()
  
    return bin_center.astype(np.float), gamma.astype(np.float)


def fit_model_variogram(bin_center, gamma, model = "Exp"):
    
    # fit the variogram variogram with a exponential model
    
    if model == "Exp":
        fit_model = gs.Exponential(dim=2)
    elif model == "Gau":
        fit_model = gs.Gaussian(dim=2)
    elif model == "Sph":
        fit_model = gs.Spherical(dim=2)
    if model == "Mat":
        fit_model = gs.Matern(dim=2)
    elif model == "Sta":
        fit_model = gs.Stable(dim=2)
        
    foo, foo2, r2 = fit_model.fit_variogram(bin_center, gamma, nugget=True, 
                                            max_eval=10000, return_r2=True)
    return fit_model, r2


if __name__ == '__main__':
    
    
    site_id = "Fuchu_Honmachi_paddy_field"
    direction = "x"
    meta_data = get_meta_data(site_id, direction)
    bin_center, gamma = get_empirical_variogram(site_id, direction)
    
    fit_model_exp, r2 = fit_model_variogram(bin_center, gamma, model = "Exp") 
    fit_model_gau, r2 = fit_model_variogram(bin_center, gamma, model = "Gau")
#    fit_model_sph, r2 = fit_model_variogram(bin_center, gamma, model = "Sph") 
    fit_model_mat, r2 = fit_model_variogram(bin_center, gamma, model = "Mat") 
    fit_model_sta, r2 = fit_model_variogram(bin_center, gamma, model = "Sta")   
    
    # output
    font = {'family' : 'normal', 'weight' : 'bold', 'size' : 20}
    plt.rc('font', **font)

    ax = fit_model_exp.plot(x_max=max(bin_center))
    plt.scatter(bin_center, gamma)
    plt.ylabel(r'$\gamma$')
    plt.xlabel("m")
    
    ax = fit_model_gau.plot(x_max=max(bin_center))
    plt.scatter(bin_center, gamma)
    plt.ylabel(r'$\gamma$')
    plt.xlabel("m")
    
    ax = fit_model_mat.plot(x_max=max(bin_center))
    plt.scatter(bin_center, gamma)
    plt.ylabel(r'$\gamma$')
    plt.xlabel("m")
    
    ax = fit_model_sta.plot(x_max=max(bin_center))
    plt.scatter(bin_center, gamma)
    plt.ylabel(r'$\gamma$')
    plt.xlabel("m")
    
    plt.show()
    