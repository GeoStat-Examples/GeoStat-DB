#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 11:44:17 2022

@author: fhesse
"""

import pandas as pd


def init_df():
    
    df = pd.DataFrame(columns=["site_id",
                               "direction",
                               "var", 
                               "len_scale",
                               "nugget", 
                               "alpha",
                               "max_scale",
                               "min_scale"])
    return df


def fill_df(df, site_id, model, direction = "x",
            max_scale = "nan", min_scale = "nan"):
    
    # initialize data of lists.
    data = {"site_id":site_id,
            "direction":[direction],
            "var":[model.var], 
            "len_scale":[model.len_scale],
            "nugget":[model.nugget],
            "alpha":[model.alpha],
            "max_scale":[max_scale],
            "min_scale": [min_scale]}

    # Create DataFrame
    data_df = pd.DataFrame(data)

    return df.append(data_df, ignore_index=True)


def write_df(df):
    
    df.to_csv('../results/aquifer_statistics.csv')
    
    