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

def get_meta_data(site_id, direction = "x", geological_unit = "1/1"):
    
    #read in data from a file
    variogram_data_df = pd.read_csv("../data/aquifer_variogram.csv")
    
    df = variogram_data_df[variogram_data_df['site_id']==site_id]
    df = df[df['direction']==direction]
    df = df[df['geological_unit']==geological_unit]
  
    return df.iloc[0]


def get_empirical_variogram(site_id, direction = "x", geological_unit = "1/1"):
    
    #read in data from a file
    variogram_data_df = pd.read_csv("../data/aquifer_variogram.csv")
    
    df = variogram_data_df[variogram_data_df['site_id']==site_id]
    df = df[df['direction']==direction]
    df = df[df['geological_unit']==geological_unit]
    
    bin_center = df["lag_m"].to_numpy()
    gamma = df["gamma"].to_numpy()
  
    return bin_center.astype(np.float), gamma.astype(np.float)


def fit_model_variogram(bin_center, gamma):
    
    # fit the variogram variogram with a stable model. (no nugget fitted)
#    fit_model, r2 = gs.Stable(dim=2)
#    fit_model, r2 = gs.Spherical(dim=2)
#    fit_model, r2 = gs.Gaussian(dim=2)
    fit_model = gs.Exponential(dim=2)
    foo, foo2, r2 = fit_model.fit_variogram(bin_center, gamma, nugget=True, 
                                            max_eval=10000, return_r2=True)
#    print(r2)
    return fit_model, r2


if __name__ == '__main__':
    
    df = io.init_df()
    
    site_id = "Aa_river"
    direction = "x"
    meta_data = get_meta_data(site_id, direction)
    bin_center, gamma = get_empirical_variogram(site_id, direction)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1])
    direction = "z"
    meta_data = get_meta_data(site_id, direction)
    bin_center, gamma = get_empirical_variogram(site_id = site_id, 
                                                direction = direction)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1])
    
    site_id = "Aa_river_weir_2"
    direction = "x"
    meta_data = get_meta_data(site_id, direction)
    bin_center, gamma = get_empirical_variogram(site_id, direction)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1])
    
    site_id = "Alamitos_saltwater_intrusion_barrier"
    geological_unit = "1/2"
    direction = "x"
    meta_data = get_meta_data(site_id, direction, geological_unit)
    bin_center, gamma = get_empirical_variogram(site_id, direction, geological_unit)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1]) 
    geological_unit = "2/2"
    direction = "x"
    meta_data = get_meta_data(site_id, direction, geological_unit)
    bin_center, gamma = get_empirical_variogram(site_id, direction, geological_unit)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1]) 
    
    site_id = "Alberta_basin"
    meta_data = get_meta_data(site_id)
    bin_center, gamma = get_empirical_variogram(site_id = site_id)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1])
    
    site_id = "Algerita_escarpment"
    meta_data = get_meta_data(site_id)
    bin_center, gamma = get_empirical_variogram(site_id = site_id)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1])
    
    site_id = "Almonte-Marismas_groundwater_system"
    meta_data = get_meta_data(site_id)
    bin_center, gamma = get_empirical_variogram(site_id)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1])
    direction = "z"
    meta_data = get_meta_data(site_id, direction)
    bin_center, gamma = get_empirical_variogram(site_id, direction)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1])
    
    site_id = "Aspo_site"
    meta_data = get_meta_data(site_id)
    bin_center, gamma = get_empirical_variogram(site_id)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1])
    
    site_id = "Baishuihe_landslide"
    meta_data = get_meta_data(site_id)
    bin_center, gamma = get_empirical_variogram(site_id)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1])
    
    site_id = "Barry_Steam_Plant_site"
    geological_unit = "1/2"
    direction = "x"
    meta_data = get_meta_data(site_id, direction, geological_unit)
    bin_center, gamma = get_empirical_variogram(site_id, direction, geological_unit)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1]) 
    geological_unit = "2/2"
    direction = "x"
    meta_data = get_meta_data(site_id, direction, geological_unit)
    bin_center, gamma = get_empirical_variogram(site_id, direction, geological_unit)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1]) 
    
    site_id = "Beijing_synchrotron_microtomography"
    meta_data = get_meta_data(site_id)
    bin_center, gamma = get_empirical_variogram(site_id)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1])
    direction = "y"
    meta_data = get_meta_data(site_id, direction)
    bin_center, gamma = get_empirical_variogram(site_id, direction)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1])
    direction = "z"
    meta_data = get_meta_data(site_id, direction)
    bin_center, gamma = get_empirical_variogram(site_id, direction)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1])
    
    site_id = "Belridge_field"
    meta_data = get_meta_data(site_id)
    bin_center, gamma = get_empirical_variogram(site_id)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1])
    direction = "z"
    meta_data = get_meta_data(site_id, direction)
    bin_center, gamma = get_empirical_variogram(site_id, direction)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1])
    
    site_id = "Belgian_nuclear_repository"
    meta_data = get_meta_data(site_id)
    bin_center, gamma = get_empirical_variogram(site_id)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1])
    
    site_id = "Berea_sandstone"
    meta_data = get_meta_data(site_id)
    bin_center, gamma = get_empirical_variogram(site_id)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1])
#    
#    site_id = "Bierbeek_quarry"
#    direction = "x"
#    geological_unit = "1/2"
#    meta_data = get_meta_data(site_id, direction, geological_unit)
#    bin_center, gamma = get_empirical_variogram(site_id, direction,
#                                                geological_unit)
#    fit_model, r2 = fit_model_variogram(bin_center, gamma)
#    df = io.fill_df(df, meta_data, model = fit_model, 
#                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1])
#    direction = "x"
#    geological_unit = "2/2"
#    meta_data = get_meta_data(site_id, direction, geological_unit)
#    bin_center, gamma = get_empirical_variogram(site_id, direction,
#                                                geological_unit)
#    fit_model, r2 = fit_model_variogram(bin_center, gamma)
#    df = io.fill_df(df, meta_data, model = fit_model, 
#                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1])
    
    site_id = "Biscayne_aquifer"
    direction = "x"
    meta_data = get_meta_data(site_id, direction)
    bin_center, gamma = get_empirical_variogram(site_id, direction)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1])
    direction = "z"
    meta_data = get_meta_data(site_id, direction)
    bin_center, gamma = get_empirical_variogram(site_id, direction)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1])
    
    site_id = "Boise_site"
    direction = "x"
    meta_data = get_meta_data(site_id, direction)
    bin_center, gamma = get_empirical_variogram(site_id, direction)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1])
    direction = "z"
    meta_data = get_meta_data(site_id, direction)
    bin_center, gamma = get_empirical_variogram(site_id, direction)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1])
    
    site_id = "Boom_Clay_formation"
    direction = "x"
    meta_data = get_meta_data(site_id, direction)
    bin_center, gamma = get_empirical_variogram(site_id, direction)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1])

    site_id = "Boom_clay_formation_Mol_site"
    direction = "x"
    meta_data = get_meta_data(site_id, direction)
    bin_center, gamma = get_empirical_variogram(site_id, direction)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1])
    
    site_id = "Borden_aquifer"
    direction = "x"
    meta_data = get_meta_data(site_id, direction)
    bin_center, gamma = get_empirical_variogram(site_id, direction)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1])
    direction = "z"
    meta_data = get_meta_data(site_id, direction)
    bin_center, gamma = get_empirical_variogram(site_id, direction)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1])
    
    site_id = "Bosque_site"
    direction = "x"
    meta_data = get_meta_data(site_id, direction)
    bin_center, gamma = get_empirical_variogram(site_id, direction)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1])
    direction = "z"
    meta_data = get_meta_data(site_id, direction)
    bin_center, gamma = get_empirical_variogram(site_id, direction)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1]) 
    
    site_id = "Bouteldja_aquifer"
    direction = "x"
    meta_data = get_meta_data(site_id, direction)
    bin_center, gamma = get_empirical_variogram(site_id, direction)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1])   

    site_id = "Cape_Cod_aquifer"
    direction = "x"
    meta_data = get_meta_data(site_id, direction)
    bin_center, gamma = get_empirical_variogram(site_id, direction)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1]) 
    direction = "z"
    meta_data = get_meta_data(site_id, direction)
    bin_center, gamma = get_empirical_variogram(site_id, direction)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1]) 
    
    site_id = "Carrizo_aquifer"
    direction = "x"
    meta_data = get_meta_data(site_id, direction)
    bin_center, gamma = get_empirical_variogram(site_id, direction)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1]) 

    site_id = "Cengio_chemical_facility"
    direction = "x"
    meta_data = get_meta_data(site_id, direction)
    bin_center, gamma = get_empirical_variogram(site_id, direction)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1])    

    site_id = "Chicot_aquifer"
    direction = "x"
    meta_data = get_meta_data(site_id, direction)
    bin_center, gamma = get_empirical_variogram(site_id, direction)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1]) 

    site_id = "Choushui_river_alluvial_fan"
    direction = "x"
    geological_unit = "1/3"
    meta_data = get_meta_data(site_id, direction, geological_unit)
    bin_center, gamma = get_empirical_variogram(site_id, direction, geological_unit)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1])
    direction = "x"
    geological_unit = "2/3"
    meta_data = get_meta_data(site_id, direction, geological_unit)
    bin_center, gamma = get_empirical_variogram(site_id, direction, geological_unit)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1])
    direction = "x"
    geological_unit = "3/3"
    meta_data = get_meta_data(site_id, direction, geological_unit)
    bin_center, gamma = get_empirical_variogram(site_id, direction, geological_unit)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1])
    
    site_id = "Clyde_Basin"
    direction = "x"
    meta_data = get_meta_data(site_id, direction)
    bin_center, gamma = get_empirical_variogram(site_id = site_id)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1])
    direction = "z"
    meta_data = get_meta_data(site_id, direction)
    bin_center, gamma = get_empirical_variogram(site_id, direction)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1])
    
    site_id = "Dammam_aquifer"
    meta_data = get_meta_data(site_id = site_id)
    bin_center, gamma = get_empirical_variogram(site_id = site_id)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1])
    
    site_id = "Drau_valley"
    direction = "x"
    meta_data = get_meta_data(site_id, direction)
    bin_center, gamma = get_empirical_variogram(site_id, direction)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1])
    direction = "z"
    meta_data = get_meta_data(site_id, direction)
    bin_center, gamma = get_empirical_variogram(site_id, direction)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1])
    
    site_id = "Dulliu_area"
    direction = "x"
    meta_data = get_meta_data(site_id, direction)
    bin_center, gamma = get_empirical_variogram(site_id, direction)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1])   
    
    site_id = "Enfida_plain"
    direction = "x"
    meta_data = get_meta_data(site_id, direction)
    bin_center, gamma = get_empirical_variogram(site_id, direction)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1])
    
    site_id = "Eocene_Ainsa_basin"
    direction = "x"
    meta_data = get_meta_data(site_id, direction)
    bin_center, gamma = get_empirical_variogram(site_id, direction)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1])
    direction = "z"
    meta_data = get_meta_data(site_id, direction)
    bin_center, gamma = get_empirical_variogram(site_id, direction)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1]) 
    
    site_id = "Euganean_basin"
    direction = "x"
    meta_data = get_meta_data(site_id, direction)
    bin_center, gamma = get_empirical_variogram(site_id, direction)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1]) 
    direction = "y"
    meta_data = get_meta_data(site_id, direction)
    bin_center, gamma = get_empirical_variogram(site_id, direction)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1])
    
    site_id = "Experimental_EarthScape_facility"
    geological_unit = "1/12"
    direction = "x"
    meta_data = get_meta_data(site_id, direction, geological_unit)
    bin_center, gamma = get_empirical_variogram(site_id, direction, geological_unit)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1]) 
    geological_unit = "1/12"
    direction = "z"
    meta_data = get_meta_data(site_id, direction, geological_unit)
    bin_center, gamma = get_empirical_variogram(site_id, direction, geological_unit)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1]) 
    geological_unit = "2/12"
    direction = "x"
    meta_data = get_meta_data(site_id, direction, geological_unit)
    bin_center, gamma = get_empirical_variogram(site_id, direction, geological_unit)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1]) 
    geological_unit = "2/12"
    direction = "z"
    meta_data = get_meta_data(site_id, direction, geological_unit)
    bin_center, gamma = get_empirical_variogram(site_id, direction, geological_unit)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1]) 
    geological_unit = "3/12"
    direction = "x"
    meta_data = get_meta_data(site_id, direction, geological_unit)
    bin_center, gamma = get_empirical_variogram(site_id, direction, geological_unit)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1]) 
    geological_unit = "3/12"
    direction = "z"
    meta_data = get_meta_data(site_id, direction, geological_unit)
    bin_center, gamma = get_empirical_variogram(site_id, direction, geological_unit)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1]) 
    geological_unit = "4/12"
    direction = "x"
    meta_data = get_meta_data(site_id, direction, geological_unit)
    bin_center, gamma = get_empirical_variogram(site_id, direction, geological_unit)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1]) 
    geological_unit = "4/12"
    direction = "z"
    meta_data = get_meta_data(site_id, direction, geological_unit)
    bin_center, gamma = get_empirical_variogram(site_id, direction, geological_unit)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1]) 
    geological_unit = "5/12"
    direction = "x"
    meta_data = get_meta_data(site_id, direction, geological_unit)
    bin_center, gamma = get_empirical_variogram(site_id, direction, geological_unit)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1]) 
    geological_unit = "5/12"
    direction = "z"
    meta_data = get_meta_data(site_id, direction, geological_unit)
    bin_center, gamma = get_empirical_variogram(site_id, direction, geological_unit)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1]) 
    geological_unit = "6/12"
    direction = "x"
    meta_data = get_meta_data(site_id, direction, geological_unit)
    bin_center, gamma = get_empirical_variogram(site_id, direction, geological_unit)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1]) 
    geological_unit = "6/12"
    direction = "z"
    meta_data = get_meta_data(site_id, direction, geological_unit)
    bin_center, gamma = get_empirical_variogram(site_id, direction, geological_unit)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1]) 
    geological_unit = "7/12"
    direction = "x"
    meta_data = get_meta_data(site_id, direction, geological_unit)
    bin_center, gamma = get_empirical_variogram(site_id, direction, geological_unit)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1]) 
    geological_unit = "7/12"
    direction = "z"
    meta_data = get_meta_data(site_id, direction, geological_unit)
    bin_center, gamma = get_empirical_variogram(site_id, direction, geological_unit)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1]) 
    geological_unit = "8/12"
    direction = "x"
    meta_data = get_meta_data(site_id, direction, geological_unit)
    bin_center, gamma = get_empirical_variogram(site_id, direction, geological_unit)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1]) 
    geological_unit = "8/12"
    direction = "z"
    meta_data = get_meta_data(site_id, direction, geological_unit)
    bin_center, gamma = get_empirical_variogram(site_id, direction, geological_unit)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1]) 
    geological_unit = "9/12"
    direction = "x"
    meta_data = get_meta_data(site_id, direction, geological_unit)
    bin_center, gamma = get_empirical_variogram(site_id, direction, geological_unit)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1]) 
    geological_unit = "9/12"
    direction = "z"
    meta_data = get_meta_data(site_id, direction, geological_unit)
    bin_center, gamma = get_empirical_variogram(site_id, direction, geological_unit)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1]) 
#    geological_unit = "10/12"
#    direction = "x"
#    meta_data = get_meta_data(site_id, direction, geological_unit)
#    bin_center, gamma = get_empirical_variogram(site_id, direction, geological_unit)
#    fit_model, r2 = fit_model_variogram(bin_center, gamma)
#    df = io.fill_df(df, meta_data, model = fit_model, 
#                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1])  
#    geological_unit = "10/12"
#    direction = "z"
#    meta_data = get_meta_data(site_id, direction, geological_unit)
#    bin_center, gamma = get_empirical_variogram(site_id, direction, geological_unit)
#    fit_model, r2 = fit_model_variogram(bin_center, gamma)
#    df = io.fill_df(df, meta_data, model = fit_model, 
#                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1]) 
#    geological_unit = "11/12"
#    direction = "x"
#    meta_data = get_meta_data(site_id, direction, geological_unit)
#    bin_center, gamma = get_empirical_variogram(site_id, direction, geological_unit)
#    fit_model, r2 = fit_model_variogram(bin_center, gamma)
#    df = io.fill_df(df, meta_data, model = fit_model, 
#                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1])  
#    geological_unit = "11/12"
#    direction = "z"
#    meta_data = get_meta_data(site_id, direction, geological_unit)
#    bin_center, gamma = get_empirical_variogram(site_id, direction, geological_unit)
#    fit_model, r2 = fit_model_variogram(bin_center, gamma)
#    df = io.fill_df(df, meta_data, model = fit_model, 
#                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1])  
#    geological_unit = "12/12"
#    direction = "x"
#    meta_data = get_meta_data(site_id, direction, geological_unit)
#    bin_center, gamma = get_empirical_variogram(site_id, direction, geological_unit)
#    fit_model, r2 = fit_model_variogram(bin_center, gamma)
#    df = io.fill_df(df, meta_data, model = fit_model, 
#                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1])    
#    geological_unit = "12/12"
#    direction = "z"
#    meta_data = get_meta_data(site_id, direction, geological_unit)
#    bin_center, gamma = get_empirical_variogram(site_id, direction, geological_unit)
#    fit_model, r2 = fit_model_variogram(bin_center, gamma)
#    df = io.fill_df(df, meta_data, model = fit_model, 
#                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1])  
        
    site_id = "Fanshawe_section_gravel_pit"
    direction = "x"
    meta_data = get_meta_data(site_id, direction)
    bin_center, gamma = get_empirical_variogram(site_id, direction)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1])  
    site_id = "Fanshawe_section_gravel_pit"
    direction = "z"
    meta_data = get_meta_data(site_id, direction)
    bin_center, gamma = get_empirical_variogram(site_id, direction)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1]) 
        
    site_id = "Finnsjon_area"
    direction = "x"
    geological_unit = "1/2"
    meta_data = get_meta_data(site_id, direction, geological_unit)
    bin_center, gamma = get_empirical_variogram(site_id, direction, geological_unit)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1]) 
    direction = "x"
    geological_unit = "2/2"
    meta_data = get_meta_data(site_id, direction, geological_unit)
    bin_center, gamma = get_empirical_variogram(site_id, direction, geological_unit)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1]) 
#    
#    site_id = "Fontainebleau_sandstone_Paris_basin"
#    direction = "x"
#    meta_data = get_meta_data(site_id, direction)
#    bin_center, gamma = get_empirical_variogram(site_id, direction)
#    fit_model, r2 = fit_model_variogram(bin_center, gamma)
#    df = io.fill_df(df, meta_data, model = fit_model, 
#                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1])   
    
    site_id = "Georgetown_site"
    geological_unit = "1/3"
    direction = "x"
    meta_data = get_meta_data(site_id, direction, geological_unit)
    bin_center, gamma = get_empirical_variogram(site_id, direction, geological_unit)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1])  
    geological_unit = "2/3"
    direction = "x"
    meta_data = get_meta_data(site_id, direction, geological_unit)
    bin_center, gamma = get_empirical_variogram(site_id, direction, geological_unit)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1])
    geological_unit = "3/3"
    direction = "x"
    meta_data = get_meta_data(site_id, direction, geological_unit)
    bin_center, gamma = get_empirical_variogram(site_id, direction, geological_unit)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1])
    
    site_id = "Hanford_site"
    geological_unit = "1/1"
    direction = "x"
    meta_data = get_meta_data(site_id, direction, geological_unit)
    bin_center, gamma = get_empirical_variogram(site_id, direction, geological_unit)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1])
    geological_unit = "1/1"
    direction = "z"
    meta_data = get_meta_data(site_id, direction, geological_unit)
    bin_center, gamma = get_empirical_variogram(site_id, direction, geological_unit)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1])
    
    site_id = "Hawaii_aquifer_Maui"
    geological_unit = "1/1"
    direction = "x"
    meta_data = get_meta_data(site_id, direction, geological_unit)
    bin_center, gamma = get_empirical_variogram(site_id, direction, geological_unit)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1])
    
    site_id = "Hawaii_aquifer_Oahu"
    geological_unit = "1/1"
    direction = "x"
    meta_data = get_meta_data(site_id, direction, geological_unit)
    bin_center, gamma = get_empirical_variogram(site_id, direction, geological_unit)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1])
    
    site_id = "Heihe_River_basin"
    geological_unit = "1/1"
    direction = "x"
    meta_data = get_meta_data(site_id, direction, geological_unit)
    bin_center, gamma = get_empirical_variogram(site_id, direction, geological_unit)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1])
    
    site_id = "Herten_site"
    geological_unit = "1/1"
    direction = "x"
    meta_data = get_meta_data(site_id, direction, geological_unit)
    bin_center, gamma = get_empirical_variogram(site_id, direction, geological_unit)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1])

    site_id = "Hyderabad"
    geological_unit = "1/1"
    direction = "x"
    meta_data = get_meta_data(site_id, direction, geological_unit)
    bin_center, gamma = get_empirical_variogram(site_id, direction, geological_unit)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1])  
    
    site_id = "Jacksonburg_Stringtown_oil_field"
    geological_unit = "1/1"
    direction = "x"
    meta_data = get_meta_data(site_id, direction, geological_unit)
    bin_center, gamma = get_empirical_variogram(site_id, direction, geological_unit)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1])
    geological_unit = "1/1"
    direction = "y"
    meta_data = get_meta_data(site_id, direction, geological_unit)
    bin_center, gamma = get_empirical_variogram(site_id, direction, geological_unit)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1])
    geological_unit = "1/1"
    direction = "z"
    meta_data = get_meta_data(site_id, direction, geological_unit)
    bin_center, gamma = get_empirical_variogram(site_id, direction, geological_unit)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1])
    
    site_id = "Jianghan_Plain"
    geological_unit = "1/1"
    direction = "x"
    meta_data = get_meta_data(site_id, direction, geological_unit)
    bin_center, gamma = get_empirical_variogram(site_id, direction, geological_unit)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1])
    site_id = "Jianghan_Plain"
    geological_unit = "1/1"
    direction = "y"
    meta_data = get_meta_data(site_id, direction, geological_unit)
    bin_center, gamma = get_empirical_variogram(site_id, direction, geological_unit)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1])
    
    site_id = "Krauthausen_field"
    geological_unit = "1/1"
    direction = "x"
    meta_data = get_meta_data(site_id, direction, geological_unit)
    bin_center, gamma = get_empirical_variogram(site_id, direction, geological_unit)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1])
    geological_unit = "1/1"
    direction = "z"
    meta_data = get_meta_data(site_id, direction, geological_unit)
    bin_center, gamma = get_empirical_variogram(site_id, direction, geological_unit)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1])
    
    site_id = "Kiso_river"
    geological_unit = "1/1"
    direction = "x"
    meta_data = get_meta_data(site_id, direction, geological_unit)
    bin_center, gamma = get_empirical_variogram(site_id, direction, geological_unit)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1])
    
    site_id = "Lauswiesen_site"
    geological_unit = "1/2"
    direction = "x"
    meta_data = get_meta_data(site_id, direction, geological_unit)
    bin_center, gamma = get_empirical_variogram(site_id, direction, geological_unit)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1])  
    geological_unit = "2/2"
    direction = "x"
    meta_data = get_meta_data(site_id, direction, geological_unit)
    bin_center, gamma = get_empirical_variogram(site_id, direction, geological_unit)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1])
        
    site_id = "Libertador_General_Bernardos_O_Higgins_region"
    geological_unit = "1/1"
    direction = "x"
    meta_data = get_meta_data(site_id, direction, geological_unit)
    bin_center, gamma = get_empirical_variogram(site_id, direction, geological_unit)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1])   
        
    site_id = "LLNL_upper_aquifer"
    geological_unit = "1/1"
    direction = "x"
    meta_data = get_meta_data(site_id, direction, geological_unit)
    bin_center, gamma = get_empirical_variogram(site_id, direction, geological_unit)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1])    
    site_id = "LLNL_upper_aquifer"
    geological_unit = "1/1"
    direction = "y"
    meta_data = get_meta_data(site_id, direction, geological_unit)
    bin_center, gamma = get_empirical_variogram(site_id, direction, geological_unit)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1])     
        
    site_id = "Lower_Cretaceous_Viking_formation"
    geological_unit = "1/1"
    direction = "x"
    meta_data = get_meta_data(site_id, direction, geological_unit)
    bin_center, gamma = get_empirical_variogram(site_id, direction, geological_unit)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1]) 
    geological_unit = "1/1"
    direction = "z"
    meta_data = get_meta_data(site_id, direction, geological_unit)
    bin_center, gamma = get_empirical_variogram(site_id, direction, geological_unit)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1]) 
    
    site_id = "Lower_Triassic_sandstones_Scrabo_quarry"
    geological_unit = "1/8"
    direction = "x"
    meta_data = get_meta_data(site_id, direction, geological_unit)
    bin_center, gamma = get_empirical_variogram(site_id, direction, geological_unit)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1])     
    geological_unit = "2/8"
    direction = "x"
    meta_data = get_meta_data(site_id, direction, geological_unit)
    bin_center, gamma = get_empirical_variogram(site_id, direction, geological_unit)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1])
    geological_unit = "3/8"
    direction = "x"
    meta_data = get_meta_data(site_id, direction, geological_unit)
    bin_center, gamma = get_empirical_variogram(site_id, direction, geological_unit)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1])
    geological_unit = "4/8"
    direction = "x"
    meta_data = get_meta_data(site_id, direction, geological_unit)
    bin_center, gamma = get_empirical_variogram(site_id, direction, geological_unit)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1])
    geological_unit = "5/8"
    direction = "x"
    meta_data = get_meta_data(site_id, direction, geological_unit)
    bin_center, gamma = get_empirical_variogram(site_id, direction, geological_unit)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1])
    geological_unit = "6/8"
    direction = "x"
    meta_data = get_meta_data(site_id, direction, geological_unit)
    bin_center, gamma = get_empirical_variogram(site_id, direction, geological_unit)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1])
    geological_unit = "7/8"
    direction = "x"
    meta_data = get_meta_data(site_id, direction, geological_unit)
    bin_center, gamma = get_empirical_variogram(site_id, direction, geological_unit)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1])
    geological_unit = "8/8"
    direction = "x"
    meta_data = get_meta_data(site_id, direction, geological_unit)
    bin_center, gamma = get_empirical_variogram(site_id, direction, geological_unit)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1])
    
    site_id = "MADE_site"
    geological_unit = "1/1"
    direction = "x"
    meta_data = get_meta_data(site_id, direction, geological_unit)
    bin_center, gamma = get_empirical_variogram(site_id, direction, geological_unit)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1])   
    geological_unit = "1/1"
    direction = "z"
    meta_data = get_meta_data(site_id, direction, geological_unit)
    bin_center, gamma = get_empirical_variogram(site_id, direction, geological_unit)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1])   
   
    site_id = "Man-Danane_region"
    geological_unit = "1/1"
    direction = "x"
    meta_data = get_meta_data(site_id, direction, geological_unit)
    bin_center, gamma = get_empirical_variogram(site_id, direction, geological_unit)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1])  
    
    site_id = "Mirror_Lake_site"
    geological_unit = "1/1"
    direction = "x"
    meta_data = get_meta_data(site_id, direction, geological_unit)
    bin_center, gamma = get_empirical_variogram(site_id, direction, geological_unit)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1]) 
    geological_unit = "1/1"
    direction = "z"
    meta_data = get_meta_data(site_id, direction, geological_unit)
    bin_center, gamma = get_empirical_variogram(site_id, direction, geological_unit)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1]) 
    
    site_id = "Neogene_aquifer"
    geological_unit = "1/1"
    direction = "x"
    meta_data = get_meta_data(site_id, direction, geological_unit)
    bin_center, gamma = get_empirical_variogram(site_id, direction, geological_unit)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1])
    
    site_id = "Nord_Pas_de_Calais"
    geological_unit = "1/1"
    direction = "x"
    meta_data = get_meta_data(site_id, direction, geological_unit)
    bin_center, gamma = get_empirical_variogram(site_id, direction, geological_unit)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1])     
    
    site_id = "North_German_basin"
    geological_unit = "1/4"
    direction = "x"
    meta_data = get_meta_data(site_id, direction, geological_unit)
    bin_center, gamma = get_empirical_variogram(site_id, direction, geological_unit)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1]) 
    geological_unit = "2/4"
    direction = "x"
    meta_data = get_meta_data(site_id, direction, geological_unit)
    bin_center, gamma = get_empirical_variogram(site_id, direction, geological_unit)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1]) 
    geological_unit = "3/4"
    direction = "x"
    meta_data = get_meta_data(site_id, direction, geological_unit)
    bin_center, gamma = get_empirical_variogram(site_id, direction, geological_unit)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1])   
    geological_unit = "4/4"
    direction = "x"
    meta_data = get_meta_data(site_id, direction, geological_unit)
    bin_center, gamma = get_empirical_variogram(site_id, direction, geological_unit)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1])  
    
    site_id = "Northwestern_Sahara_basin_CI_aquifer"
    geological_unit = "1/1"
    direction = "x"
    meta_data = get_meta_data(site_id, direction, geological_unit)
    bin_center, gamma = get_empirical_variogram(site_id, direction, geological_unit)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1]) 
    
    site_id = "Northwestern_Sahara_basin_CT_aquifer"
    geological_unit = "1/1"
    direction = "x"
    meta_data = get_meta_data(site_id, direction, geological_unit)
    bin_center, gamma = get_empirical_variogram(site_id, direction, geological_unit)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1])      
    
    site_id = "Nubian_Sandstone_aquifer"
    geological_unit = "1/1"
    direction = "x"
    meta_data = get_meta_data(site_id, direction, geological_unit)
    bin_center, gamma = get_empirical_variogram(site_id, direction, geological_unit)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1])  
    geological_unit = "1/1"
    direction = "y"
    meta_data = get_meta_data(site_id, direction, geological_unit)
    bin_center, gamma = get_empirical_variogram(site_id, direction, geological_unit)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1])      
     
    site_id = "Obersulzbach_sandstone_quarry_outcrop"
    geological_unit = "1/2"
    direction = "x"
    meta_data = get_meta_data(site_id, direction, geological_unit)
    bin_center, gamma = get_empirical_variogram(site_id, direction, geological_unit)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1]) 
    geological_unit = "2/2"
    direction = "x"
    meta_data = get_meta_data(site_id, direction, geological_unit)
    bin_center, gamma = get_empirical_variogram(site_id, direction, geological_unit)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1])    
    
    site_id = "Oligocene_Huagang_Formation"
    geological_unit = "1/1"
    direction = "x"
    meta_data = get_meta_data(site_id, direction, geological_unit)
    bin_center, gamma = get_empirical_variogram(site_id, direction, geological_unit)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1])       
    
    site_id = "Pingtung_plain"
    geological_unit = "1/3"
    direction = "x"
    meta_data = get_meta_data(site_id, direction, geological_unit)
    bin_center, gamma = get_empirical_variogram(site_id, direction, geological_unit)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1])  
    geological_unit = "2/3"
    direction = "x"
    meta_data = get_meta_data(site_id, direction, geological_unit)
    bin_center, gamma = get_empirical_variogram(site_id, direction, geological_unit)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1]) 
    geological_unit = "3/3"
    direction = "x"
    meta_data = get_meta_data(site_id, direction, geological_unit)
    bin_center, gamma = get_empirical_variogram(site_id, direction, geological_unit)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1])   

    site_id = "Plain_of_Haouz"
    geological_unit = "1/1"
    direction = "x"
    meta_data = get_meta_data(site_id, direction, geological_unit)
    bin_center, gamma = get_empirical_variogram(site_id, direction, geological_unit)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1])   
    geological_unit = "1/1"
    direction = "y"
    meta_data = get_meta_data(site_id, direction, geological_unit)
    bin_center, gamma = get_empirical_variogram(site_id, direction, geological_unit)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1]) 

    site_id = "Platte_river"
    geological_unit = "1/1"
    direction = "x"
    meta_data = get_meta_data(site_id, direction, geological_unit)
    bin_center, gamma = get_empirical_variogram(site_id, direction, geological_unit)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1])

    site_id = "Prairie_Creek_test_site"
    geological_unit = "1/3"
    direction = "x"
    meta_data = get_meta_data(site_id, direction, geological_unit)
    bin_center, gamma = get_empirical_variogram(site_id, direction, geological_unit)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1])
    geological_unit = "2/3"
    direction = "x"
    meta_data = get_meta_data(site_id, direction, geological_unit)
    bin_center, gamma = get_empirical_variogram(site_id, direction, geological_unit)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1])
    geological_unit = "3/3"
    direction = "x"
    meta_data = get_meta_data(site_id, direction, geological_unit)
    bin_center, gamma = get_empirical_variogram(site_id, direction, geological_unit)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1])

    site_id = "RMA_Superfund_site"
    geological_unit = "1/1"
    direction = "x"
    meta_data = get_meta_data(site_id, direction, geological_unit)
    bin_center, gamma = get_empirical_variogram(site_id, direction, geological_unit)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1])

    site_id = "Sand_box_US"
    geological_unit = "1/1"
    direction = "x"
    meta_data = get_meta_data(site_id, direction, geological_unit)
    bin_center, gamma = get_empirical_variogram(site_id, direction, geological_unit)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1])

    site_id = "San_Pedro_area"
    geological_unit = "1/1"
    direction = "x"
    meta_data = get_meta_data(site_id, direction, geological_unit)
    bin_center, gamma = get_empirical_variogram(site_id, direction, geological_unit)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1])

    site_id = "Savannah_River_site"
    geological_unit = "1/3"
    direction = "x"
    meta_data = get_meta_data(site_id, direction, geological_unit)
    bin_center, gamma = get_empirical_variogram(site_id, direction, geological_unit)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1])
    geological_unit = "1/3"
    direction = "y"
    meta_data = get_meta_data(site_id, direction, geological_unit)
    bin_center, gamma = get_empirical_variogram(site_id, direction, geological_unit)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1])
    geological_unit = "1/3"
    direction = "z"
    meta_data = get_meta_data(site_id, direction, geological_unit)
    bin_center, gamma = get_empirical_variogram(site_id, direction, geological_unit)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1])
    geological_unit = "2/3"
    direction = "x"
    meta_data = get_meta_data(site_id, direction, geological_unit)
    bin_center, gamma = get_empirical_variogram(site_id, direction, geological_unit)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1])
    geological_unit = "2/3"
    direction = "y"
    meta_data = get_meta_data(site_id, direction, geological_unit)
    bin_center, gamma = get_empirical_variogram(site_id, direction, geological_unit)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1])
    geological_unit = "2/3"
    direction = "z"
    meta_data = get_meta_data(site_id, direction, geological_unit)
    bin_center, gamma = get_empirical_variogram(site_id, direction, geological_unit)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1])
    geological_unit = "3/3"
    direction = "x"
    meta_data = get_meta_data(site_id, direction, geological_unit)
    bin_center, gamma = get_empirical_variogram(site_id, direction, geological_unit)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1])
    geological_unit = "3/3"
    direction = "y"
    meta_data = get_meta_data(site_id, direction, geological_unit)
    bin_center, gamma = get_empirical_variogram(site_id, direction, geological_unit)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1])
    geological_unit = "3/3"
    direction = "z"
    meta_data = get_meta_data(site_id, direction, geological_unit)
    bin_center, gamma = get_empirical_variogram(site_id, direction, geological_unit)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1])

    site_id = "Shurijeh-B_reservoir"
    geological_unit = "1/1"
    direction = "x"
    meta_data = get_meta_data(site_id, direction, geological_unit)
    bin_center, gamma = get_empirical_variogram(site_id, direction, geological_unit)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1])
    geological_unit = "1/1"
    direction = "z"
    meta_data = get_meta_data(site_id, direction, geological_unit)
    bin_center, gamma = get_empirical_variogram(site_id, direction, geological_unit)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1])

    site_id = "Sierra_Ladrones_formation"
    geological_unit = "1/1"
    direction = "x"
    meta_data = get_meta_data(site_id, direction, geological_unit)
    bin_center, gamma = get_empirical_variogram(site_id, direction, geological_unit)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1])
    geological_unit = "1/1"
    direction = "z"
    meta_data = get_meta_data(site_id, direction, geological_unit)
    bin_center, gamma = get_empirical_variogram(site_id, direction, geological_unit)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1])

    site_id = "Sindhudurg_district"
    geological_unit = "1/1"
    direction = "x"
    meta_data = get_meta_data(site_id, direction, geological_unit)
    bin_center, gamma = get_empirical_variogram(site_id, direction, geological_unit)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1])

    site_id = "Snake_River_aquifer"
    geological_unit = "1/1"
    direction = "x"
    meta_data = get_meta_data(site_id, direction, geological_unit)
    bin_center, gamma = get_empirical_variogram(site_id, direction, geological_unit)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1])
    geological_unit = "1/1"
    direction = "y"
    meta_data = get_meta_data(site_id, direction, geological_unit)
    bin_center, gamma = get_empirical_variogram(site_id, direction, geological_unit)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1])

    site_id = "South_Jingyang_Plateau"
    geological_unit = "1/2"
    direction = "x"
    meta_data = get_meta_data(site_id, direction, geological_unit)
    bin_center, gamma = get_empirical_variogram(site_id, direction, geological_unit)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1])
    geological_unit = "2/2"
    direction = "x"
    meta_data = get_meta_data(site_id, direction, geological_unit)
    bin_center, gamma = get_empirical_variogram(site_id, direction, geological_unit)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1])

    site_id = "South_Pars_gas_field"
    geological_unit = "1/1"
    direction = "x"
    meta_data = get_meta_data(site_id, direction, geological_unit)
    bin_center, gamma = get_empirical_variogram(site_id, direction, geological_unit)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1])
   
    site_id = "Southwest_China"
    geological_unit = "1/12"
    direction = "x"
    meta_data = get_meta_data(site_id, direction, geological_unit)
    bin_center, gamma = get_empirical_variogram(site_id, direction, geological_unit)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1]) 
    geological_unit = "2/12"
    direction = "x"
    meta_data = get_meta_data(site_id, direction, geological_unit)
    bin_center, gamma = get_empirical_variogram(site_id, direction, geological_unit)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1]) 
    geological_unit = "3/12"
    direction = "x"
    meta_data = get_meta_data(site_id, direction, geological_unit)
    bin_center, gamma = get_empirical_variogram(site_id, direction, geological_unit)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1])
    geological_unit = "4/12"
    direction = "x"
    meta_data = get_meta_data(site_id, direction, geological_unit)
    bin_center, gamma = get_empirical_variogram(site_id, direction, geological_unit)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1])  
    geological_unit = "5/12"
    direction = "x"
    meta_data = get_meta_data(site_id, direction, geological_unit)
    bin_center, gamma = get_empirical_variogram(site_id, direction, geological_unit)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1])  
    geological_unit = "6/12"
    direction = "x"
    meta_data = get_meta_data(site_id, direction, geological_unit)
    bin_center, gamma = get_empirical_variogram(site_id, direction, geological_unit)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1]) 
    geological_unit = "7/12"
    direction = "x"
    meta_data = get_meta_data(site_id, direction, geological_unit)
    bin_center, gamma = get_empirical_variogram(site_id, direction, geological_unit)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1]) 
    geological_unit = "8/12"
    direction = "x"
    meta_data = get_meta_data(site_id, direction, geological_unit)
    bin_center, gamma = get_empirical_variogram(site_id, direction, geological_unit)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1]) 
    geological_unit = "9/12"
    direction = "x"
    meta_data = get_meta_data(site_id, direction, geological_unit)
    bin_center, gamma = get_empirical_variogram(site_id, direction, geological_unit)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1])
    geological_unit = "10/12"
    direction = "x"
    meta_data = get_meta_data(site_id, direction, geological_unit)
    bin_center, gamma = get_empirical_variogram(site_id, direction, geological_unit)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1])
    geological_unit = "11/12"
    direction = "x"
    meta_data = get_meta_data(site_id, direction, geological_unit)
    bin_center, gamma = get_empirical_variogram(site_id, direction, geological_unit)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1])
    geological_unit = "12/12"
    direction = "x"
    meta_data = get_meta_data(site_id, direction, geological_unit)
    bin_center, gamma = get_empirical_variogram(site_id, direction, geological_unit)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1])
   
    site_id = "Takelsa_multilayer_aquifer"
    geological_unit = "1/1"
    direction = "x"
    meta_data = get_meta_data(site_id, direction, geological_unit)
    bin_center, gamma = get_empirical_variogram(site_id, direction, geological_unit)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1]) 
   
    site_id = "Ticino_valley"
    geological_unit = "1/8"
    direction = "x"
    meta_data = get_meta_data(site_id, direction, geological_unit)
    bin_center, gamma = get_empirical_variogram(site_id, direction, geological_unit)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1]) 
    geological_unit = "1/8"
    direction = "y"
    meta_data = get_meta_data(site_id, direction, geological_unit)
    bin_center, gamma = get_empirical_variogram(site_id, direction, geological_unit)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1]) 
    geological_unit = "1/8"
    direction = "z"
    meta_data = get_meta_data(site_id, direction, geological_unit)
    bin_center, gamma = get_empirical_variogram(site_id, direction, geological_unit)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1]) 
    geological_unit = "2/8"
    direction = "x"
    meta_data = get_meta_data(site_id, direction, geological_unit)
    bin_center, gamma = get_empirical_variogram(site_id, direction, geological_unit)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1]) 
    geological_unit = "2/8"
    direction = "y"
    meta_data = get_meta_data(site_id, direction, geological_unit)
    bin_center, gamma = get_empirical_variogram(site_id, direction, geological_unit)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1]) 
    geological_unit = "2/8"
    direction = "z"
    meta_data = get_meta_data(site_id, direction, geological_unit)
    bin_center, gamma = get_empirical_variogram(site_id, direction, geological_unit)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1]) 
    geological_unit = "3/8"
    direction = "x"
    meta_data = get_meta_data(site_id, direction, geological_unit)
    bin_center, gamma = get_empirical_variogram(site_id, direction, geological_unit)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1]) 
    geological_unit = "3/8"
    direction = "y"
    meta_data = get_meta_data(site_id, direction, geological_unit)
    bin_center, gamma = get_empirical_variogram(site_id, direction, geological_unit)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1]) 
    geological_unit = "3/8"
    direction = "z"
    meta_data = get_meta_data(site_id, direction, geological_unit)
    bin_center, gamma = get_empirical_variogram(site_id, direction, geological_unit)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1]) 
    geological_unit = "4/8"
    direction = "x"
    meta_data = get_meta_data(site_id, direction, geological_unit)
    bin_center, gamma = get_empirical_variogram(site_id, direction, geological_unit)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1]) 
    geological_unit = "4/8"
    direction = "y"
    meta_data = get_meta_data(site_id, direction, geological_unit)
    bin_center, gamma = get_empirical_variogram(site_id, direction, geological_unit)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1]) 
    geological_unit = "4/8"
    direction = "z"
    meta_data = get_meta_data(site_id, direction, geological_unit)
    bin_center, gamma = get_empirical_variogram(site_id, direction, geological_unit)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1]) 
    geological_unit = "5/8"
    direction = "x"
    meta_data = get_meta_data(site_id, direction, geological_unit)
    bin_center, gamma = get_empirical_variogram(site_id, direction, geological_unit)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1]) 
    geological_unit = "5/8"
    direction = "y"
    meta_data = get_meta_data(site_id, direction, geological_unit)
    bin_center, gamma = get_empirical_variogram(site_id, direction, geological_unit)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1]) 
    geological_unit = "5/8"
    direction = "z"
    meta_data = get_meta_data(site_id, direction, geological_unit)
    bin_center, gamma = get_empirical_variogram(site_id, direction, geological_unit)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1]) 
    geological_unit = "6/8"
    direction = "x"
    meta_data = get_meta_data(site_id, direction, geological_unit)
    bin_center, gamma = get_empirical_variogram(site_id, direction, geological_unit)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1]) 
    geological_unit = "6/8"
    direction = "y"
    meta_data = get_meta_data(site_id, direction, geological_unit)
    bin_center, gamma = get_empirical_variogram(site_id, direction, geological_unit)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1])  
    geological_unit = "6/8"
    direction = "z"
    meta_data = get_meta_data(site_id, direction, geological_unit)
    bin_center, gamma = get_empirical_variogram(site_id, direction, geological_unit)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1]) 
    geological_unit = "7/8"
    direction = "x"
    meta_data = get_meta_data(site_id, direction, geological_unit)
    bin_center, gamma = get_empirical_variogram(site_id, direction, geological_unit)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1]) 
    geological_unit = "7/8"
    direction = "y"
    meta_data = get_meta_data(site_id, direction, geological_unit)
    bin_center, gamma = get_empirical_variogram(site_id, direction, geological_unit)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1])
    geological_unit = "7/8"
    direction = "z"
    meta_data = get_meta_data(site_id, direction, geological_unit)
    bin_center, gamma = get_empirical_variogram(site_id, direction, geological_unit)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1])
    geological_unit = "8/8"
    direction = "x"
    meta_data = get_meta_data(site_id, direction, geological_unit)
    bin_center, gamma = get_empirical_variogram(site_id, direction, geological_unit)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1]) 
    geological_unit = "8/8"
    direction = "y"
    meta_data = get_meta_data(site_id, direction, geological_unit)
    bin_center, gamma = get_empirical_variogram(site_id, direction, geological_unit)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1]) 
    geological_unit = "8/8"
    direction = "z"
    meta_data = get_meta_data(site_id, direction, geological_unit)
    bin_center, gamma = get_empirical_variogram(site_id, direction, geological_unit)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1])
   
    site_id = "Tono_uranium_deposit"
    geological_unit = "1/1"
    direction = "x"
    meta_data = get_meta_data(site_id, direction, geological_unit)
    bin_center, gamma = get_empirical_variogram(site_id, direction, geological_unit)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1]) 
    geological_unit = "1/1"
    direction = "z"
    meta_data = get_meta_data(site_id, direction, geological_unit)
    bin_center, gamma = get_empirical_variogram(site_id, direction, geological_unit)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1]) 
   
    site_id = "Topopah_Spring_tuff"
    geological_unit = "1/1"
    direction = "x"
    meta_data = get_meta_data(site_id, direction, geological_unit)
    bin_center, gamma = get_empirical_variogram(site_id, direction, geological_unit)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1]) 
    geological_unit = "1/1"
    direction = "y"
    meta_data = get_meta_data(site_id, direction, geological_unit)
    bin_center, gamma = get_empirical_variogram(site_id, direction, geological_unit)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1]) 
   
    site_id = "Triassic_Hawkesbury_sandstone_Sydney_basin"
    geological_unit = "1/2"
    direction = "x"
    meta_data = get_meta_data(site_id, direction, geological_unit)
    bin_center, gamma = get_empirical_variogram(site_id, direction, geological_unit)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1]) 
    geological_unit = "1/2"
    direction = "z"
    meta_data = get_meta_data(site_id, direction, geological_unit)
    bin_center, gamma = get_empirical_variogram(site_id, direction, geological_unit)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1]) 
    geological_unit = "2/2"
    direction = "x"
    meta_data = get_meta_data(site_id, direction, geological_unit)
    bin_center, gamma = get_empirical_variogram(site_id, direction, geological_unit)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1]) 
    geological_unit = "2/2"
    direction = "z"
    meta_data = get_meta_data(site_id, direction, geological_unit)
    bin_center, gamma = get_empirical_variogram(site_id, direction, geological_unit)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1]) 
   
    site_id = "Trifa_aquifer_north_zone"
    geological_unit = "1/1"
    direction = "x"
    meta_data = get_meta_data(site_id, direction, geological_unit)
    bin_center, gamma = get_empirical_variogram(site_id, direction, geological_unit)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1]) 
   
    site_id = "Trifa_aquifer_south_zone"
    geological_unit = "1/1"
    direction = "x"
    meta_data = get_meta_data(site_id, direction, geological_unit)
    bin_center, gamma = get_empirical_variogram(site_id, direction, geological_unit)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1]) 
   
    site_id = "Tuebingen_site"
    geological_unit = "1/1"
    direction = "x"
    meta_data = get_meta_data(site_id, direction, geological_unit)
    bin_center, gamma = get_empirical_variogram(site_id, direction, geological_unit)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1]) 
    geological_unit = "1/1"
    direction = "z"
    meta_data = get_meta_data(site_id, direction, geological_unit)
    bin_center, gamma = get_empirical_variogram(site_id, direction, geological_unit)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1])
   
    site_id = "Upper_Awash_basin"
    geological_unit = "1/1"
    direction = "x"
    meta_data = get_meta_data(site_id, direction, geological_unit)
    bin_center, gamma = get_empirical_variogram(site_id, direction, geological_unit)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1]) 
   
    site_id = "Upper_Jurassic_Ain_Dar_field"
    geological_unit = "1/1"
    direction = "x"
    meta_data = get_meta_data(site_id, direction, geological_unit)
    bin_center, gamma = get_empirical_variogram(site_id, direction, geological_unit)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1]) 
    geological_unit = "1/1"
    direction = "y"
    meta_data = get_meta_data(site_id, direction, geological_unit)
    bin_center, gamma = get_empirical_variogram(site_id, direction, geological_unit)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1]) 
   
    site_id = "Upper_Jurassic_Ghawar_field"
    geological_unit = "1/1"
    direction = "x"
    meta_data = get_meta_data(site_id, direction, geological_unit)
    bin_center, gamma = get_empirical_variogram(site_id, direction, geological_unit)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1]) 
    geological_unit = "1/1"
    direction = "y"
    meta_data = get_meta_data(site_id, direction, geological_unit)
    bin_center, gamma = get_empirical_variogram(site_id, direction, geological_unit)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1]) 
   
    site_id = "Upper_Jurassic_Haradh"
    geological_unit = "1/1"
    direction = "x"
    meta_data = get_meta_data(site_id, direction, geological_unit)
    bin_center, gamma = get_empirical_variogram(site_id, direction, geological_unit)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1]) 
    geological_unit = "1/1"
    direction = "y"
    meta_data = get_meta_data(site_id, direction, geological_unit)
    bin_center, gamma = get_empirical_variogram(site_id, direction, geological_unit)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1]) 
   
    site_id = "Upper_Maastrichtian_chalk_outcrops"
    geological_unit = "1/1"
    direction = "x"
    meta_data = get_meta_data(site_id, direction, geological_unit)
    bin_center, gamma = get_empirical_variogram(site_id, direction, geological_unit)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1])  
   
    site_id = "Upper_Ulayyah_reservoir"
    geological_unit = "1/5"
    direction = "x"
    meta_data = get_meta_data(site_id, direction, geological_unit)
    bin_center, gamma = get_empirical_variogram(site_id, direction, geological_unit)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1]) 
    geological_unit = "1/5"
    direction = "y"
    meta_data = get_meta_data(site_id, direction, geological_unit)
    bin_center, gamma = get_empirical_variogram(site_id, direction, geological_unit)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1]) 
    geological_unit = "1/5"
    direction = "z"
    meta_data = get_meta_data(site_id, direction, geological_unit)
    bin_center, gamma = get_empirical_variogram(site_id, direction, geological_unit)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1]) 
    geological_unit = "2/5"
    direction = "x"
    meta_data = get_meta_data(site_id, direction, geological_unit)
    bin_center, gamma = get_empirical_variogram(site_id, direction, geological_unit)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1]) 
    geological_unit = "2/5"
    direction = "y"
    meta_data = get_meta_data(site_id, direction, geological_unit)
    bin_center, gamma = get_empirical_variogram(site_id, direction, geological_unit)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1])
    geological_unit = "2/5"
    direction = "z"
    meta_data = get_meta_data(site_id, direction, geological_unit)
    bin_center, gamma = get_empirical_variogram(site_id, direction, geological_unit)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1])
    geological_unit = "3/5"
    direction = "x"
    meta_data = get_meta_data(site_id, direction, geological_unit)
    bin_center, gamma = get_empirical_variogram(site_id, direction, geological_unit)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1]) 
    geological_unit = "3/5"
    direction = "y"
    meta_data = get_meta_data(site_id, direction, geological_unit)
    bin_center, gamma = get_empirical_variogram(site_id, direction, geological_unit)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1]) 
    geological_unit = "3/5"
    direction = "z"
    meta_data = get_meta_data(site_id, direction, geological_unit)
    bin_center, gamma = get_empirical_variogram(site_id, direction, geological_unit)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1]) 
    geological_unit = "4/5"
    direction = "x"
    meta_data = get_meta_data(site_id, direction, geological_unit)
    bin_center, gamma = get_empirical_variogram(site_id, direction, geological_unit)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1]) 
    geological_unit = "4/5"
    direction = "y"
    meta_data = get_meta_data(site_id, direction, geological_unit)
    bin_center, gamma = get_empirical_variogram(site_id, direction, geological_unit)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1]) 
    geological_unit = "4/5"
    direction = "z"
    meta_data = get_meta_data(site_id, direction, geological_unit)
    bin_center, gamma = get_empirical_variogram(site_id, direction, geological_unit)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1]) 
    geological_unit = "5/5"
    direction = "x"
    meta_data = get_meta_data(site_id, direction, geological_unit)
    bin_center, gamma = get_empirical_variogram(site_id, direction, geological_unit)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1]) 
    geological_unit = "5/5"
    direction = "y"
    meta_data = get_meta_data(site_id, direction, geological_unit)
    bin_center, gamma = get_empirical_variogram(site_id, direction, geological_unit)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1]) 
    geological_unit = "5/5"
    direction = "z"
    meta_data = get_meta_data(site_id, direction, geological_unit)
    bin_center, gamma = get_empirical_variogram(site_id, direction, geological_unit)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1]) 
   
    site_id = "Vargem_de_Caldas_basin"
    geological_unit = "1/1"
    direction = "x"
    meta_data = get_meta_data(site_id, direction, geological_unit)
    bin_center, gamma = get_empirical_variogram(site_id, direction, geological_unit)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1]) 
    geological_unit = "1/1"
    direction = "y"
    meta_data = get_meta_data(site_id, direction, geological_unit)
    bin_center, gamma = get_empirical_variogram(site_id, direction, geological_unit)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1]) 
   
    site_id = "Waste_Isolation_Pilot_Plant_site"
    geological_unit = "1/1"
    direction = "x"
    meta_data = get_meta_data(site_id, direction, geological_unit)
    bin_center, gamma = get_empirical_variogram(site_id, direction, geological_unit)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1]) 
   
    site_id = "West_Bear_Creek_watershed"
    geological_unit = "1/1"
    direction = "x"
    meta_data = get_meta_data(site_id, direction, geological_unit)
    bin_center, gamma = get_empirical_variogram(site_id, direction, geological_unit)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1]) 
   
    site_id = "Western_Denmark"
    geological_unit = "1/3"
    direction = "x"
    meta_data = get_meta_data(site_id, direction, geological_unit)
    bin_center, gamma = get_empirical_variogram(site_id, direction, geological_unit)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1]) 
    geological_unit = "2/3"
    direction = "x"
    meta_data = get_meta_data(site_id, direction, geological_unit)
    bin_center, gamma = get_empirical_variogram(site_id, direction, geological_unit)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1]) 
    geological_unit = "3/3"
    direction = "x"
    meta_data = get_meta_data(site_id, direction, geological_unit)
    bin_center, gamma = get_empirical_variogram(site_id, direction, geological_unit)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1]) 
   
    site_id = "Yolo_basin"
    geological_unit = "1/1"
    direction = "x"
    meta_data = get_meta_data(site_id, direction, geological_unit)
    bin_center, gamma = get_empirical_variogram(site_id, direction, geological_unit)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1]) 
   
    site_id = "Yucca_Mountain"
    geological_unit = "1/1"
    direction = "x"
    meta_data = get_meta_data(site_id, direction, geological_unit)
    bin_center, gamma = get_empirical_variogram(site_id, direction, geological_unit)
    fit_model, r2 = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    r2 = r2, min_scale = bin_center[0], max_scale = bin_center[-1]) 
        
    
    io.write_df(df, path = '../results/aquifer_statistics_exponential.csv')
    
    
    # output
    ax = fit_model.plot(x_max=max(bin_center))
    plt.scatter(bin_center, gamma)
    plt.show()
    print(fit_model)
    