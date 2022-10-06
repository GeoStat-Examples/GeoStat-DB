#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 11:44:17 2022

@author: fhesse
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression


def plot_scatter(x, y):
    
    plt.scatter(x, y)
    plt.axis([0, 1, 0, 1])
    
    
#    plt.xlabel(r'Gaussian model')
#    plt.ylabel(r'Exponential model')
    plt.xlabel(r'Stable model')
    plt.ylabel(r'Matern model')

    #pd.plotting.scatter_matrix(df_nugget, diagonal='kde')
    #sn.kdeplot(y, color='red', shade='True')
    #plt.xlabel(r'$\alpha$')
    #plt.ylabel(r'$p$')

    font = {'family' : 'normal', 'weight' : 'bold', 'size' : 22}
    plt.rc('font', **font)
    #
    plt.show()
    
    
def plot_kde(df):
    
    nugget = np.array(df['nugget'])
    
    nugget = nugget[(nugget <= 1)]
    
    font = {'family' : 'normal', 'weight' : 'bold', 'size' : 22}
    plt.rc('font', **font)

    #pd.plotting.scatter_matrix(df_nugget, diagonal='kde')
#    sns.kdeplot(nugget, color='red', shade='True')#
    ax = sns.displot(nugget, kde=True, binwidth=0.025)
    ax.set(xlabel='Nugget', ylabel='counts')
    #plt.xlabel(r'$\alpha$')
    #plt.ylabel(r'$p$')

    #
    plt.show()    


if __name__ == '__main__':
    
#    site_type = 'soil'
    site_type = 'aquifer'
    
    df_matern = pd.read_csv("../../data_stats/" + site_type + "_statistics_matern.csv")
    df_stable = pd.read_csv("../../data_stats/" + site_type + "_statistics_stable.csv")
    df_gauss = pd.read_csv("../../data_stats/" + site_type + "_statistics_gaussian.csv")
    df_exp = pd.read_csv("../../data_stats/" + site_type + "_statistics_exponential.csv")
    df_sph = pd.read_csv("../../data_stats/" + site_type + "_statistics_spherical.csv")
    
    # normalize nuggets with the variance
    df_matern['nugget'] = df_matern['nugget']/(df_matern['var'] + df_matern['nugget'])
    df_stable['nugget'] = df_stable['nugget']/(df_stable['var'] + df_stable['nugget'])
    df_gauss['nugget'] = df_gauss['nugget']/(df_gauss['var'] + df_gauss['nugget'])
    df_exp['nugget'] = df_exp['nugget']/(df_exp['var'] + df_exp['nugget'])
    df_sph['nugget'] = df_sph['nugget']/(df_sph['var'] + df_sph['nugget'])
    
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

    df_nugget = pd.DataFrame({'Matern': (np.array(df_matern["nugget"])),
                              'Stable': (np.array(df_stable["nugget"])),
                              'Gauss': (np.array(df_gauss["nugget"])),
                              'Exp': (np.array(df_exp["nugget"])),
                              'Sph': (np.array(df_sph["nugget"]))})

    x = np.array(df_nugget["Matern"])

    x = x[~np.isnan(x)]
    x = x.reshape((-1, 1))
    y = np.array(df_nugget["Stable"])

    y = y[~np.isnan(y)]


    reg = LinearRegression()
    reg.fit(x, y)

    y_reg = x[:,0]*reg.coef_ + reg.intercept_
    y_reg = x[:,0]
    y_res = y - y_reg
    
    plot_scatter(x, y)
#    plot_kde(df_stable)

    