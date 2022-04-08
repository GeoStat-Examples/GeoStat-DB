#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 11:44:17 2022

@author: fhesse
"""

import pandas as pd
import numpy as np


soil_df = pd.read_csv("../data/sol_ksat.pnts_horizons.csv")

site_key = soil_df['site_key'].unique()
site_key_no = len(site_key)

row_no_array = np.zeros(site_key_no)
for site_key_i in range(3900):
    row_id = soil_df.apply(lambda x: True if x['site_key'] == site_key[site_key_i] else False,
                           axis=1)
    row_no_array[site_key_i] = len(row_id[row_id == True].index)

valid_id = np.where(row_no_array > 10)
valid_id_no = len(valid_id[0]) 

