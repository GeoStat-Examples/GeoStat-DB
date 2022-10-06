#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 11:44:17 2022

@author: fhesse
"""
import geopandas
import geoplot
import mapclassify
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def get_data():
    world = geopandas.read_file(
            geopandas.datasets.get_path('naturalearth_lowres')
            )

#    del world['gdp_md_est']
    world.rename(columns={'gdp_md_est': 'data_points'}, inplace=True)
    world.iloc[-50:, world.columns.get_loc('pop_est')] = np.nan
    world.iloc[:, world.columns.get_loc('data_points')] = np.nan
    #world = world.iloc[:-50]
    
    return world

def get_variogram_data():
    
    df1 = pd.read_csv('../../data_proc/aquifer_variogram.csv')
    df2 = pd.read_csv('../../data_proc/soil_variogram.csv')
    
    df1 = df1[['ISO 3166']].copy()
    df2 = df2[['ISO 3166']].copy()
    
    df1 = df1.append(df2, ignore_index=True)
    
#    df = df1.merge(df2)
    
    return df1

def plot_data(world):
    
    fig, ax = plt.subplots(
            nrows = 1,
            ncols = 1,
            figsize = (15,6),
            facecolor = plt.cm.Blues(.2))
    fig.suptitle('Data on variogram parameters per country',
                 fontsize = 'xx-large',  
                 fontweight = 'bold')
    ax.set_facecolor(plt.cm.Blues(.2))

    world.plot(
            ax = ax,
            color = 'white',
            edgecolor = 'black'
            )

    world.plot(column = 'data_points',
               cmap = 'OrRd',
               ax = ax,
               legend = True,
               legend_kwds = {'label': "no. of data points", 'shrink': 0.7},
               missing_kwds = {'facecolor':'Gray'},
               )
    [spine.set_visible(False) for spine in ax.spines.values()]
    ax.xaxis.set_visible(False)
    ax.yaxis.set_visible(False)

    plt.show()

if __name__ == '__main__':
    
    df = get_data()
    
    df_vario = get_variogram_data()
    countries = df_vario['ISO 3166'].unique()
    counts = df_vario['ISO 3166'].value_counts()
    for i in range(len(countries)):
#        print(countries[i])
#        print(counts[countries[i]])
#        print(df.loc[df['iso_a3'] == countries[i]])
#        print(df[df['iso_a3']==countries[i]].index.values)
        df["data_points"][df[df['iso_a3']==countries[i]].index.values] = counts[countries[i]]
    
    
    plot_data(df)