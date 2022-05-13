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


def get_empirical_variogram(site_id):
    
    #read in data from a file
    variogram_data_df = pd.read_csv("../data/aquifer_variogram.csv")
    
    df = variogram_data_df[variogram_data_df['site_id']==site_id]
    
    bin_center = df["lag_m"].to_numpy()
    gamma = df["gamma"].to_numpy()
  
    return bin_center.astype(np.float), gamma.astype(np.float)


def fit_model_variogram(bin_center, gamma):
    
    # fit the variogram variogram with a stable model. (no nugget fitted)
    fit_model = gs.Stable(dim=2)
    fit_model.fit_variogram(bin_center, gamma, nugget=True)
    return fit_model


if __name__ == '__main__':
    
    df = init_df()
    
    bin_center, gamma = get_empirical_variogram(site_id = "Dammam_aquifer")
    fit_model = fit_model_variogram(bin_center, gamma)
    df = fill_df(df, fit_model)

    write_df(df)
    
    
    # output
    ax = fit_model.plot(x_max=max(bin_center))
    plt.scatter(bin_center, gamma)
    plt.show()
#    print(fit_model)
    