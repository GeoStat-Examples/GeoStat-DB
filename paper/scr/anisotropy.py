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


def plot_kde(y_res, y_grid = None):
    
    font = {'family' : 'normal', 'weight' : 'bold', 'size' : 22}
    plt.rc('font', **font)


    ax = sns.displot(y_res, kde=True)
    ax.set(xlabel=r'log $\lambda_x$', ylabel='counts')
    
#    plt.savefig('../../fig/anisotropy_z_kde.png')
#    plt.savefig('../../fig/anisotropy_y_kde.png')
    plt.show()
    
    
def plot_scatter(x, y):
    
    plt.scatter(x, y)
    plt.plot(x, x)
    plt.ylabel(r'log $\lambda_z$')
    plt.xlabel(r'log $\lambda_x$')
    
#    plt.savefig('../../fig/anisotropy_z_scatter.png')
#    plt.savefig('../../fig/anisotropy_y_scatter.png')
    plt.show()

if __name__ == '__main__':
    
    #    data_type = 'soil'
    data_type = 'aquifer'
    
    variogram_type = 'gaussian'
#    variogram_type = 'stable'
    
    df = get_data(data_type, variogram_type)

    df_x = df[df.direction.isin(['x'])]
    df_y = df[df.direction.isin(['y'])]
    df_z = df[df.direction.isin(['z'])]

    unique_z_sites = df_z['site_id'].unique()
    unique_y_sites = df_y['site_id'].unique()

    df_xz = df_x[df_x.site_id.isin(unique_z_sites)]
    df_xy = df_x[df_x.site_id.isin(unique_y_sites)]

    x = np.log(np.array(df_xy["len_scale"]))
    x = x[~np.isnan(x)]
    x = x.reshape((-1, 1))
    y = np.log(np.array(df_y["len_scale"]))
    y = y[~np.isnan(y)]

#    reg = LinearRegression()
#    reg.fit(x, y)
    
    #y_reg = x[:,0]*reg.coef_ + reg.intercept_
    y_reg = x[:,0]
    y_res = y - y_reg
    
    plot_kde(y_res)
#    plot_scatter(x, y)


