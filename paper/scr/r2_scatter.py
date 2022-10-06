#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 11:44:17 2022

@author: fhesse
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sn
from sklearn.linear_model import LinearRegression


df_matern = pd.read_csv("../../data_stats/aquifer_statistics_matern.csv")
df_stable = pd.read_csv("../../data_stats/aquifer_statistics_stable.csv")
df_gauss = pd.read_csv("../../data_stats/aquifer_statistics_gaussian.csv")
df_exp = pd.read_csv("../../data_stats/aquifer_statistics_exponential.csv")
df_sph = pd.read_csv("../../data_stats/aquifer_statistics_spherical.csv")


# create a unique identifier
df_matern['unique_id'] = df_matern['site_id'] + df_matern['direction'] + df_matern['geological_unit']
df_stable['unique_id'] = df_stable['site_id'] + df_stable['direction'] + df_stable['geological_unit']
df_gauss['unique_id'] = df_gauss['site_id'] + df_gauss['direction'] + df_gauss['geological_unit']
df_exp['unique_id'] = df_exp['site_id'] + df_exp['direction'] + df_exp['geological_unit']
df_sph['unique_id'] = df_sph['site_id'] + df_sph['direction'] + df_sph['geological_unit']

unique_matern_sites = df_matern['unique_id'].unique()
unique_stable_sites = df_stable['unique_id'].unique()
unique_gauss_sites = df_gauss['unique_id'].unique()
unique_exp_sites = df_exp['unique_id'].unique()
unique_sph_sites = df_sph['unique_id'].unique()

unique_sites = set(unique_matern_sites)&set(unique_stable_sites)
unique_sites = sorted(unique_sites, key = lambda k : list(unique_matern_sites).index(k))
unique_sites_full = set(unique_sites)&set(unique_gauss_sites)
unique_sites = sorted(unique_sites_full, key = lambda k : list(unique_matern_sites).index(k))
unique_sites_full = set(unique_sites)&set(unique_exp_sites)
unique_sites = sorted(unique_sites_full, key = lambda k : list(unique_matern_sites).index(k))
unique_sites_full = set(unique_sites)&set(unique_sph_sites)
unique_sites = sorted(unique_sites_full, key = lambda k : list(unique_matern_sites).index(k))

df_stable = df_stable[df_stable.unique_id.isin(unique_sites)]
df_matern = df_matern.loc[df_matern['unique_id'].isin(unique_sites)]
df_gauss = df_gauss.loc[df_gauss['unique_id'].isin(unique_sites)]
df_exp = df_exp.loc[df_exp['unique_id'].isin(unique_sites)]
df_sph = df_sph.loc[df_sph['unique_id'].isin(unique_sites)]

df_log_length = pd.DataFrame({'Matern': np.log(np.array(df_matern["r2"])),
                              'Stable': np.log(np.array(df_stable["r2"])),
                              'Gauss': np.log(np.array(df_gauss["r2"])),
                              'Exp': np.log(np.array(df_exp["r2"])),
                              'Sph': np.log(np.array(df_sph["r2"]))})

#x = np.array(df_log_length["Stable"])
##x = x/np.array(df_stable["var"])
#x = x[~np.isnan(x)]
#x = x.reshape((-1, 1))
#y = np.array(df_log_length["Matern"])
##y = y/np.array(df_matern["var"])
#y = y[~np.isnan(y)]
#
#
#reg = LinearRegression()
#reg.fit(x, y)
#
#y_reg = x[:,0]*reg.coef_ + reg.intercept_
#y_reg = x[:,0]
#y_res = y - y_reg
#
#plt.scatter(x, y)
##plt.plot(x, x)
#plt.xlabel(r'Gaussian model')
#plt.ylabel(r'Exponential model')

pd.plotting.scatter_matrix(df_log_length, diagonal='kde')
#sn.kdeplot(y, color='red', shade='True')
#plt.xlabel(r'$\alpha$')
#plt.ylabel(r'$p$')

font = {'family' : 'normal',
        'weight' : 'bold',
        'size'   : 36}

plt.rc('font', **font)
#
plt.show()