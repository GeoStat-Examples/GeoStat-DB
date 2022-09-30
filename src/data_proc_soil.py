#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 15:27:47 2022

@author: fhesse
"""

import numpy as np
import pandas as pd

def init_df():
    
    df = pd.DataFrame(columns=["site_id", 
                               "lag_m", 
                               "gamma", 
                               "var_type", 
                               "direction",
                               "geological_unit",
                               "measurement_method", 
                               "data_source",
                               "ISO 3166"])
    return df


def fill_df(df, f_path, 
            site_id = "nan", 
            var_type = "nan", 
            direction = "nan",
            unit = "nan",
            data_source = "nan", 
            country_code = "nan", 
            measurement_method = "nan"):
    
    df_var = pd.read_csv(f_path, names=["lag_m", "var"])
    
    # initialize data of lists.
    data = {"site_id":site_id,
            "lag_m":df_var["lag_m"],
            "gamma":df_var["var"],
            "var_type":var_type,
            "direction":direction,
            "geological_unit":unit,
            "measurement_method":measurement_method,
            "data_source":data_source,
            "ISO 3166":country_code}
    
    # Create DataFrame
    data_df = pd.DataFrame(data)
    
#    bigdata = df.append(data_df, ignore_index=True)
    
    return df.append(data_df, ignore_index=True)


def write_df(df):
    
    df.to_csv('../data_proc/soil_variogram.csv')


if __name__ == '__main__':
    
    # create data frame
    
    df = init_df()
    
    df = fill_df(df, f_path="../data_prep/soil_variograms/Alto_Rio_Grande_basin_BRA/variogram_saturated_conductivity.csv",
                 site_id = 'Alto_Rio_Grande_basin',
                 var_type = "saturated_hydraulic_conductivty",
                 direction = "x",
                 unit = "1/1",
                 data_source = '10.1590/S0100-06832011000500029',
                 country_code = 'BRA')
    
    df = fill_df(df, f_path="../data_prep/soil_variograms/Amik_Plain_TUR/variogram_saturated_conductivity_layer_1.csv",
                 site_id = 'Amik_Plain',
                 var_type = "saturated_hydraulic_conductivty",
                 direction = "x",
                 unit = "1/3",
                 data_source = '10.1007/s11119-014-9379-0',
                 country_code = 'TUR')    
    df = fill_df(df, f_path="../data_prep/soil_variograms/Amik_Plain_TUR/variogram_saturated_conductivity_layer_2.csv",
                 site_id = 'Amik_Plain',
                 var_type = "saturated_hydraulic_conductivty",
                 direction = "x",
                 unit = "2/3",
                 data_source = '10.1007/s11119-014-9379-0',
                 country_code = 'TUR')    
    df = fill_df(df, f_path="../data_prep/soil_variograms/Amik_Plain_TUR/variogram_saturated_conductivity_layer_3.csv",
                 site_id = 'Amik_Plain',
                 var_type = "saturated_hydraulic_conductivty",
                 direction = "x",
                 unit = "3/3",
                 data_source = '10.1007/s11119-014-9379-0',
                 country_code = 'TUR')

    df = fill_df(df, f_path="../data_prep/soil_variograms/Aurora_oil_sands_mine_CAN/variogram_saturated_conductivity.csv",
                 site_id = 'Aurora_oil_sands_mine',
                 var_type = "saturated_hydraulic_conductivty",
                 direction = "x",
                 unit = "1/1",
                 data_source = '10.1016/j.geoderma.2015.08.014',
                 country_code = 'CAN')

    df = fill_df(df, f_path="../data_prep/soil_variograms/Baishuihe_Landslide_CHN/variogram_saturated_conductivity_layer_1.csv",
                 site_id = 'Baishuihe_Landslide',
                 var_type = "saturated_hydraulic_conductivty",
                 direction = "x",
                 unit = "1/2",
                 data_source = '10.1155/2018/7290640',
                 country_code = 'CHN')    
    df = fill_df(df, f_path="../data_prep/soil_variograms/Baishuihe_Landslide_CHN/variogram_saturated_conductivity_layer_2.csv",
                 site_id = 'Baishuihe_Landslide',
                 var_type = "saturated_hydraulic_conductivty",
                 direction = "x",
                 unit = "2/2",
                 data_source = '10.1155/2018/7290640',
                 country_code = 'CHN')

    df = fill_df(df, f_path="../data_prep/soil_variograms/Bekkevoort_field_experiment_BEL/variogram_saturated_conductivity_layer_1.csv",
                 site_id = 'Bekkevoort_field_experiment',
                 var_type = "saturated_hydraulic_conductivty",
                 direction = "x",
                 unit = "1/3",
                 data_source = '10.1097/00010694-199603000-00003',
                 country_code = 'BEL') 
    df = fill_df(df, f_path="../data_prep/soil_variograms/Bekkevoort_field_experiment_BEL/variogram_saturated_conductivity_layer_2.csv",
                 site_id = 'Bekkevoort_field_experiment',
                 var_type = "saturated_hydraulic_conductivty",
                 direction = "x",
                 unit = "2/3",
                 data_source = '10.1097/00010694-199603000-00003',
                 country_code = 'BEL')
    df = fill_df(df, f_path="../data_prep/soil_variograms/Bekkevoort_field_experiment_BEL/variogram_saturated_conductivity_layer_3.csv",
                 site_id = 'Bekkevoort_field_experiment',
                 var_type = "saturated_hydraulic_conductivty",
                 direction = "x",
                 unit = "3/3",
                 data_source = '10.1097/00010694-199603000-00003',
                 country_code = 'BEL')

    df = fill_df(df, f_path="../data_prep/soil_variograms/Botucatu_Formation_BRA/variogram_saturated_conductivity.csv",
                 site_id = 'Botucatu_Formation',
                 var_type = "saturated_hydraulic_conductivty",
                 direction = "x",
                 unit = "1/1",
                 data_source = '10.1016/j.compgeo.2018.03.004',
                 country_code = 'BRA')

    df = fill_df(df, f_path="../data_prep/soil_variograms/Caldwell_County_site_US/variogram_saturated_conductivity.csv",
                 site_id = 'Caldwell_County_site',
                 var_type = "saturated_hydraulic_conductivty",
                 direction = "x",
                 unit = "1/1",
                 data_source = '10.1016/j.catena.2019.104335',
                 country_code = 'USA')

    df = fill_df(df, f_path="../data_prep/soil_variograms/Calingri_farm_site_AUS/variogram_saturated_conductivity.csv",
                 site_id = 'Calingri_farm_site',
                 var_type = "saturated_hydraulic_conductivty",
                 direction = "x",
                 unit = "1/1",
                 data_source = '10.2136/sssaj2004.0312',
                 country_code = 'AUS')

    df = fill_df(df, f_path="../data_prep/soil_variograms/Campania_Plain_site_ITA/variogram_saturated_conductivity.csv",
                 site_id = 'Campania_Plain_site',
                 var_type = "saturated_hydraulic_conductivty",
                 direction = "x",
                 unit = "1/1",
                 data_source = '10.1016/0016-7061(94)00050-K',
                 country_code = 'ITA')

    df = fill_df(df, f_path="../data_prep/soil_variograms/Campinas_Experimental_Center_BRZ/variogram_saturated_conductivity.csv",
                 site_id = 'Campinas_Experimental_Center',
                 var_type = "saturated_hydraulic_conductivty",
                 direction = "x",
                 unit = "1/1",
                 data_source = '10.1590/S0100-06832010000100001',
                 country_code = 'BRA')

    df = fill_df(df, f_path="../data_prep/soil_variograms/Cemagref_Experimental_Station_FRA/variogram_saturated_conductivity.csv",
                 site_id = 'Cemagref_Experimental_Station',
                 var_type = "saturated_hydraulic_conductivty",
                 direction = "x",
                 unit = "1/1",
                 data_source = '10.1016/j.agwat.2010.05.005',
                 country_code = 'FRA')

    df = fill_df(df, f_path="../data_prep/soil_variograms/CNR_experimental_farm_ITA/variogram_saturated_conductivity.csv",
                 site_id = 'CNR_experimental_farm',
                 var_type = "saturated_hydraulic_conductivty",
                 direction = "x",
                 unit = "1/1",
                 data_source = '10.1016/0016-7061(93)90025-G',
                 country_code = 'ITA')

    df = fill_df(df, f_path="../data_prep/soil_variograms/Dal_Lake_catchment_IND/variogram_saturated_conductivity.csv",
                 site_id = 'Dal_Lake_catchment',
                 var_type = "saturated_hydraulic_conductivty",
                 direction = "x",
                 unit = "1/1",
                 data_source = '10.1134/S1064229320030060',
                 country_code = 'IND')

    df = fill_df(df, f_path="../data_prep/soil_variograms/Domaine_of_Lavalette_FRA/variogram_saturated_conductivity.csv",
                 site_id = 'Domaine_of_Lavalette',
                 var_type = "saturated_hydraulic_conductivty",
                 direction = "x",
                 unit = "1/1",
                 data_source = '10.1016/0933-3630(94)90020-5',
                 country_code = 'FRA')

    df = fill_df(df, f_path="../data_prep/soil_variograms/East_Central_Kansas_US/variogram_saturated_conductivity.csv",
                 site_id = 'East_Central_Kansas',
                 var_type = "saturated_hydraulic_conductivty",
                 direction = "x",
                 unit = "1/1",
                 data_source = '10.1061/(ASCE)1084-0699(1996)1:3(131)',
                 country_code = 'USA')

    df = fill_df(df, f_path="../data_prep/soil_variograms/Eutric_Regosol_site_Bel/variogram_saturated_conductivity_layer_1.csv",
                 site_id = 'Eutric_Regosol_site',
                 var_type = "saturated_hydraulic_conductivty",
                 direction = "x",
                 unit = "1/3",
                 data_source = '10.1016/S0933-3630(96)00093-1',
                 country_code = 'BEL')
    df = fill_df(df, f_path="../data_prep/soil_variograms/Eutric_Regosol_site_Bel/variogram_saturated_conductivity_layer_2.csv",
                 site_id = 'Eutric_Regosol_site',
                 var_type = "saturated_hydraulic_conductivty",
                 direction = "x",
                 unit = "2/3",
                 data_source = '10.1016/S0933-3630(96)00093-1',
                 country_code = 'BEL')
    df = fill_df(df, f_path="../data_prep/soil_variograms/Eutric_Regosol_site_Bel/variogram_saturated_conductivity_layer_3.csv",
                 site_id = 'Eutric_Regosol_site',
                 var_type = "saturated_hydraulic_conductivty",
                 direction = "x",
                 unit = "3/3",
                 data_source = '10.1016/S0933-3630(96)00093-1',
                 country_code = 'BEL')

    df = fill_df(df, f_path="../data_prep/soil_variograms/Fall_Line_Hills_Pine_Flat_US/variogram_saturated_conductivity.csv",
                 site_id = 'Fall_Line_Hills_Pine_Flat',
                 var_type = "saturated_hydraulic_conductivty",
                 direction = "x",
                 unit = "1/1",
                 data_source = '10.2136/sssaj1998.03615995006200010012x',
                 country_code = 'USA')

    df = fill_df(df, f_path="../data_prep/soil_variograms/Fall_Line_Hills_Troup_US/variogram_saturated_conductivity.csv",
                 site_id = 'Fall_Line_Hills_Troup',
                 var_type = "saturated_hydraulic_conductivty",
                 direction = "x",
                 unit = "1/1",
                 data_source = '10.2136/sssaj1998.03615995006200010012x',
                 country_code = 'USA')

    df = fill_df(df, f_path="../data_prep/soil_variograms/Fuchu_Honmachi_paddy_field_JPN/variogram_saturated_conductivity.csv",
                 site_id = 'Fuchu_Honmachi_paddy_field',
                 var_type = "saturated_hydraulic_conductivty",
                 direction = "x",
                 unit = "1/1",
                 data_source = '10.1007/s10333-009-0190-x',
                 country_code = 'JPN')

    df = fill_df(df, f_path="../data_prep/soil_variograms/Heihe_River_Basin_CHN/variogram_saturated_conductivity.csv",
                 site_id = 'Heihe_River_Basin',
                 var_type = "saturated_hydraulic_conductivty",
                 direction = "x",
                 unit = "1/1",
                 data_source = '10.1002/hyp.10544',
                 country_code = 'CHN')

    df = fill_df(df, f_path="../data_prep/soil_variograms/Huanjiang_Observation_and_Research_Station_CHN/variogram_saturated_conductivity.csv",
                 site_id = 'Huanjiang_Observation_and_Research_Station',
                 var_type = "saturated_hydraulic_conductivty",
                 direction = "x",
                 unit = "1/1",
                 data_source = '10.1007/s12665-015-4238-5',
                 country_code = 'CHN')

    df = fill_df(df, f_path="../data_prep/soil_variograms/Instituto_Agronomico_Campinas_BRA/variogram_saturated_conductivity_layer_1.csv",
                 site_id = 'Instituto_Agronomico_Campinas',
                 var_type = "saturated_hydraulic_conductivty",
                 direction = "x",
                 unit = "1/2",
                 data_source = '10.1590/S0100-06832010000100001',
                 country_code = 'BRA')
    df = fill_df(df, f_path="../data_prep/soil_variograms/Instituto_Agronomico_Campinas_BRA/variogram_saturated_conductivity_layer_2.csv",
                 site_id = 'Instituto_Agronomico_Campinas',
                 var_type = "saturated_hydraulic_conductivty",
                 direction = "x",
                 unit = "2/2",
                 data_source = '10.1590/S0100-06832010000100001',
                 country_code = 'BRA')

    df = fill_df(df, f_path="../data_prep/soil_variograms/Karkheh_River_site_IRN/variogram_saturated_conductivity.csv",
                 site_id = 'Karkheh_River_site',
                 var_type = "saturated_hydraulic_conductivty",
                 direction = "x",
                 unit = "1/1",
                 data_source = '10.13031/2013.28512',
                 country_code = 'IRN')

    df = fill_df(df, f_path="../data_prep/soil_variograms/Karrendorfer_Wiesen_GER/variogram_saturated_conductivity.csv",
                 site_id = 'Karrendorfer_Wiesen',
                 var_type = "saturated_hydraulic_conductivty",
                 direction = "x",
                 unit = "1/1",
                 data_source = '10.19189/MaP.2019.GDC.StA.1779',
                 country_code = 'DEU')

    df = fill_df(df, f_path="../data_prep/soil_variograms/Key_Lake_Uranium_Mine_CAN/variogram_saturated_conductivity.csv",
                 site_id = 'Key_Lake_Uranium_Mine',
                 var_type = "saturated_hydraulic_conductivty",
                 direction = "x",
                 unit = "1/1",
                 data_source = '10.1016/j.geoderma.2015.08.014',
                 country_code = 'CAN')

    df = fill_df(df, f_path="../data_prep/soil_variograms/Konza_Prairie_US/variogram_saturated_conductivity.csv",
                 site_id = 'Konza_Prairie',
                 var_type = "saturated_hydraulic_conductivty",
                 direction = "x",
                 unit = "1/1",
                 data_source = '10.1061/(ASCE)1084-0699(1996)1:3(131)',
                 country_code = 'USA')

    df = fill_df(df, f_path="../data_prep/soil_variograms/Krauthausen_site_GER/variogram_saturated_conductivity.csv",
                 site_id = 'Krauthausen_site',
                 var_type = "saturated_hydraulic_conductivty",
                 direction = "x",
                 unit = "1/1",
                 data_source = '10.1016/j.jconhyd.2007.07.013',
                 country_code = 'DEU')

    df = fill_df(df, f_path="../data_prep/soil_variograms/Kwinana_Bauxite_Residue_Disposal_Area_AUS/variogram_saturated_conductivity.csv",
                 site_id = 'Kwinana_Bauxite_Residue_Disposal_Area',
                 var_type = "saturated_hydraulic_conductivty",
                 direction = "x",
                 unit = "1/1",
                 data_source = '10.1016/j.geoderma.2011.06.010',
                 country_code = 'AUS')

    df = fill_df(df, f_path="../data_prep/soil_variograms/LaoYeManQu_watershed_CHN/variogram_saturated_conductivity.csv",
                 site_id = 'LaoYeManQu_watershed',
                 var_type = "saturated_hydraulic_conductivty",
                 direction = "x",
                 unit = "1/1",
                 data_source = '10.1061/(ASCE)HE.1943-5584.0000630',
                 country_code = 'CHN')

    df = fill_df(df, f_path="../data_prep/soil_variograms/Loess_Plateau_CHN/variogram_saturated_conductivity.csv",
                 site_id = 'Loess_Plateau',
                 var_type = "saturated_hydraulic_conductivty",
                 direction = "x",
                 unit = "1/1",
                 data_source = '10.1016/j.jhydrol.2013.02.006',
                 country_code = 'CHN')

    df = fill_df(df, f_path="../data_prep/soil_variograms/Lutzito_catchment_PAN/variogram_saturated_conductivity.csv",
                 site_id = 'Lutzito_catchment',
                 var_type = "saturated_hydraulic_conductivty",
                 direction = "x",
                 unit = "1/1",
                 data_source = '10.1016/j.geoderma.2012.11.002',
                 country_code = 'PAN')

    df = fill_df(df, f_path="../data_prep/soil_variograms/Lykorrema_stream_GRE/variogram_saturated_conductivity.csv",
                 site_id = 'Lykorrema_stream',
                 var_type = "saturated_hydraulic_conductivty",
                 direction = "x",
                 unit = "1/1",
                 data_source = '10.1080/02626667.2020.1831694',
                 country_code = 'GRC')

    df = fill_df(df, f_path="../data_prep/soil_variograms/Mahantango_Creek_watershed_US/variogram_saturated_conductivity_layer_1.csv",
                 site_id = 'Mahantango_Creek_watershed',
                 var_type = "saturated_hydraulic_conductivty",
                 direction = "x",
                 unit = "1/3",
                 data_source = '10.1080/02693799608902090',
                 country_code = 'USA')
    df = fill_df(df, f_path="../data_prep/soil_variograms/Mahantango_Creek_watershed_US/variogram_saturated_conductivity_layer_2.csv",
                 site_id = 'Mahantango_Creek_watershed',
                 var_type = "saturated_hydraulic_conductivty",
                 direction = "x",
                 unit = "2/3",
                 data_source = '10.1080/02693799608902090',
                 country_code = 'USA')
    df = fill_df(df, f_path="../data_prep/soil_variograms/Mahantango_Creek_watershed_US/variogram_saturated_conductivity_layer_3.csv",
                 site_id = 'Mahantango_Creek_watershed',
                 var_type = "saturated_hydraulic_conductivty",
                 direction = "x",
                 unit = "3/3",
                 data_source = '10.1080/02693799608902090',
                 country_code = 'USA')

    df = fill_df(df, f_path="../data_prep/soil_variograms/Manoa_Waimanalo_Research_Station_US/variogram_saturated_conductivity.csv",
                 site_id = 'Manoa_Waimanalo_Research_Station',
                 var_type = "saturated_hydraulic_conductivty",
                 direction = "x",
                 unit = "1/1",
                 data_source = '10.3390/agronomy9110750',
                 country_code = 'USA')

    df = fill_df(df, f_path="../data_prep/soil_variograms/Mansoura_site_EGY/variogram_saturated_conductivity.csv",
                 site_id = 'Mansoura_site',
                 var_type = "saturated_hydraulic_conductivty",
                 direction = "x",
                 unit = "1/1",
                 data_source = '10.1016/0016-7061(93)90040-R',
                 country_code = 'EGY')

    df = fill_df(df, f_path="../data_prep/soil_variograms/MonDak_Irrigation_Research_Farm_US/variogram_saturated_conductivity.csv",
                 site_id = 'MonDak_Irrigation_Research_Farm',
                 var_type = "saturated_hydraulic_conductivty",
                 direction = "x",
                 unit = "1/1",
                 data_source = '10.13031/2013.29957',
                 country_code = 'USA')

    df = fill_df(df, f_path="../data_prep/soil_variograms/Nazareno_site_BRZ/variogram_saturated_conductivity.csv",
                 site_id = 'Nazareno_site',
                 var_type = "saturated_hydraulic_conductivty",
                 direction = "x",
                 unit = "1/1",
                 data_source = '10.1016/j.still.2021.105127',
                 country_code = 'BRA')

    df = fill_df(df, f_path="../data_prep/soil_variograms/Neckar_river_valley_GER/variogram_saturated_conductivity_layer_1_x.csv",
                 site_id = 'Neckar_river_valley',
                 var_type = "saturated_hydraulic_conductivty",
                 direction = "x",
                 unit = "1/2",
                 data_source = '10.1002/2014WR015566',
                 country_code = 'DEU')
    df = fill_df(df, f_path="../data_prep/soil_variograms/Neckar_river_valley_GER/variogram_saturated_conductivity_layer_1_z.csv",
                 site_id = 'Neckar_river_valley',
                 var_type = "saturated_hydraulic_conductivty",
                 direction = "z",
                 unit = "1/2",
                 data_source = '10.1002/2014WR015566',
                 country_code = 'DEU')
    df = fill_df(df, f_path="../data_prep/soil_variograms/Neckar_river_valley_GER/variogram_saturated_conductivity_layer_2_x.csv",
                 site_id = 'Neckar_river_valley',
                 var_type = "saturated_hydraulic_conductivty",
                 direction = "x",
                 unit = "2/2",
                 data_source = '10.1002/2014WR015566',
                 country_code = 'DEU')
    df = fill_df(df, f_path="../data_prep/soil_variograms/Neckar_river_valley_GER/variogram_saturated_conductivity_layer_2_z.csv",
                 site_id = 'Neckar_river_valley',
                 var_type = "saturated_hydraulic_conductivty",
                 direction = "z",
                 unit = "2/2",
                 data_source = '10.1002/2014WR015566',
                 country_code = 'DEU')

    df = fill_df(df, f_path="../data_prep/soil_variograms/Nevada_Test_Site_US/variogram_saturated_conductivity.csv",
                 site_id = 'Nevada_Test_Site',
                 var_type = "saturated_hydraulic_conductivty",
                 direction = "x",
                 unit = "1/1",
                 data_source = '10.2136/sssaj1994.03615995005800040007x',
                 country_code = 'USA')

    df = fill_df(df, f_path="../data_prep/soil_variograms/Nile_delta_EGY/variogram_saturated_conductivity.csv",
                 site_id = 'Nile_delta',
                 var_type = "saturated_hydraulic_conductivty",
                 direction = "x",
                 unit = "1/1",
                 data_source = '10.1016/S0378-3774(98)00046-8',
                 country_code = 'EGY')

    df = fill_df(df, f_path="../data_prep/soil_variograms/Northeast_China_CHN/variogram_saturated_conductivity.csv",
                 site_id = 'Northeast_China',
                 var_type = "saturated_hydraulic_conductivty",
                 direction = "x",
                 unit = "1/1",
                 data_source = '10.1016/j.catena.2022.106115',
                 country_code = 'CHN')

    df = fill_df(df, f_path="../data_prep/soil_variograms/Ondokuz_Mayis_University_TUR/variogram_saturated_conductivity.csv",
                 site_id = 'Ondokuz_Mayis_University',
                 var_type = "saturated_hydraulic_conductivty",
                 direction = "x",
                 unit = "1/1",
                 data_source = '10.18393/ejss.2016.3.192-200',
                 country_code = 'TUR')

    df = fill_df(df, f_path="../data_prep/soil_variograms/Orchard_Experiment_site_US/variogram_saturated_conductivity_x.csv",
                 site_id = 'Orchard_Experiment_site',
                 var_type = "saturated_hydraulic_conductivty",
                 direction = "x",
                 unit = "1/1",
                 data_source = '10.2136/vzj2008.0087',
                 country_code = 'USA')
    df = fill_df(df, f_path="../data_prep/soil_variograms/Orchard_Experiment_site_US/variogram_saturated_conductivity_z.csv",
                 site_id = 'Orchard_Experiment_site',
                 var_type = "saturated_hydraulic_conductivty",
                 direction = "z",
                 unit = "1/1",
                 data_source = '10.2136/vzj2008.0087',
                 country_code = 'USA')

    df = fill_df(df, f_path="../data_prep/soil_variograms/Pars_Abad_IRN/variogram_saturated_conductivity.csv",
                 site_id = 'Pars_Abad',
                 var_type = "saturated_hydraulic_conductivty",
                 direction = "x",
                 unit = "1/1",
                 data_source = '10.1007/s12517-018-3788-8',
                 country_code = 'IRN')

    df = fill_df(df, f_path="../data_prep/soil_variograms/Pla_de_Sant_Jordi_ESP/variogram_saturated_conductivity_layer_1.csv",
                 site_id = 'Pla_de_Sant_Jordi',
                 var_type = "saturated_hydraulic_conductivty",
                 direction = "x",
                 unit = "1/2",
                 data_source = '10.1016/j.catena.2021.105788',
                 country_code = 'ESP')
    df = fill_df(df, f_path="../data_prep/soil_variograms/Pla_de_Sant_Jordi_ESP/variogram_saturated_conductivity_layer_2.csv",
                 site_id = 'Pla_de_Sant_Jordi',
                 var_type = "saturated_hydraulic_conductivty",
                 direction = "x",
                 unit = "2/2",
                 data_source = '10.1016/j.catena.2021.105788',
                 country_code = 'ESP')

    df = fill_df(df, f_path="../data_prep/soil_variograms/Plastic_Lake_watershed_CAN/variogram_saturated_conductivity.csv",
                 site_id = 'Plastic_Lake_watershed',
                 var_type = "saturated_hydraulic_conductivty",
                 direction = "x",
                 unit = "1/1",
                 data_source = '10.1016/S0022-1694(97)00095-4',
                 country_code = 'CAN')

    df = fill_df(df, f_path="../data_prep/soil_variograms/Reserva_Biosfera_de_San_Francisco_ECU/variogram_saturated_conductivity_layer_1.csv",
                 site_id = 'Reserva_Biosfera_de_San_Francisco',
                 var_type = "saturated_hydraulic_conductivty",
                 direction = "x",
                 unit = "1/3",
                 data_source = '10.1029/2007WR006604',
                 country_code = 'ECU')
    df = fill_df(df, f_path="../data_prep/soil_variograms/Reserva_Biosfera_de_San_Francisco_ECU/variogram_saturated_conductivity_layer_2.csv",
                 site_id = 'Reserva_Biosfera_de_San_Francisco',
                 var_type = "saturated_hydraulic_conductivty",
                 direction = "x",
                 unit = "2/3",
                 data_source = '10.1029/2007WR006604',
                 country_code = 'ECU')
    df = fill_df(df, f_path="../data_prep/soil_variograms/Reserva_Biosfera_de_San_Francisco_ECU/variogram_saturated_conductivity_layer_3.csv",
                 site_id = 'Reserva_Biosfera_de_San_Francisco',
                 var_type = "saturated_hydraulic_conductivty",
                 direction = "x",
                 unit = "3/3",
                 data_source = '10.1029/2007WR006604',
                 country_code = 'ECU')

    df = fill_df(df, f_path="../data_prep/soil_variograms/Ribeirao_Marcela_watershed_BRA/variogram_saturated_conductivity.csv",
                 site_id = 'Ribeirao_Marcela_watershed',
                 var_type = "saturated_hydraulic_conductivty",
                 direction = "x",
                 unit = "1/1",
                 data_source = '10.1590/S0100-06832007000300003',
                 country_code = 'BRA')

    df = fill_df(df, f_path="../data_prep/soil_variograms/Ribera_Seca_catchment_POR/variogram_saturated_conductivity.csv",
                 site_id = 'Ribera_Seca_catchment',
                 var_type = "saturated_hydraulic_conductivty",
                 direction = "x",
                 unit = "1/1",
                 data_source = '10.1002/esp.3501',
                 country_code = 'POR')

    df = fill_df(df, f_path="../data_prep/soil_variograms/Saby_site_SWE/variogram_saturated_conductivity.csv",
                 site_id = 'Saby_site',
                 var_type = "saturated_hydraulic_conductivty",
                 direction = "x",
                 unit = "1/1",
                 data_source = '10.2136/sssaj1999.03615995006300030010x',
                 country_code = 'SWE')

    df = fill_df(df, f_path="../data_prep/soil_variograms/Shenmu_County_watershed_CHN/variogram_saturated_conductivity.csv",
                 site_id = 'Shenmu_County_watershed',
                 var_type = "saturated_hydraulic_conductivty",
                 direction = "x",
                 unit = "1/1",
                 data_source = '10.1002/ldr.1128',
                 country_code = 'CHN')

    df = fill_df(df, f_path="../data_prep/soil_variograms/Smeaton_farm_field_CAN/variogram_saturated_conductivity.csv",
                 site_id = 'Smeaton_farm_field',
                 var_type = "saturated_hydraulic_conductivty",
                 direction = "x",
                 unit = "1/1",
                 data_source = '10.4141/cjss08052',
                 country_code = 'CAN')

    df = fill_df(df, f_path="../data_prep/soil_variograms/South_Jingyang_Plateau_CHN/variogram_saturated_conductivity_layer_1.csv",
                 site_id = 'South_Jingyang_Plateau',
                 var_type = "saturated_hydraulic_conductivty",
                 direction = "x",
                 unit = "1/2",
                 data_source = '10.1016/j.enggeo.2017.08.002',
                 country_code = 'CHN')
    df = fill_df(df, f_path="../data_prep/soil_variograms/South_Jingyang_Plateau_CHN/variogram_saturated_conductivity_layer_2.csv",
                 site_id = 'South_Jingyang_Plateau',
                 var_type = "saturated_hydraulic_conductivty",
                 direction = "x",
                 unit = "2/2",
                 data_source = '10.1016/j.enggeo.2017.08.002',
                 country_code = 'CHN')

    df = fill_df(df, f_path="../data_prep/soil_variograms/Spanish_mainland_ESP/variogram_saturated_conductivity.csv",
                 site_id = 'Spanish_mainland',
                 var_type = "saturated_hydraulic_conductivty",
                 direction = "x",
                 unit = "1/1",
                 data_source = '10.1016/j.geoderma.2004.02.011',
                 country_code = 'ESP')

    df = fill_df(df, f_path="../data_prep/soil_variograms/Vargem_de_Caldas_basin_BRZ/variogram_saturated_conductivity_layer_1.csv",
                 site_id = 'Vargem_de_Caldas_basin',
                 var_type = "saturated_hydraulic_conductivty",
                 direction = "x",
                 unit = "1/2",
                 data_source = '10.1016/j.envsoft.2013.01.009',
                 country_code = 'BRA')
    df = fill_df(df, f_path="../data_prep/soil_variograms/Vargem_de_Caldas_basin_BRZ/variogram_saturated_conductivity_layer_2.csv",
                 site_id = 'Vargem_de_Caldas_basin',
                 var_type = "saturated_hydraulic_conductivty",
                 direction = "x",
                 unit = "2/2",
                 data_source = '10.1016/j.envsoft.2013.01.009',
                 country_code = 'BRA')

    df = fill_df(df, f_path="../data_prep/soil_variograms/Waimanalo_Research_Station_US/variogram_saturated_conductivity.csv",
                 site_id = 'Waimanalo_Research_Station',
                 var_type = "saturated_hydraulic_conductivty",
                 direction = "x",
                 unit = "1/1",
                 data_source = '10.3390/agronomy9110750',
                 country_code = 'USA')

    df = fill_df(df, f_path="../data_prep/soil_variograms/Water_management_study_site_US/variogram_saturated_conductivity.csv",
                 site_id = 'Water_management_study_site',
                 var_type = "saturated_hydraulic_conductivty",
                 direction = "x",
                 unit = "1/1",
                 data_source = '10.13031/2013.31743',
                 country_code = 'USA')

    df = fill_df(df, f_path="../data_prep/soil_variograms/West_Side_Field_Station_US/variogram_saturated_conductivity.csv",
                 site_id = 'West_Side_Field_Station',
                 var_type = "saturated_hydraulic_conductivty",
                 direction = "x",
                 unit = "1/1",
                 data_source = '10.2136/sssaj1990.03615995005400060005x',
                 country_code = 'USA')

    df = fill_df(df, f_path="../data_prep/soil_variograms/Xilin_River_basin_CHN/variogram_saturated_conductivity.csv",
                 site_id = 'Xilin_River_basin',
                 var_type = "saturated_hydraulic_conductivty",
                 direction = "x",
                 unit = "1/1",
                 data_source = '10.1016/j.ecolmodel.2007.02.019',
                 country_code = 'CHN')
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    # write data frame to file
    write_df(df)
    