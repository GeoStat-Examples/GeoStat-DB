#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 11:44:17 2022

@author: fhesse
"""

import pandas as pd


def init_df():
    
    df = pd.DataFrame(columns=["site_id",
                               "var", 
                               "len_scale",
                               "nugget", 
                               "alpha",
                               "max_scale",
                               "min_scale", 
                               "var_type",
                               "direction",
                               "geological_unit",
                               "measurement_method",
                               "data_source",
                               "ISO 3166"])
    return df


def fill_df(df, meta_data, model, 
            max_scale = "nan", min_scale = "nan"):
    
    # initialize data of lists.
    data = {"site_id":meta_data["site_id"],
            "var":[model.var], 
            "len_scale":[model.len_scale],
            "nugget":[model.nugget],
            "alpha":[model.alpha],
            "max_scale":[max_scale],
            "min_scale": [min_scale],
            "var_type":meta_data["var_type"],
            "direction":meta_data["direction"],            
            "geological_unit":meta_data["geological_unit"],
            "measurement_method":meta_data["measurement_method"],
            "data_source":meta_data["data_source"],
            "ISO 3166":meta_data["ISO 3166"],}

    # Create DataFrame
    data_df = pd.DataFrame(data)

    return df.append(data_df, ignore_index=True)


def write_df(df):
    
    df.to_csv('../results/aquifer_statistics.csv')
    
    