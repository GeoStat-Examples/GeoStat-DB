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
from scipy.optimize import curve_fit
from statsmodels.nonparametric.kde import KDEUnivariate


def func_2(x, mu_1, sigma_1, mu_2, sigma_2, theta):
    func_1 = 1/(sigma_1*np.sqrt(2*np.pi)) * np.exp(-0.5 *((x-mu_1)/sigma_1)**2)
    func_2 = 1/(sigma_2*np.sqrt(2*np.pi)) * np.exp(-0.5 *((x-mu_2)/sigma_2)**2)
    return theta*func_1 + (1-theta)*func_2


def kde_statsmodels_u(x, x_grid, bandwidth=0.2, **kwargs):
    """Univariate Kernel Density Estimation with Statsmodels"""
    kde = KDEUnivariate(x)
    kde.fit(bw=bandwidth, **kwargs)
    return kde.evaluate(x_grid)

def get_data(data_type, variogram_type):
    return pd.read_csv("../../data_stats/" + data_type + "_statistics_" + variogram_type +  ".csv")


def regress_data(df):
    
#    len_scale = df["len_scale"]
#    max_scale = df["max_scale"]

    x = np.log(np.array(df["max_scale"]))
    x = x[~np.isnan(x)]
    x = x.reshape((-1, 1))
    y = np.log(np.array(df["len_scale"]))
    y = y[~np.isnan(y)]

    reg = LinearRegression()
    reg.fit(x, y)

    y_reg = x[:,0]*reg.coef_ + reg.intercept_
    y_res = y - y_reg
    
    y_grid = np.linspace(-4.0, 11.0, 1000)
    
    return y_res, y_grid, x, y


def fit_data(y_res, y_grid):
    popt, pcov = curve_fit(func_2, 
                           y_grid, 
                           kde_statsmodels_u(y_res, y_grid, bandwidth=0.5), 
                           p0=[0.5, 1, 5, 1, 0.5])
#    popt, pcov = curve_fit(func, 
#                           y_grid, 
#                           kde_statsmodels_u(y_res, y_grid, bandwidth=0.5), 
#                           p0=[-0.1, 1])
    return popt


def plot_kde(y_res, y_grid):
    
    font = {'family' : 'normal', 'weight' : 'bold', 'size' : 22}
    plt.rc('font', **font)


    ax = sns.displot(y_res, kde=True)
    ax.set(xlabel='log max length scale', ylabel='counts')
    
#    plt.plot(y_grid, kde_statsmodels_u(y_res, y_grid, bandwidth=0.5))
#    plt.plot(y_grid, func_2(y_grid, popt[0], popt[1], popt[2], popt[3], popt[4]))
#    plt.xlabel('log max length scale')
#    plt.ylabel('p')
    
#    plt.savefig('../../fig/kdeplot_len_scale_' + data_type)
    plt.show()
    

def plot_scatter(x, y):
    
    plt.scatter(x, y)
    plt.plot(x, x)
    plt.ylabel(r'log $\lambda$')
    plt.xlabel(r'log $\lambda_{max}$')
    
#    plt.savefig('../../fig/kdeplot_len_scale_' + data_type)
    plt.show()    


if __name__ == '__main__':
    
    data_type = 'soil'
#    data_type = 'aquifer'
    
#    variogram_type = 'gaussian'
    variogram_type = 'stable'
    
    df = get_data(data_type, variogram_type)
    y_res, y_grid, x, y = regress_data(df)
    popt = fit_data(y_res, y_grid)    
    
#    plot_kde(y_res, y_grid)
    plot_scatter(x, y)

