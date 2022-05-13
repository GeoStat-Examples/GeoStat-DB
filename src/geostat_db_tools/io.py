#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 11:44:17 2022

@author: fhesse
"""

import pandas as pd


def init_df():
    
    df = pd.DataFrame(columns=["dim", 
                               "var", 
                               "len_scale",
                               "nugget", 
                               "alpha"])
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
    
    