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
    variogram_data_df = pd.read_csv("../data/soil_variogram.csv")
    
    df = variogram_data_df[variogram_data_df['site_id']==site_id]
    df = df[df['direction']==direction]
    df = df[df['geological_unit']==geological_unit]
  
    return df.iloc[0]


def get_empirical_variogram(site_id, direction = "x", geological_unit = "1/1"):
    
    #read in data from a file
    variogram_data_df = pd.read_csv("../data/soil_variogram.csv")
    
    df = variogram_data_df[variogram_data_df['site_id']==site_id]
    df = df[df['direction']==direction]
    df = df[df['geological_unit']==geological_unit]
    
    bin_center = df["lag_m"].to_numpy()
    gamma = df["gamma"].to_numpy()
  
    return bin_center.astype(np.float), gamma.astype(np.float)


def fit_model_variogram(bin_center, gamma):
    
    # fit the variogram variogram with a stable model. (no nugget fitted)
#    fit_model = gs.Stable(dim=2)
#    fit_model = gs.Matern(dim=2)
#    fit_model = gs.Gaussian(dim=2)
    fit_model = gs.Exponential(dim=2)
    fit_model.fit_variogram(bin_center, gamma, nugget=True, max_eval=10000)
    return fit_model


if __name__ == '__main__':
    
    df = io.init_df()
    
#    site_id = "Alto_Rio_Grande_basin"
#    direction = "x"
#    meta_data = get_meta_data(site_id, direction)
#    bin_center, gamma = get_empirical_variogram(site_id, direction)
#    fit_model = fit_model_variogram(bin_center, gamma)
#    df = io.fill_df(df, meta_data, model = fit_model, 
#                    max_scale = bin_center[-1])   
#    
#    site_id = "Amik_Plain"
#    direction = "x"
#    geological_unit = "1/3"
#    meta_data = get_meta_data(site_id, direction, geological_unit)
#    bin_center, gamma = get_empirical_variogram(site_id, direction,
#                                                geological_unit)
#    fit_model = fit_model_variogram(bin_center, gamma)
#    df = io.fill_df(df, meta_data, model = fit_model, 
#                    max_scale = bin_center[-1])
#    direction = "x"
#    geological_unit = "2/3"
#    meta_data = get_meta_data(site_id, direction, geological_unit)
#    bin_center, gamma = get_empirical_variogram(site_id, direction,
#                                                geological_unit)
#    fit_model = fit_model_variogram(bin_center, gamma)
#    df = io.fill_df(df, meta_data, model = fit_model, 
#                    max_scale = bin_center[-1])
#    direction = "x"
#    geological_unit = "3/3"
#    meta_data = get_meta_data(site_id, direction, geological_unit)
#    bin_center, gamma = get_empirical_variogram(site_id, direction,
#                                                geological_unit)
#    fit_model = fit_model_variogram(bin_center, gamma)
#    df = io.fill_df(df, meta_data, model = fit_model, 
#                    max_scale = bin_center[-1])
#    
#    site_id = "Aurora_oil_sands_mine"
#    direction = "x"
#    meta_data = get_meta_data(site_id, direction)
#    bin_center, gamma = get_empirical_variogram(site_id, direction)
#    fit_model = fit_model_variogram(bin_center, gamma)
#    df = io.fill_df(df, meta_data, model = fit_model, 
#                    max_scale = bin_center[-1])  
#    
#    site_id = "Baishuihe_Landslide"
#    direction = "x"
#    geological_unit = "1/2"
#    meta_data = get_meta_data(site_id, direction, geological_unit)
#    bin_center, gamma = get_empirical_variogram(site_id, direction,
#                                                geological_unit)
#    fit_model = fit_model_variogram(bin_center, gamma)
#    df = io.fill_df(df, meta_data, model = fit_model, 
#                    max_scale = bin_center[-1]) 
#    direction = "x"
#    geological_unit = "2/2"
#    meta_data = get_meta_data(site_id, direction, geological_unit)
#    bin_center, gamma = get_empirical_variogram(site_id, direction,
#                                                geological_unit)
#    fit_model = fit_model_variogram(bin_center, gamma)
#    df = io.fill_df(df, meta_data, model = fit_model, 
#                    max_scale = bin_center[-1]) 
#    
#    site_id = "Bekkevoort_field_experiment"
#    direction = "x"
#    geological_unit = "1/3"
#    meta_data = get_meta_data(site_id, direction, geological_unit)
#    bin_center, gamma = get_empirical_variogram(site_id, direction,
#                                                geological_unit)
#    fit_model = fit_model_variogram(bin_center, gamma)
#    df = io.fill_df(df, meta_data, model = fit_model, 
#                    max_scale = bin_center[-1]) 
#    direction = "x"
#    geological_unit = "2/3"
#    meta_data = get_meta_data(site_id, direction, geological_unit)
#    bin_center, gamma = get_empirical_variogram(site_id, direction,
#                                                geological_unit)
#    fit_model = fit_model_variogram(bin_center, gamma)
#    df = io.fill_df(df, meta_data, model = fit_model, 
#                    max_scale = bin_center[-1]) 
#    direction = "x"
#    geological_unit = "3/3"
#    meta_data = get_meta_data(site_id, direction, geological_unit)
#    bin_center, gamma = get_empirical_variogram(site_id, direction,
#                                                geological_unit)
#    fit_model = fit_model_variogram(bin_center, gamma)
#    df = io.fill_df(df, meta_data, model = fit_model, 
#                    max_scale = bin_center[-1]) 
#    
#    site_id = "Botucatu_Formation"
#    direction = "x"
#    meta_data = get_meta_data(site_id, direction)
#    bin_center, gamma = get_empirical_variogram(site_id, direction)
#    fit_model = fit_model_variogram(bin_center, gamma)
#    df = io.fill_df(df, meta_data, model = fit_model, 
#                    max_scale = bin_center[-1])  
#    
#    site_id = "Caldwell_County_site"
#    direction = "x"
#    meta_data = get_meta_data(site_id, direction)
#    bin_center, gamma = get_empirical_variogram(site_id, direction)
#    fit_model = fit_model_variogram(bin_center, gamma)
#    df = io.fill_df(df, meta_data, model = fit_model, 
#                    max_scale = bin_center[-1])  
#    
#    site_id = "Calingri_farm_site"
#    direction = "x"
#    meta_data = get_meta_data(site_id, direction)
#    bin_center, gamma = get_empirical_variogram(site_id, direction)
#    fit_model = fit_model_variogram(bin_center, gamma)
#    df = io.fill_df(df, meta_data, model = fit_model, 
#                    max_scale = bin_center[-1]) 
#    
#    site_id = "Campania_Plain_site"
#    direction = "x"
#    meta_data = get_meta_data(site_id, direction)
#    bin_center, gamma = get_empirical_variogram(site_id, direction)
#    fit_model = fit_model_variogram(bin_center, gamma)
#    df = io.fill_df(df, meta_data, model = fit_model, 
#                    max_scale = bin_center[-1]) 
#    
#    site_id = "Campinas_Experimental_Center"
#    direction = "x"
#    meta_data = get_meta_data(site_id, direction)
#    bin_center, gamma = get_empirical_variogram(site_id, direction)
#    fit_model = fit_model_variogram(bin_center, gamma)
#    df = io.fill_df(df, meta_data, model = fit_model, 
#                    max_scale = bin_center[-1]) 
#    
#    site_id = "Cemagref_Experimental_Station"
#    direction = "x"
#    meta_data = get_meta_data(site_id, direction)
#    bin_center, gamma = get_empirical_variogram(site_id, direction)
#    fit_model = fit_model_variogram(bin_center, gamma)
#    df = io.fill_df(df, meta_data, model = fit_model, 
#                    max_scale = bin_center[-1]) 
#    
#    site_id = "CNR_experimental_farm"
#    direction = "x"
#    meta_data = get_meta_data(site_id, direction)
#    bin_center, gamma = get_empirical_variogram(site_id, direction)
#    fit_model = fit_model_variogram(bin_center, gamma)
#    df = io.fill_df(df, meta_data, model = fit_model, 
#                    max_scale = bin_center[-1]) 
#    
#    site_id = "Dal_Lake_catchment"
#    direction = "x"
#    meta_data = get_meta_data(site_id, direction)
#    bin_center, gamma = get_empirical_variogram(site_id, direction)
#    fit_model = fit_model_variogram(bin_center, gamma)
#    df = io.fill_df(df, meta_data, model = fit_model, 
#                    max_scale = bin_center[-1])
#    
#    site_id = "Domaine_of_Lavalette"
#    direction = "x"
#    meta_data = get_meta_data(site_id, direction)
#    bin_center, gamma = get_empirical_variogram(site_id, direction)
#    fit_model = fit_model_variogram(bin_center, gamma)
#    df = io.fill_df(df, meta_data, model = fit_model, 
#                    max_scale = bin_center[-1]) 
#    
#    site_id = "East_Central_Kansas"
#    direction = "x"
#    meta_data = get_meta_data(site_id, direction)
#    bin_center, gamma = get_empirical_variogram(site_id, direction)
#    fit_model = fit_model_variogram(bin_center, gamma)
#    df = io.fill_df(df, meta_data, model = fit_model, 
#                    max_scale = bin_center[-1]) 
#    
#    site_id = "Eutric_Regosol_site"
#    direction = "x"
#    geological_unit = "1/3"
#    meta_data = get_meta_data(site_id, direction, geological_unit)
#    bin_center, gamma = get_empirical_variogram(site_id, direction,
#                                                geological_unit)
#    fit_model = fit_model_variogram(bin_center, gamma)
#    df = io.fill_df(df, meta_data, model = fit_model, 
#                    max_scale = bin_center[-1]) 
#    direction = "x"
#    geological_unit = "2/3"
#    meta_data = get_meta_data(site_id, direction, geological_unit)
#    bin_center, gamma = get_empirical_variogram(site_id, direction,
#                                                geological_unit)
#    fit_model = fit_model_variogram(bin_center, gamma)
#    df = io.fill_df(df, meta_data, model = fit_model, 
#                    max_scale = bin_center[-1]) 
#    direction = "x"
#    geological_unit = "3/3"
#    meta_data = get_meta_data(site_id, direction, geological_unit)
#    bin_center, gamma = get_empirical_variogram(site_id, direction,
#                                                geological_unit)
#    fit_model = fit_model_variogram(bin_center, gamma)
#    df = io.fill_df(df, meta_data, model = fit_model, 
#                    max_scale = bin_center[-1]) 
#    
#    site_id = "Fall_Line_Hills_Pine_Flat"
#    direction = "x"
#    meta_data = get_meta_data(site_id, direction)
#    bin_center, gamma = get_empirical_variogram(site_id, direction)
#    fit_model = fit_model_variogram(bin_center, gamma)
#    df = io.fill_df(df, meta_data, model = fit_model, 
#                    max_scale = bin_center[-1]) 
#    
#    site_id = "Fall_Line_Hills_Troup"
#    direction = "x"
#    meta_data = get_meta_data(site_id, direction)
#    bin_center, gamma = get_empirical_variogram(site_id, direction)
#    fit_model = fit_model_variogram(bin_center, gamma)
#    df = io.fill_df(df, meta_data, model = fit_model, 
#                    max_scale = bin_center[-1]) 
#    
#    site_id = "Fuchu_Honmachi_paddy_field"
#    direction = "x"
#    meta_data = get_meta_data(site_id, direction)
#    bin_center, gamma = get_empirical_variogram(site_id, direction)
#    fit_model = fit_model_variogram(bin_center, gamma)
#    df = io.fill_df(df, meta_data, model = fit_model, 
#                    max_scale = bin_center[-1]) 
#    
#    site_id = "Heihe_River_Basin"
#    direction = "x"
#    meta_data = get_meta_data(site_id, direction)
#    bin_center, gamma = get_empirical_variogram(site_id, direction)
#    fit_model = fit_model_variogram(bin_center, gamma)
#    df = io.fill_df(df, meta_data, model = fit_model, 
#                    max_scale = bin_center[-1]) 
#    
#    site_id = "Huanjiang_Observation_and_Research_Station"
#    direction = "x"
#    meta_data = get_meta_data(site_id, direction)
#    bin_center, gamma = get_empirical_variogram(site_id, direction)
#    fit_model = fit_model_variogram(bin_center, gamma)
#    df = io.fill_df(df, meta_data, model = fit_model, 
#                    max_scale = bin_center[-1]) 
#    
#    site_id = "Instituto_Agronomico_Campinas"
#    direction = "x"
#    geological_unit = "1/2"
#    meta_data = get_meta_data(site_id, direction, geological_unit)
#    bin_center, gamma = get_empirical_variogram(site_id, direction,
#                                                geological_unit)
#    fit_model = fit_model_variogram(bin_center, gamma)
#    df = io.fill_df(df, meta_data, model = fit_model, 
#                    max_scale = bin_center[-1]) 
#    direction = "x"
#    geological_unit = "2/2"
#    meta_data = get_meta_data(site_id, direction, geological_unit)
#    bin_center, gamma = get_empirical_variogram(site_id, direction,
#                                                geological_unit)
#    fit_model = fit_model_variogram(bin_center, gamma)
#    df = io.fill_df(df, meta_data, model = fit_model, 
#                    max_scale = bin_center[-1]) 
#    
#    site_id = "Karkheh_River_site"
#    direction = "x"
#    meta_data = get_meta_data(site_id, direction)
#    bin_center, gamma = get_empirical_variogram(site_id, direction)
#    fit_model = fit_model_variogram(bin_center, gamma)
#    df = io.fill_df(df, meta_data, model = fit_model, 
#                    max_scale = bin_center[-1]) 
#    
#    site_id = "Karrendorfer_Wiesen"
#    direction = "x"
#    meta_data = get_meta_data(site_id, direction)
#    bin_center, gamma = get_empirical_variogram(site_id, direction)
#    fit_model = fit_model_variogram(bin_center, gamma)
#    df = io.fill_df(df, meta_data, model = fit_model, 
#                    max_scale = bin_center[-1]) 
#    
#    site_id = "Key_Lake_Uranium_Mine"
#    direction = "x"
#    meta_data = get_meta_data(site_id, direction)
#    bin_center, gamma = get_empirical_variogram(site_id, direction)
#    fit_model = fit_model_variogram(bin_center, gamma)
#    df = io.fill_df(df, meta_data, model = fit_model, 
#                    max_scale = bin_center[-1]) 
#    
#    site_id = "Konza_Prairie"
#    direction = "x"
#    meta_data = get_meta_data(site_id, direction)
#    bin_center, gamma = get_empirical_variogram(site_id, direction)
#    fit_model = fit_model_variogram(bin_center, gamma)
#    df = io.fill_df(df, meta_data, model = fit_model, 
#                    max_scale = bin_center[-1]) 
#    
#    site_id = "Krauthausen_site"
#    direction = "x"
#    meta_data = get_meta_data(site_id, direction)
#    bin_center, gamma = get_empirical_variogram(site_id, direction)
#    fit_model = fit_model_variogram(bin_center, gamma)
#    df = io.fill_df(df, meta_data, model = fit_model, 
#                    max_scale = bin_center[-1])
#    
#    site_id = "Kwinana_Bauxite_Residue_Disposal_Area"
#    direction = "x"
#    meta_data = get_meta_data(site_id, direction)
#    bin_center, gamma = get_empirical_variogram(site_id, direction)
#    fit_model = fit_model_variogram(bin_center, gamma)
#    df = io.fill_df(df, meta_data, model = fit_model, 
#                    max_scale = bin_center[-1])
#    
#    site_id = "LaoYeManQu_watershed"
#    direction = "x"
#    meta_data = get_meta_data(site_id, direction)
#    bin_center, gamma = get_empirical_variogram(site_id, direction)
#    fit_model = fit_model_variogram(bin_center, gamma)
#    df = io.fill_df(df, meta_data, model = fit_model, 
#                    max_scale = bin_center[-1])
#    
#    site_id = "Loess_Plateau"
#    direction = "x"
#    meta_data = get_meta_data(site_id, direction)
#    bin_center, gamma = get_empirical_variogram(site_id, direction)
#    fit_model = fit_model_variogram(bin_center, gamma)
#    df = io.fill_df(df, meta_data, model = fit_model, 
#                    max_scale = bin_center[-1])
#    
#    site_id = "Lutzito_catchment"
#    direction = "x"
#    meta_data = get_meta_data(site_id, direction)
#    bin_center, gamma = get_empirical_variogram(site_id, direction)
#    fit_model = fit_model_variogram(bin_center, gamma)
#    df = io.fill_df(df, meta_data, model = fit_model, 
#                    max_scale = bin_center[-1])
#    
#    site_id = "Lykorrema_stream"
#    direction = "x"
#    meta_data = get_meta_data(site_id, direction)
#    bin_center, gamma = get_empirical_variogram(site_id, direction)
#    fit_model = fit_model_variogram(bin_center, gamma)
#    df = io.fill_df(df, meta_data, model = fit_model, 
#                    max_scale = bin_center[-1])
#    
#    site_id = "Mahantango_Creek_watershed"
#    direction = "x"
#    geological_unit = "1/3"
#    meta_data = get_meta_data(site_id, direction, geological_unit)
#    bin_center, gamma = get_empirical_variogram(site_id, direction,
#                                                geological_unit)
#    fit_model = fit_model_variogram(bin_center, gamma)
#    df = io.fill_df(df, meta_data, model = fit_model, 
#                    max_scale = bin_center[-1]) 
#    direction = "x"
#    geological_unit = "2/3"
#    meta_data = get_meta_data(site_id, direction, geological_unit)
#    bin_center, gamma = get_empirical_variogram(site_id, direction,
#                                                geological_unit)
#    fit_model = fit_model_variogram(bin_center, gamma)
#    df = io.fill_df(df, meta_data, model = fit_model, 
#                    max_scale = bin_center[-1]) 
#    direction = "x"
#    geological_unit = "3/3"
#    meta_data = get_meta_data(site_id, direction, geological_unit)
#    bin_center, gamma = get_empirical_variogram(site_id, direction,
#                                                geological_unit)
#    fit_model = fit_model_variogram(bin_center, gamma)
#    df = io.fill_df(df, meta_data, model = fit_model, 
#                    max_scale = bin_center[-1]) 
#    
#    site_id = "Manoa_Waimanalo_Research_Station"
#    direction = "x"
#    meta_data = get_meta_data(site_id, direction)
#    bin_center, gamma = get_empirical_variogram(site_id, direction)
#    fit_model = fit_model_variogram(bin_center, gamma)
#    df = io.fill_df(df, meta_data, model = fit_model, 
#                    max_scale = bin_center[-1])
#    
#    site_id = "Mansoura_site"
#    direction = "x"
#    meta_data = get_meta_data(site_id, direction)
#    bin_center, gamma = get_empirical_variogram(site_id, direction)
#    fit_model = fit_model_variogram(bin_center, gamma)
#    df = io.fill_df(df, meta_data, model = fit_model, 
#                    max_scale = bin_center[-1])
#    
#    site_id = "MonDak_Irrigation_Research_Farm"
#    direction = "x"
#    meta_data = get_meta_data(site_id, direction)
#    bin_center, gamma = get_empirical_variogram(site_id, direction)
#    fit_model = fit_model_variogram(bin_center, gamma)
#    df = io.fill_df(df, meta_data, model = fit_model, 
#                    max_scale = bin_center[-1])
#    
#    site_id = "Nazareno_site"
#    direction = "x"
#    meta_data = get_meta_data(site_id, direction)
#    bin_center, gamma = get_empirical_variogram(site_id, direction)
#    fit_model = fit_model_variogram(bin_center, gamma)
#    df = io.fill_df(df, meta_data, model = fit_model, 
#                    max_scale = bin_center[-1])
#    
#    site_id = "Neckar_river_valley"
#    direction = "x"
#    geological_unit = "1/2"
#    meta_data = get_meta_data(site_id, direction, geological_unit)
#    bin_center, gamma = get_empirical_variogram(site_id, direction,
#                                                geological_unit)
#    fit_model = fit_model_variogram(bin_center, gamma)
#    df = io.fill_df(df, meta_data, model = fit_model, 
#                    max_scale = bin_center[-1]) 
#    direction = "z"
#    geological_unit = "1/2"
#    meta_data = get_meta_data(site_id, direction, geological_unit)
#    bin_center, gamma = get_empirical_variogram(site_id, direction,
#                                                geological_unit)
#    fit_model = fit_model_variogram(bin_center, gamma)
#    df = io.fill_df(df, meta_data, model = fit_model, 
#                    max_scale = bin_center[-1]) 
#    direction = "x"
#    geological_unit = "2/2"
#    meta_data = get_meta_data(site_id, direction, geological_unit)
#    bin_center, gamma = get_empirical_variogram(site_id, direction,
#                                                geological_unit)
#    fit_model = fit_model_variogram(bin_center, gamma)
#    df = io.fill_df(df, meta_data, model = fit_model, 
#                    max_scale = bin_center[-1]) 
#    direction = "z"
#    geological_unit = "2/2"
#    meta_data = get_meta_data(site_id, direction, geological_unit)
#    bin_center, gamma = get_empirical_variogram(site_id, direction,
#                                                geological_unit)
#    fit_model = fit_model_variogram(bin_center, gamma)
#    df = io.fill_df(df, meta_data, model = fit_model, 
#                    max_scale = bin_center[-1]) 
#    
#    site_id = "Nevada_Test_Site"
#    direction = "x"
#    meta_data = get_meta_data(site_id, direction)
#    bin_center, gamma = get_empirical_variogram(site_id, direction)
#    fit_model = fit_model_variogram(bin_center, gamma)
#    df = io.fill_df(df, meta_data, model = fit_model, 
#                    max_scale = bin_center[-1])
#    
#    site_id = "Nile_delta"
#    direction = "x"
#    meta_data = get_meta_data(site_id, direction)
#    bin_center, gamma = get_empirical_variogram(site_id, direction)
#    fit_model = fit_model_variogram(bin_center, gamma)
#    df = io.fill_df(df, meta_data, model = fit_model, 
#                    max_scale = bin_center[-1])
#    
#    site_id = "Northeast_China"
#    direction = "x"
#    meta_data = get_meta_data(site_id, direction)
#    bin_center, gamma = get_empirical_variogram(site_id, direction)
#    fit_model = fit_model_variogram(bin_center, gamma)
#    df = io.fill_df(df, meta_data, model = fit_model, 
#                    max_scale = bin_center[-1])
#    
#    site_id = "Ondokuz_Mayis_University"
#    direction = "x"
#    meta_data = get_meta_data(site_id, direction)
#    bin_center, gamma = get_empirical_variogram(site_id, direction)
#    fit_model = fit_model_variogram(bin_center, gamma)
#    df = io.fill_df(df, meta_data, model = fit_model, 
#                    max_scale = bin_center[-1])
#    
#    site_id = "Orchard_Experiment_site"
#    direction = "x"
#    meta_data = get_meta_data(site_id, direction)
#    bin_center, gamma = get_empirical_variogram(site_id, direction)
#    fit_model = fit_model_variogram(bin_center, gamma)
#    df = io.fill_df(df, meta_data, model = fit_model, 
#                    max_scale = bin_center[-1])
#    
#    site_id = "Pars_Abad"
#    direction = "x"
#    meta_data = get_meta_data(site_id, direction)
#    bin_center, gamma = get_empirical_variogram(site_id, direction)
#    fit_model = fit_model_variogram(bin_center, gamma)
#    df = io.fill_df(df, meta_data, model = fit_model, 
#                    max_scale = bin_center[-1])
#    
#    site_id = "Pla_de_Sant_Jordi"
#    direction = "x"
#    geological_unit = "1/2"
#    meta_data = get_meta_data(site_id, direction, geological_unit)
#    bin_center, gamma = get_empirical_variogram(site_id, direction,
#                                                geological_unit)
#    fit_model = fit_model_variogram(bin_center, gamma)
#    df = io.fill_df(df, meta_data, model = fit_model, 
#                    max_scale = bin_center[-1]) 
#    direction = "x"
#    geological_unit = "2/2"
#    meta_data = get_meta_data(site_id, direction, geological_unit)
#    bin_center, gamma = get_empirical_variogram(site_id, direction,
#                                                geological_unit)
#    fit_model = fit_model_variogram(bin_center, gamma)
#    df = io.fill_df(df, meta_data, model = fit_model, 
#                    max_scale = bin_center[-1]) 
    
    site_id = "Plastic_Lake_watershed"
    direction = "x"
    meta_data = get_meta_data(site_id, direction)
    bin_center, gamma = get_empirical_variogram(site_id, direction)
    fit_model = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    max_scale = bin_center[-1])
    
    site_id = "Reserva_Biosfera_de_San_Francisco"
    direction = "x"
    geological_unit = "1/3"
    meta_data = get_meta_data(site_id, direction, geological_unit)
    bin_center, gamma = get_empirical_variogram(site_id, direction,
                                                geological_unit)
    fit_model = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    max_scale = bin_center[-1]) 
    direction = "x"
    geological_unit = "2/3"
    meta_data = get_meta_data(site_id, direction, geological_unit)
    bin_center, gamma = get_empirical_variogram(site_id, direction,
                                                geological_unit)
    fit_model = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    max_scale = bin_center[-1]) 
    direction = "x"
    geological_unit = "3/3"
    meta_data = get_meta_data(site_id, direction, geological_unit)
    bin_center, gamma = get_empirical_variogram(site_id, direction,
                                                geological_unit)
    fit_model = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    max_scale = bin_center[-1]) 
    
    site_id = "Ribeirao_Marcela_watershed"
    direction = "x"
    meta_data = get_meta_data(site_id, direction)
    bin_center, gamma = get_empirical_variogram(site_id, direction)
    fit_model = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    max_scale = bin_center[-1])
    
    site_id = "Ribera_Seca_catchment"
    direction = "x"
    meta_data = get_meta_data(site_id, direction)
    bin_center, gamma = get_empirical_variogram(site_id, direction)
    fit_model = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    max_scale = bin_center[-1])
    
    site_id = "Saby_site"
    direction = "x"
    meta_data = get_meta_data(site_id, direction)
    bin_center, gamma = get_empirical_variogram(site_id, direction)
    fit_model = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    max_scale = bin_center[-1])
    
    site_id = "Shenmu_County_watershed"
    direction = "x"
    meta_data = get_meta_data(site_id, direction)
    bin_center, gamma = get_empirical_variogram(site_id, direction)
    fit_model = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    max_scale = bin_center[-1])
    
    site_id = "Smeaton_farm_field"
    direction = "x"
    meta_data = get_meta_data(site_id, direction)
    bin_center, gamma = get_empirical_variogram(site_id, direction)
    fit_model = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    max_scale = bin_center[-1])
    
    site_id = "South_Jingyang_Plateau"
    direction = "x"
    geological_unit = "1/2"
    meta_data = get_meta_data(site_id, direction, geological_unit)
    bin_center, gamma = get_empirical_variogram(site_id, direction,
                                                geological_unit)
    fit_model = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    max_scale = bin_center[-1]) 
    direction = "x"
    geological_unit = "2/2"
    meta_data = get_meta_data(site_id, direction, geological_unit)
    bin_center, gamma = get_empirical_variogram(site_id, direction,
                                                geological_unit)
    fit_model = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    max_scale = bin_center[-1]) 
    
    site_id = "Spanish_mainland"
    direction = "x"
    meta_data = get_meta_data(site_id, direction)
    bin_center, gamma = get_empirical_variogram(site_id, direction)
    fit_model = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    max_scale = bin_center[-1])
    
    site_id = "Vargem_de_Caldas_basin"
    direction = "x"
    geological_unit = "1/2"
    meta_data = get_meta_data(site_id, direction, geological_unit)
    bin_center, gamma = get_empirical_variogram(site_id, direction,
                                                geological_unit)
    fit_model = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    max_scale = bin_center[-1]) 
    direction = "x"
    geological_unit = "2/2"
    meta_data = get_meta_data(site_id, direction, geological_unit)
    bin_center, gamma = get_empirical_variogram(site_id, direction,
                                                geological_unit)
    fit_model = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    max_scale = bin_center[-1]) 
    
    site_id = "Waimanalo_Research_Station"
    direction = "x"
    meta_data = get_meta_data(site_id, direction)
    bin_center, gamma = get_empirical_variogram(site_id, direction)
    fit_model = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    max_scale = bin_center[-1])
    
    site_id = "Water_management_study_site"
    direction = "x"
    meta_data = get_meta_data(site_id, direction)
    bin_center, gamma = get_empirical_variogram(site_id, direction)
    fit_model = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    max_scale = bin_center[-1])
    
    site_id = "West_Side_Field_Station"
    direction = "x"
    meta_data = get_meta_data(site_id, direction)
    bin_center, gamma = get_empirical_variogram(site_id, direction)
    fit_model = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    max_scale = bin_center[-1])
    
    site_id = "Xilin_River_basin"
    direction = "x"
    meta_data = get_meta_data(site_id, direction)
    bin_center, gamma = get_empirical_variogram(site_id, direction)
    fit_model = fit_model_variogram(bin_center, gamma)
    df = io.fill_df(df, meta_data, model = fit_model, 
                    max_scale = bin_center[-1])
    
    
    
    
    

        
    
    io.write_df(df)
    
    
    # output
    ax = fit_model.plot(x_max=max(bin_center))
    plt.scatter(bin_center, gamma)
    plt.show()
    print(fit_model)
    