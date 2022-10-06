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


def get_data(data_type, variogram_type):
    return pd.read_csv("../../data_stats/" + data_type + "_statistics_" + variogram_type +  ".csv")

def regress_data(df_stable, df_matern):
    
    x = np.array(df_stable["nu"])
    x = x[~np.isnan(x)]
    x = x.reshape((-1, 1))
    y = np.array(df_matern["nu"])
    y = y[~np.isnan(y)]


    reg = LinearRegression()
    reg.fit(x, y)

    y_reg = x[:,0]*reg.coef_ + reg.intercept_
    y_reg = x[:,0]
    y_res = y - y_reg
    
    return x, y


def plot_scatter(x, y):
    
    font = {'family' : 'normal', 'weight' : 'bold', 'size' : 22}
    plt.rc('font', **font)
    
    plt.scatter(x, y)
    #plt.plot(x, x)
    plt.ylabel(r'$\nu$')
    plt.xlabel(r'$\alpha$')

    plt.show()
    
    
def plot_kde(y):
    
    font = {'family' : 'normal', 'weight' : 'bold', 'size' : 22}
    plt.rc('font', **font)

    ax = sns.displot(y, kde=True, binwidth=0.5)
#    ax.set(xlabel=r'$\alpha$', ylabel='p')
    ax.set(xlabel=r'$\nu$', ylabel='p')

    plt.show()
    

if __name__ == '__main__':

    
#    data_type = 'soil'
    data_type = 'aquifer'
    
    df_matern = get_data(data_type, 'matern')
    df_stable = get_data(data_type, 'stable')

    # create a unique identifier
    df_matern['unique_id'] = df_matern['site_id'] + df_matern['direction'] + df_matern['geological_unit']
    df_stable['unique_id'] = df_stable['site_id'] + df_stable['direction'] + df_stable['geological_unit']

    unique_matern_sites = df_matern['unique_id'].unique()
    df_stable = df_stable[df_stable.unique_id.isin(unique_matern_sites)]

    unique_stable_sites = df_stable['unique_id'].unique()
    df_matern = df_matern[df_matern.unique_id.isin(unique_stable_sites)]

    x, y = regress_data(df_stable, df_matern)

#    plot_scatter(x, y)
    plot_kde(y)
    