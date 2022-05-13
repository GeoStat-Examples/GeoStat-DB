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


def init_df():
    
    df = pd.DataFrame(columns=["dim", "var", "len_scale",
                               "nugget", "alpha"])
    return df


def fill_df(df, model):
    
    # initialize data of lists.
    data = {"dim":[model.dim],
            "var":[model.var], 
            "len_scale":[model.len_scale],
            "nugget":[model.nugget],
            "alpha":[model.alpha]}

    # Create DataFrame
    data_df = pd.DataFrame(data)

    return df.append(data_df, ignore_index=True)


def write_df(df):
    
    df.to_csv('../results/aquifer_statistics.csv')
    

def get_data(site_id):
    
    #read in data from a file
    T_data_df = pd.read_csv("../data/aquifer_T.csv")
    
    df = T_data_df[T_data_df['site_id']==site_id]
    
    T_field = np.log(df["T_m2/d"])
    
    x = df["East_UTM_km"]
    y = df["North_UTM_km"]
    
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
    
    df = init_df()
    
    x, y, field = get_data(site_id = "Dammam_aquifer")   
    bin_center, gamma = get_empirical_variogram(x, y, field)
    fit_model = fit_model_variogram(bin_center, gamma)
    df = fill_df(df, fit_model)
    
    
    
    write_df(df)
    
    
    # output
    ax = fit_model.plot(x_max=max(bin_center))
    plt.scatter(bin_center, gamma)
    plt.show()
    print(fit_model)
    