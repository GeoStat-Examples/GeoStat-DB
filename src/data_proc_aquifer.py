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
    
    df.to_csv('../data_proc/aquifer_variogram.csv')


if __name__ == '__main__':
    
    # create data frame
    
    df = init_df()
    
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/Aa_river_Bel/variogram_conductivity_x.csv",
                 site_id = 'Aa_river',
                 var_type = "hydraulic_conductivty",
                 direction = "x",
                 unit = "1/1",
                 data_source = '10.1016/j.jhydrol.2018.03.002',
                 country_code = 'BEL')
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/Aa_river_Bel/variogram_conductivity_z.csv",
                 site_id = 'Aa_river',
                 var_type = "hydraulic_conductivty",
                 direction = "z",
                 unit = "1/1",
                 data_source = '10.1016/j.jhydrol.2018.03.002',
                 country_code = 'BEL')
    
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/Aa_river_weir_2_BEL/variogram_conductivity.csv",
                 site_id = 'Aa_river_weir_2',
                 var_type = "hydraulic_conductivty",
                 direction = "x",
                 unit = "1/1",
                 data_source = '10.1007/s10040-018-1862-7',
                 country_code = 'BEL')
    
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/Alamitos_saltwater_intrusion_barrier_US/variogram_conductivity_layer_1.csv",
                 site_id = 'Alamitos_saltwater_intrusion_barrier',
                 var_type = "hydraulic_conductivty",
                 direction = "x",
                 unit = "1/2",
                 data_source = '10.1111/j.1752-1688.2007.00098.x',
                 country_code = 'USA')
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/Alamitos_saltwater_intrusion_barrier_US/variogram_conductivity_layer_2.csv",
                 site_id = 'Alamitos_saltwater_intrusion_barrier',
                 var_type = "hydraulic_conductivty",
                 direction = "x",
                 unit = "2/2",
                 data_source = '10.1111/j.1752-1688.2007.00098.x',
                 country_code = 'USA')
    
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/Alberta_CAN/variogram_conductivity.csv",
                 site_id = 'Alberta_basin',
                 var_type = "hydraulic_conductivty",
                 direction = "x",
                 unit = "1/1",
                 data_source = '10.1029/93WR02980',
                 country_code = 'CAN')
    
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/Algerita_escarpment_US/variogram_permeability.csv",
                 site_id = 'Algerita_escarpment',
                 var_type = "permeability",
                 direction = "x",
                 unit = "1/1",
                 data_source = '10.1306/A25FEC93-171B-11D7-8645000102C1865D',
                 country_code = 'USA')
    
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/Almonte-Marismas_groundwater_system_SPA/variogram_permeability_x.csv",
                 site_id = 'Almonte-Marismas_groundwater_system',
                 var_type = "permeability",
                 direction = "x",
                 unit = "1/1",
                 data_source = '10.3390/w11010039',
                 country_code = 'ESP')
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/Almonte-Marismas_groundwater_system_SPA/variogram_permeability_z.csv",
                 site_id = 'Almonte-Marismas_groundwater_system',
                 var_type = "permeability",
                 direction = "z",
                 unit = "1/1",
                 data_source = '10.3390/w11010039',
                 country_code = 'ESP')
    
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/Aspo_site_SWE/variogram_conductivity.csv",
                 site_id = 'Aspo_site',
                 var_type = "hydraulic_conductivty",
                 direction = "x",
                 unit = "1/1",
                 data_source = '10.1111/j.1745-6584.2005.tb02284.x',
                 country_code = 'SWE')
    
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/Baishuihe_landslide_CHI/variogram_conductivity.csv",
                 site_id = 'Baishuihe_landslide',
                 var_type = "hydraulic_conductivty",
                 direction = "x",
                 unit = "1/1",
                 data_source = '10.1155/2018/7290640',
                 country_code = 'CHN')
    
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/Barry_Steam_Plant_site_US/variogram_conductivity_layer_1.csv",
                 site_id = 'Barry_Steam_Plant_site',
                 var_type = "hydraulic_conductivty",
                 direction = "x",
                 unit = "1/2",
                 data_source = '10.1111/j.1745-6584.1995.tb00279.x',
                 country_code = 'USA')
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/Barry_Steam_Plant_site_US/variogram_conductivity_layer_2.csv",
                 site_id = 'Barry_Steam_Plant_site',
                 var_type = "hydraulic_conductivty",
                 direction = "x",
                 unit = "2/2",
                 data_source = '10.1111/j.1745-6584.1995.tb00279.x',
                 country_code = 'USA')
    
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/Beijing_synchrotron_microtomography_CHI/variogram_indicator_x.csv",
                 site_id = 'Beijing_synchrotron_microtomography',
                 var_type = "indicator",
                 direction = "x",
                 unit = "1/1",
                 country_code = 'CHN')
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/Beijing_synchrotron_microtomography_CHI/variogram_indicator_y.csv",
                 site_id = 'Beijing_synchrotron_microtomography',
                 var_type = "indicator",
                 direction = "y",
                 unit = "1/1",
                 country_code = 'CHN')
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/Beijing_synchrotron_microtomography_CHI/variogram_indicator_z.csv",
                 site_id = 'Beijing_synchrotron_microtomography',
                 var_type = "indicator",
                 direction = "z",
                 unit = "1/1",
                 country_code = 'CHN')
    
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/Belgian_nuclear_repository_BEL/variogram_conductivity.csv",
                 site_id = 'Belgian_nuclear_repository',
                 var_type = "hydraulic_conductivity",
                 direction = "x",
                 unit = "1/1",
                 data_source = '10.1007/s10040-006-0035-2',
                 country_code = 'BEL')
    
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/Belridge_field_US/variogram_permeability_x.csv",
                 site_id = 'Belridge_field',
                 var_type = "permeability",
                 direction = "x",
                 unit = "1/1",
                 country_code = 'USA')
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/Belridge_field_US/variogram_permeability_z.csv",
                 site_id = 'Belridge_field',
                 var_type = "permeability",
                 direction = "z",
                 unit = "1/1",
                 country_code = 'USA')
    
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/Berea_sandstone_US/variogram_permeability.csv",
                 site_id = 'Berea_sandstone',
                 var_type = "permeability",
                 direction = "x",
                 unit = "1/1",
                 data_source = '10.1007/BF02768903',
                 country_code = 'USA')
    
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/Bierbeek_quarry_BEL/variogram_conductivity_layer_1.csv",
                 site_id = 'Bierbeek_quarry',
                 var_type = "hydraulic_conductivity",
                 direction = "x",
                 unit = "1/2",
                 data_source = '10.1007/s10040-009-0495-2',
                 country_code = 'BEL')
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/Bierbeek_quarry_BEL/variogram_conductivity_layer_2.csv",
                 site_id = 'Bierbeek_quarry',
                 var_type = "hydraulic_conductivity",
                 direction = "x",
                 unit = "2/2",
                 data_source = '10.1007/s10040-009-0495-2',
                 country_code = 'BEL')
    
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/Biscayne_aquifer_US/variogram_conductivity_x.csv",
                 site_id = 'Biscayne_aquifer',
                 var_type = "hydraulic_conductivity",
                 direction = "x",
                 unit = "1/1",
                 data_source = '10.1111/j.1745-6584.1995.tb00279.x',
                 country_code = 'USA')
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/Biscayne_aquifer_US/variogram_conductivity_z.csv",
                 site_id = 'Biscayne_aquifer',
                 var_type = "hydraulic_conductivity",
                 direction = "z",
                 unit = "1/1",
                 data_source = '10.1111/j.1745-6584.1995.tb00279.x',
                 country_code = 'USA')
    
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/Boise_site_US/variogram_conductivity_x.csv",
                 site_id = 'Boise_site',
                 var_type = "hydraulic_conductivity",
                 direction = "x",
                 unit = "1/1",
                 data_source = '10.1029/2002WR001436',
                 country_code = 'USA')
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/Boise_site_US/variogram_conductivity_z.csv",
                 site_id = 'Boise_site',
                 var_type = "hydraulic_conductivity",
                 direction = "z",
                 unit = "1/1",
                 data_source = '10.1029/2002WR001436',
                 country_code = 'USA')
    
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/Boom_Clay_formation_BEL/variogram_conductivity.csv",
                 site_id = 'Boom_Clay_formation',
                 var_type = "hydraulic_conductivity",
                 direction = "x",
                 unit = "1/1",
                 data_source = '10.1016/j.pce.2013.05.014',
                 country_code = 'BEL')
    
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/Boom_clay_formation_Mol_site_BEL/variogram_conductivity.csv",
                 site_id = 'Boom_clay_formation_Mol_site',
                 var_type = "hydraulic_conductivity",
                 direction = "x",
                 unit = "1/1",
                 data_source = '10.1016/j.clay.2013.02.018',
                 country_code = 'BEL')    
    
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/Borden_aquifer_CAN/variogram_conductivity_x.csv",
                 site_id = 'Borden_aquifer',
                 var_type = "hydraulic_conductivity",
                 direction = "x",
                 unit = "1/1",
                 data_source = '10.1016/0022-1694(95)02805-6',
                 country_code = 'CAN')
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/Borden_aquifer_CAN/variogram_conductivity_z.csv",
                 site_id = 'Borden_aquifer',
                 var_type = "hydraulic_conductivity",
                 direction = "z",
                 unit = "1/1",
                 data_source = '10.1016/0022-1694(95)02805-6',
                 country_code = 'CAN')
    
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/Bosque_site_US/variogram_permeability_x.csv",
                 site_id = 'Bosque_site',
                 var_type = "permeability",
                 direction = "x",
                 unit = "1/1",
                 data_source = '10.1029/97WR01003',
                 country_code = 'USA')
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/Bosque_site_US/variogram_permeability_z.csv",
                 site_id = 'Bosque_site',
                 var_type = "permeability",
                 direction = "z",
                 unit = "1/1",
                 data_source = '10.1029/97WR01003',
                 country_code = 'USA')
    
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/Bouteldja_aquifer_ALG/variogram_conductivity.csv",
                 site_id = 'Bouteldja_aquifer',
                 var_type = "hydraulic_conductivity",
                 direction = "x",
                 unit = "1/1",
                 data_source = '10.1007/s12665-018-8005-2',
                 country_code = 'DZA')
    
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/Cape_Cod_aquifer_US/variogram_conductivity_x.csv",
                 site_id = 'Cape_Cod_aquifer',
                 var_type = "hydraulic_conductivity",
                 direction = "x",
                 unit = "1/1",
                 data_source = '10.1029/96WR00272',
                 country_code = 'USA')
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/Cape_Cod_aquifer_US/variogram_conductivity_z.csv",
                 site_id = 'Cape_Cod_aquifer',
                 var_type = "hydraulic_conductivity",
                 direction = "z",
                 unit = "1/1",
                 data_source = '10.1029/96WR00272',
                 country_code = 'USA')
    
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/Carrizo_aquifer_US/variogram_transmissivity.csv",
                 site_id = 'Carrizo_aquifer',
                 var_type = "hydraulic_transmissivity",
                 direction = "x",
                 unit = "1/1",
                 data_source = '10.1007/s11004-005-7308-5',
                 country_code = 'USA')
    
    
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/Cengio_chemical_facility_ITA/variogram_conductivity.csv",
                 site_id = 'Cengio_chemical_facility',
                 var_type = "hydraulic_condutivity",
                 direction = "x",
                 unit = "1/1",
                 data_source = '10.1016/j.jhydrol.2017.08.051',
                 country_code = 'ITA')
    
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/Chicot_Aquifer_system_US/variogram_conductivity.csv",
                 site_id = 'Chicot_aquifer',
                 var_type = "hydraulic_condutivity",
                 direction = "x",
                 unit = "1/1",
                 data_source = '10.1007/s10040-007-0258-x',
                 country_code = 'USA')
    
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/Choushui_river_alluvial_fan_TAI/variogram_conductivity_layer_1.csv",
                 site_id = 'Choushui_river_alluvial_fan',
                 var_type = "hydraulic_condutivity",
                 direction = "x",
                 unit = "1/3",
                 data_source = '10.1002/hyp.1397',
                 country_code = 'TWN')
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/Choushui_river_alluvial_fan_TAI/variogram_conductivity_layer_2.csv",
                 site_id = 'Choushui_river_alluvial_fan',
                 var_type = "hydraulic_condutivity",
                 direction = "x",
                 unit = "2/3",
                 data_source = '10.1002/hyp.1397',
                 country_code = 'TWN')
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/Choushui_river_alluvial_fan_TAI/variogram_conductivity_layer_3.csv",
                 site_id = 'Choushui_river_alluvial_fan',
                 var_type = "hydraulic_condutivity",
                 direction = "x",
                 unit = "3/3",
                 data_source = '10.1002/hyp.1397',
                 country_code = 'TWN')
    
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/Clyde_Basin_UK/variogram_conductivity_x.csv",
                 site_id = 'Clyde_Basin',
                 var_type = "hydraulic_conductivity",
                 direction = "x",
                 unit = "1/1",
                 data_source = '10.1017/S1755691018000312',
                 country_code = 'GBR')
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/Clyde_Basin_UK/variogram_conductivity_z.csv",
                 site_id = 'Clyde_Basin',
                 var_type = "hydraulic_conductivity",
                 direction = "z",
                 unit = "1/1",
                 data_source = '10.1017/S1755691018000312',
                 country_code = 'GBR')
    
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/Dammam_aquifer_KUW/variogram_transmissivity.csv",
                 site_id = 'Dammam_aquifer',
                 var_type = "hydraulic_transmissivity",
                 direction = "x",
                 unit = "1/1",
                 data_source = '10.3390/w10070828',
                 country_code = 'KWT')
    
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/Drau_valley_AUT/variogram_permeability_x.csv",
                 site_id = 'Drau_valley',
                 var_type = "permeability",
                 direction = "x",
                 unit = "1/1",
                 data_source = '10.1306/E4FD3351-1732-11D7-8645000102C1865D',
                 country_code = 'AUT')
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/Drau_valley_AUT/variogram_permeability_z.csv",
                 site_id = 'Drau_valley',
                 var_type = "permeability",
                 direction = "z",
                 unit = "1/1",
                 data_source = '10.1306/E4FD3351-1732-11D7-8645000102C1865D',
                 country_code = 'AUT')
    
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/Dulliu_area_TAI/variogram_transmissivity.csv",
                 site_id = 'Dulliu_area',
                 var_type = "hydraulic_transmissivity",
                 direction = "x",
                 unit = "1/1",
                 data_source = '10.1007/s002540000150',
                 country_code = 'TWN')
    
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/Enfida_plain_TUN/variogram_transmissivity.csv",
                 site_id = 'Enfida_plain',
                 var_type = "hydraulic_transmissivity",
                 direction = "x",
                 unit = "1/1",
                 data_source = '10.1007/s12517-012-0814-0',
                 country_code = 'TUN')
    
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/Eocene_Ainsa_basin_SPA/variogram_permeability_x.csv",
                 site_id = 'Eocene_Ainsa_basin',
                 var_type = "permeability",
                 direction = "x",
                 unit = "1/1",
                 data_source = '10.1306/02070605112',
                 country_code = 'ESP')
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/Eocene_Ainsa_basin_SPA/variogram_permeability_z.csv",
                 site_id = 'Eocene_Ainsa_basin',
                 var_type = "permeability",
                 direction = "z",
                 unit = "1/1",
                 data_source = '10.1306/02070605112',
                 country_code = 'ESP')
    
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/Euganean_basin_ITA/variogram_transmissivity_x.csv",
                 site_id = 'Euganean_basin',
                 var_type = "hydraulic_transmissivity",
                 direction = "x",
                 unit = "1/1",
                 data_source = '10.1111/j.1745-6584.1997.tb00156.x',
                 country_code = 'ITA')
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/Euganean_basin_ITA/variogram_transmissivity_y.csv",
                 site_id = 'Euganean_basin',
                 var_type = "hydraulic_transmissivity",
                 direction = "y",
                 unit = "1/1",
                 data_source = '10.1111/j.1745-6584.1997.tb00156.x',
                 country_code = 'ITA')
    
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/Experimental_EarthScape_facility_US/variogram_conductivity_layer_1_x.csv",
                 site_id = 'Experimental_EarthScape_facility',
                 var_type = "hydraulic_conductivity",
                 direction = "x",
                 unit = "1/12",
                 data_source = '10.1029/2004WR003756',
                 country_code = 'USA')
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/Experimental_EarthScape_facility_US/variogram_conductivity_layer_1_z.csv",
                 site_id = 'Experimental_EarthScape_facility',
                 var_type = "hydraulic_conductivity",
                 direction = "z",
                 unit = "1/12",
                 data_source = '10.1029/2004WR003756',
                 country_code = 'USA')
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/Experimental_EarthScape_facility_US/variogram_conductivity_layer_2_x.csv",
                 site_id = 'Experimental_EarthScape_facility',
                 var_type = "hydraulic_conductivity",
                 direction = "x",
                 unit = "2/12",
                 data_source = '10.1029/2004WR003756',
                 country_code = 'USA')
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/Experimental_EarthScape_facility_US/variogram_conductivity_layer_2_z.csv",
                 site_id = 'Experimental_EarthScape_facility',
                 var_type = "hydraulic_conductivity",
                 direction = "z",
                 unit = "2/12",
                 data_source = '10.1029/2004WR003756',
                 country_code = 'USA')
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/Experimental_EarthScape_facility_US/variogram_conductivity_layer_3_x.csv",
                 site_id = 'Experimental_EarthScape_facility',
                 var_type = "hydraulic_conductivity",
                 direction = "x",
                 unit = "3/12",
                 data_source = '10.1029/2004WR003756',
                 country_code = 'USA')
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/Experimental_EarthScape_facility_US/variogram_conductivity_layer_3_z.csv",
                 site_id = 'Experimental_EarthScape_facility',
                 var_type = "hydraulic_conductivity",
                 direction = "z",
                 unit = "3/12",
                 data_source = '10.1029/2004WR003756',
                 country_code = 'USA')
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/Experimental_EarthScape_facility_US/variogram_conductivity_layer_4_x.csv",
                 site_id = 'Experimental_EarthScape_facility',
                 var_type = "hydraulic_conductivity",
                 direction = "x",
                 unit = "4/12",
                 data_source = '10.1029/2004WR003756',
                 country_code = 'USA')
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/Experimental_EarthScape_facility_US/variogram_conductivity_layer_4_z.csv",
                 site_id = 'Experimental_EarthScape_facility',
                 var_type = "hydraulic_conductivity",
                 direction = "z",
                 unit = "4/12",
                 data_source = '10.1029/2004WR003756',
                 country_code = 'USA')
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/Experimental_EarthScape_facility_US/variogram_conductivity_layer_5_x.csv",
                 site_id = 'Experimental_EarthScape_facility',
                 var_type = "hydraulic_conductivity",
                 direction = "x",
                 unit = "5/12",
                 data_source = '10.1029/2004WR003756',
                 country_code = 'USA')
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/Experimental_EarthScape_facility_US/variogram_conductivity_layer_5_z.csv",
                 site_id = 'Experimental_EarthScape_facility',
                 var_type = "hydraulic_conductivity",
                 direction = "z",
                 unit = "5/12",
                 data_source = '10.1029/2004WR003756',
                 country_code = 'USA')
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/Experimental_EarthScape_facility_US/variogram_conductivity_layer_6_x.csv",
                 site_id = 'Experimental_EarthScape_facility',
                 var_type = "hydraulic_conductivity",
                 direction = "x",
                 unit = "6/12",
                 data_source = '10.1029/2004WR003756',
                 country_code = 'USA')
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/Experimental_EarthScape_facility_US/variogram_conductivity_layer_6_z.csv",
                 site_id = 'Experimental_EarthScape_facility',
                 var_type = "hydraulic_conductivity",
                 direction = "z",
                 unit = "6/12",
                 data_source = '10.1029/2004WR003756',
                 country_code = 'USA')
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/Experimental_EarthScape_facility_US/variogram_conductivity_layer_7_x.csv",
                 site_id = 'Experimental_EarthScape_facility',
                 var_type = "hydraulic_conductivity",
                 direction = "x",
                 unit = "7/12",
                 data_source = '10.1029/2004WR003756',
                 country_code = 'USA')
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/Experimental_EarthScape_facility_US/variogram_conductivity_layer_7_z.csv",
                 site_id = 'Experimental_EarthScape_facility',
                 var_type = "hydraulic_conductivity",
                 direction = "z",
                 unit = "7/12",
                 data_source = '10.1029/2004WR003756',
                 country_code = 'USA')
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/Experimental_EarthScape_facility_US/variogram_conductivity_layer_8_x.csv",
                 site_id = 'Experimental_EarthScape_facility',
                 var_type = "hydraulic_conductivity",
                 direction = "x",
                 unit = "8/12",
                 data_source = '10.1029/2004WR003756',
                 country_code = 'USA')
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/Experimental_EarthScape_facility_US/variogram_conductivity_layer_8_z.csv",
                 site_id = 'Experimental_EarthScape_facility',
                 var_type = "hydraulic_conductivity",
                 direction = "z",
                 unit = "8/12",
                 data_source = '10.1029/2004WR003756',
                 country_code = 'USA')
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/Experimental_EarthScape_facility_US/variogram_conductivity_layer_9_x.csv",
                 site_id = 'Experimental_EarthScape_facility',
                 var_type = "hydraulic_conductivity",
                 direction = "x",
                 unit = "9/12",
                 data_source = '10.1029/2004WR003756',
                 country_code = 'USA')
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/Experimental_EarthScape_facility_US/variogram_conductivity_layer_9_z.csv",
                 site_id = 'Experimental_EarthScape_facility',
                 var_type = "hydraulic_conductivity",
                 direction = "z",
                 unit = "9/12",
                 data_source = '10.1029/2004WR003756',
                 country_code = 'USA')
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/Experimental_EarthScape_facility_US/variogram_conductivity_layer_10_x.csv",
                 site_id = 'Experimental_EarthScape_facility',
                 var_type = "hydraulic_conductivity",
                 direction = "x",
                 unit = "10/12",
                 data_source = '10.1029/2004WR003756',
                 country_code = 'USA')
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/Experimental_EarthScape_facility_US/variogram_conductivity_layer_10_z.csv",
                 site_id = 'Experimental_EarthScape_facility',
                 var_type = "hydraulic_conductivity",
                 direction = "z",
                 unit = "10/12",
                 data_source = '10.1029/2004WR003756',
                 country_code = 'USA')
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/Experimental_EarthScape_facility_US/variogram_conductivity_layer_11_x.csv",
                 site_id = 'Experimental_EarthScape_facility',
                 var_type = "hydraulic_conductivity",
                 direction = "x",
                 unit = "11/12",
                 data_source = '10.1029/2004WR003756',
                 country_code = 'USA')
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/Experimental_EarthScape_facility_US/variogram_conductivity_layer_11_z.csv",
                 site_id = 'Experimental_EarthScape_facility',
                 var_type = "hydraulic_conductivity",
                 direction = "z",
                 unit = "11/12",
                 data_source = '10.1029/2004WR003756',
                 country_code = 'USA')
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/Experimental_EarthScape_facility_US/variogram_conductivity_layer_12_x.csv",
                 site_id = 'Experimental_EarthScape_facility',
                 var_type = "hydraulic_conductivity",
                 direction = "x",
                 unit = "12/12",
                 data_source = '10.1029/2004WR003756',
                 country_code = 'USA')
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/Experimental_EarthScape_facility_US/variogram_conductivity_layer_12_z.csv",
                 site_id = 'Experimental_EarthScape_facility',
                 var_type = "hydraulic_conductivity",
                 direction = "z",
                 unit = "12/12",
                 data_source = '10.1029/2004WR003756',
                 country_code = 'USA')
    
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/Fanshawe_section_gravel_pit_CAN/variogram_conductivity_x.csv",
                 site_id = 'Fanshawe_section_gravel_pit',
                 var_type = "hydraulic_conductivity",
                 direction = "x",
                 unit = "1/1",
                 data_source = '10.1111/j.1745-6584.2003.tb02564.x',
                 country_code = 'CAN')
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/Fanshawe_section_gravel_pit_CAN/variogram_conductivity_z.csv",
                 site_id = 'Fanshawe_section_gravel_pit',
                 var_type = "hydraulic_conductivity",
                 direction = "z",
                 unit = "1/1",
                 data_source = '10.1111/j.1745-6584.2003.tb02564.x',
                 country_code = 'CAN')
    
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/Finnsjon_area_SWE/variogram_conductivity_layer_1.csv",
                 site_id = 'Finnsjon_area',
                 var_type = "variogram_conductivity",
                 direction = "x",
                 unit = "1/2",
                 data_source = '10.1111/j.1745-6584.1993.tb00869.x',
                 country_code = 'SWE')
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/Finnsjon_area_SWE/variogram_conductivity_layer_1.csv",
                 site_id = 'Finnsjon_area',
                 var_type = "variogram_conductivity",
                 direction = "x",
                 unit = "2/2",
                 data_source = '10.1111/j.1745-6584.1993.tb00869.x',
                 country_code = 'SWE')
    
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/Georgetown_site_US/variogram_conductivity_layer_1.csv",
                 site_id = 'Georgetown_site',
                 var_type = "hydraulic_conductivity",
                 direction = "x",
                 unit = "1/3",
                 data_source = '10.1111/j.1745-6584.1997.tb00110.x',
                 country_code = 'USA')
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/Georgetown_site_US/variogram_conductivity_layer_2.csv",
                 site_id = 'Georgetown_site',
                 var_type = "hydraulic_conductivity",
                 direction = "x",
                 unit = "2/3",
                 data_source = '10.1111/j.1745-6584.1997.tb00110.x',
                 country_code = 'USA')
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/Georgetown_site_US/variogram_conductivity_layer_3.csv",
                 site_id = 'Georgetown_site',
                 var_type = "hydraulic_conductivity",
                 direction = "x",
                 unit = "3/3",
                 data_source = '10.1111/j.1745-6584.1997.tb00110.x',
                 country_code = 'USA')
    
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/Hanford_site_US/variogram_conductivity_x.csv",
                 site_id = 'Hanford_site',
                 var_type = "hydraulic_conductivity",
                 direction = "x",
                 unit = "1/1",
                 country_code = 'USA')
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/Hanford_site_US/variogram_conductivity_z.csv",
                 site_id = 'Hanford_site',
                 var_type = "hydraulic_conductivity",
                 direction = "z",
                 unit = "1/1",
                 country_code = 'USA')
    
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/Hawaii_aquifer_Maui_US/variogram_conductivity.csv",
                 site_id = 'Hawaii_aquifer_Maui',
                 var_type = "hydraulic_conductivity",
                 direction = "x",
                 unit = "1/1",
                 data_source = '10.1007/s10040-007-0271-0',
                 country_code = 'USA')
    
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/Hawaii_aquifer_Oahu_US/variogram_conductivity.csv",
                 site_id = 'Hawaii_aquifer_Oahu',
                 var_type = "hydraulic_conductivity",
                 direction = "x",
                 unit = "1/1",
                 data_source = '10.1007/s10040-007-0271-0',
                 country_code = 'USA')
    
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/Heihe_River_basin_CHN/variogram_conductivity.csv",
                 site_id = 'Heihe_River_basin',
                 var_type = "hydraulic_conductivity",
                 direction = "x",
                 unit = "1/1",
                 data_source = '10.1002/2015WR018408',
                 country_code = 'CHN')
    
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/Herten_site_GER/variogram_indicator.csv",
                 site_id = 'Herten_site',
                 var_type = "indicator",
                 direction = "x",
                 unit = "1/1",
                 data_source = '10.1016/j.jhydrol.2011.03.037',
                 country_code = 'DEU')
    
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/Hyderabad_IND/variogram_conductivity.csv",
                 site_id = 'Hyderabad',
                 var_type = "hydraulic_conductivity",
                 direction = "x",
                 unit = "1/1",
                 data_source = '10.1016/j.jhydrol.2011.11.038',
                 country_code = 'IND')
    
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/Jacksonburg-Stringtown_oil_field_US/variogram_permeability_layer_1_x.csv",
                 site_id = 'Jacksonburg_Stringtown_oil_field',
                 var_type = "permeability",
                 direction = "x",
                 unit = "1/1",
                 data_source = '10.1016/j.ijggc.2018.10.011',
                 country_code = 'USA')
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/Jacksonburg-Stringtown_oil_field_US/variogram_permeability_layer_1_y.csv",
                 site_id = 'Jacksonburg_Stringtown_oil_field',
                 var_type = "permeability",
                 direction = "y",
                 unit = "1/1",
                 data_source = '10.1016/j.ijggc.2018.10.011',
                 country_code = 'USA')
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/Jacksonburg-Stringtown_oil_field_US/variogram_permeability_layer_1_z.csv",
                 site_id = 'Jacksonburg_Stringtown_oil_field',
                 var_type = "permeability",
                 direction = "z",
                 unit = "1/1",
                 data_source = '10.1016/j.ijggc.2018.10.011',
                 country_code = 'USA')
    
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/Jianghan_Plain_CHN/variogram_conductivity_x.csv",
                 site_id = 'Jianghan_Plain',
                 var_type = "hydraulic_conductivity",
                 direction = "x",
                 unit = "1/1",
                 data_source = '10.1016/j.jhydrol.2020.125917',
                 country_code = 'CHN')
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/Jianghan_Plain_CHN/variogram_conductivity_y.csv",
                 site_id = 'Jianghan_Plain',
                 var_type = "hydraulic_conductivity",
                 direction = "y",
                 unit = "1/1",
                 data_source = '10.1016/j.jhydrol.2020.125917',
                 country_code = 'CHN')
    
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/Krauthausen_field_GER/variogram_conductivity_x.csv",
                 site_id = 'Krauthausen_field',
                 var_type = "hydraulic_conductivity",
                 direction = "x",
                 unit = "1/1",
                 data_source = '10.1016/S0169-7722(00)00107-8',
                 country_code = 'DEU')
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/Krauthausen_field_GER/variogram_conductivity_z.csv",
                 site_id = 'Krauthausen_field',
                 var_type = "hydraulic_conductivity",
                 direction = "z",
                 unit = "1/1",
                 data_source = '10.1016/S0169-7722(00)00107-8',
                 country_code = 'DEU')
    
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/Kiso_river_JAP/variogram_permeability.csv",
                 site_id = 'Kiso_river',
                 var_type = "permeability",
                 direction = "x",
                 unit = "1/1",
                 data_source = '10.1029/2001WR000672',
                 country_code = 'JPN')
    
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/Lauswiesen_site_GER/variogram_conductivity_layer_1.csv",
                 site_id = 'Lauswiesen_site',
                 var_type = "hydraulic_conductivity",
                 direction = "x",
                 unit = "1/2",
                 data_source = '10.1029/2009WR008949',
                 country_code = 'DEU')
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/Lauswiesen_site_GER/variogram_conductivity_layer_2.csv",
                 site_id = 'Lauswiesen_site',
                 var_type = "hydraulic_conductivity",
                 direction = "x",
                 unit = "2/2",
                 data_source = '10.1029/2009WR008949',
                 country_code = 'DEU')
    
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/Libertador_General_Bernardos_O_Higgins_region_CIL/variogram_conductivity.csv",
                 site_id = 'Libertador_General_Bernardos_O_Higgins_region',
                 var_type = "hydraulic_conductivity",
                 direction = "x",
                 unit = "1/1",
                 data_source = '10.4067/S0718-58392011000200012',
                 country_code = 'CHL')
    
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/LLNL_upper_aquifer_US/variogram_conductivity_x.csv",
                 site_id = 'LLNL_upper_aquifer',
                 var_type = "hydraulic_conductivity",
                 direction = "x",
                 unit = "1/1",
                 data_source = '10.1016/S0309-1708(98)00013-X',
                 country_code = 'USA')
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/LLNL_upper_aquifer_US/variogram_conductivity_y.csv",
                 site_id = 'LLNL_upper_aquifer',
                 var_type = "hydraulic_conductivity",
                 direction = "y",
                 unit = "1/1",
                 data_source = '10.1016/S0309-1708(98)00013-X',
                 country_code = 'USA')
    
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/Lower_Cretaceous_Viking_formation_US/variogram_permeability_x.csv",
                 site_id = 'Lower_Cretaceous_Viking_formation',
                 var_type = "permeability",
                 direction = "x",
                 unit = "1/1",
                 data_source = '10.2118/21520-PA',
                 country_code = 'USA')
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/Lower_Cretaceous_Viking_formation_US/variogram_permeability_z.csv",
                 site_id = 'Lower_Cretaceous_Viking_formation',
                 var_type = "permeability",
                 direction = "z",
                 unit = "1/1",
                 data_source = '10.2118/21520-PA',
                 country_code = 'USA')
    
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/Lower_Triassic_sandstones_Scrabo_quarry_NIR/variogram_permeability_layer_1.csv",
                 site_id = 'Lower_Triassic_sandstones_Scrabo_quarry',
                 var_type = "permeability",
                 direction = "x",
                 unit = "1/8",
                 data_source = '10.1023/B:MATG.0000041178.73284.88',
                 country_code = 'GBR')
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/Lower_Triassic_sandstones_Scrabo_quarry_NIR/variogram_permeability_layer_2.csv",
                 site_id = 'Lower_Triassic_sandstones_Scrabo_quarry',
                 var_type = "permeability",
                 direction = "x",
                 unit = "2/8",
                 data_source = '10.1023/B:MATG.0000041178.73284.88',
                 country_code = 'GBR')
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/Lower_Triassic_sandstones_Scrabo_quarry_NIR/variogram_permeability_layer_3.csv",
                 site_id = 'Lower_Triassic_sandstones_Scrabo_quarry',
                 var_type = "permeability",
                 direction = "x",
                 unit = "3/8",
                 data_source = '10.1023/B:MATG.0000041178.73284.88',
                 country_code = 'GBR')
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/Lower_Triassic_sandstones_Scrabo_quarry_NIR/variogram_permeability_layer_4.csv",
                 site_id = 'Lower_Triassic_sandstones_Scrabo_quarry',
                 var_type = "permeability",
                 direction = "x",
                 unit = "4/8",
                 data_source = '10.1023/B:MATG.0000041178.73284.88',
                 country_code = 'GBR')
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/Lower_Triassic_sandstones_Scrabo_quarry_NIR/variogram_permeability_layer_5.csv",
                 site_id = 'Lower_Triassic_sandstones_Scrabo_quarry',
                 var_type = "permeability",
                 direction = "x",
                 unit = "5/8",
                 data_source = '10.1023/B:MATG.0000041178.73284.88',
                 country_code = 'GBR')
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/Lower_Triassic_sandstones_Scrabo_quarry_NIR/variogram_permeability_layer_6.csv",
                 site_id = 'Lower_Triassic_sandstones_Scrabo_quarry',
                 var_type = "permeability",
                 direction = "x",
                 unit = "6/8",
                 data_source = '10.1023/B:MATG.0000041178.73284.88',
                 country_code = 'GBR')
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/Lower_Triassic_sandstones_Scrabo_quarry_NIR/variogram_permeability_layer_7.csv",
                 site_id = 'Lower_Triassic_sandstones_Scrabo_quarry',
                 var_type = "permeability",
                 direction = "x",
                 unit = "7/8",
                 data_source = '10.1023/B:MATG.0000041178.73284.88',
                 country_code = 'GBR')
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/Lower_Triassic_sandstones_Scrabo_quarry_NIR/variogram_permeability_layer_8.csv",
                 site_id = 'Lower_Triassic_sandstones_Scrabo_quarry',
                 var_type = "permeability",
                 direction = "x",
                 unit = "8/8",
                 data_source = '10.1023/B:MATG.0000041178.73284.88',
                 country_code = 'GBR')
    
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/MADE_site_US/variogram_conductivity_x.csv",
                 site_id = 'MADE_site',
                 var_type = "hydraulic_conductivity",
                 direction = "x",
                 unit = "1/1",
                 data_source = '10.1029/2009WR008966',
                 country_code = 'USA')
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/MADE_site_US/variogram_conductivity_z.csv",
                 site_id = 'MADE_site',
                 var_type = "hydraulic_conductivity",
                 direction = "z",
                 unit = "1/1",
                 data_source = '10.1029/2009WR008966',
                 country_code = 'USA')
    
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/Man-Danane_region_IC/variogram_transmissivity.csv",
                 site_id = 'Man-Danane_region',
                 var_type = "hydraulic_transmissivity",
                 direction = "x",
                 unit = "1/1",
                 data_source = '10.1016/j.jhydrol.2005.10.014',
                 country_code = 'CIV')
    
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/Mirror_Lake_site_US/variogram_indicator_x.csv",
                 site_id = 'Mirror_Lake_site',
                 var_type = "indicator",
                 direction = "x",
                 unit = "1/1",
                 data_source = '10.1029/2000WR900073',
                 country_code = 'USA')
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/Mirror_Lake_site_US/variogram_indicator_z.csv",
                 site_id = 'Mirror_Lake_site',
                 var_type = "indicator",
                 direction = "z",
                 unit = "1/1",
                 data_source = '10.1029/2000WR900073',
                 country_code = 'USA')
    
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/Neogene_aquifer_BEL/variogram_conductivity_x.csv",
                 site_id = 'Neogene_aquifer',
                 var_type = "hydraulic_concuctivity",
                 direction = "x",
                 unit = "1/1",
                 data_source = '10.1002/hyp.10007',
                 country_code = 'BEL')
    
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/Neogene_aquifer_BEL/variogram_conductivity_z.csv",
                 site_id = 'Neogene_aquifer',
                 var_type = "hydraulic_concuctivity",
                 direction = "z",
                 unit = "1/1",
                 data_source = '10.1002/hyp.10007',
                 country_code = 'BEL')
    
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/Nord_Pas_de_Calais_FRA/variogram_transmissivity.csv",
                 site_id = 'Nord_Pas_de_Calais',
                 var_type = "hydraulic_concuctivity",
                 direction = "x",
                 unit = "1/1",
                 data_source = '10.1016/S0022-1694(96)03074-0',
                 country_code = 'FRA')
    
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/North_German_basin_GER/variogram_permeability_layer_1.csv",
                 site_id = 'North_German_basin',
                 var_type = "permeability",
                 direction = "x",
                 unit = "1/4",
                 data_source = '10.1007/s12665-013-2627-1',
                 country_code = 'DEU')
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/North_German_basin_GER/variogram_permeability_layer_2.csv",
                 site_id = 'North_German_basin',
                 var_type = "permeability",
                 direction = "x",
                 unit = "2/4",
                 data_source = '10.1007/s12665-013-2627-1',
                 country_code = 'DEU')
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/North_German_basin_GER/variogram_permeability_layer_3.csv",
                 site_id = 'North_German_basin',
                 var_type = "permeability",
                 direction = "x",
                 unit = "3/4",
                 data_source = '10.1007/s12665-013-2627-1',
                 country_code = 'DEU')
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/North_German_basin_GER/variogram_permeability_layer_4.csv",
                 site_id = 'North_German_basin',
                 var_type = "permeability",
                 direction = "x",
                 unit = "4/4",
                 data_source = '10.1007/s12665-013-2627-1',
                 country_code = 'DEU')
    
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/Northwestern_Sahara_basin_CI_aquifer_ALG/variogram_conductivity.csv",
                 site_id = 'Northwestern_Sahara_basin_CI_aquifer',
                 var_type = "hydraulic_conductivity",
                 direction = "x",
                 unit = "1/1",
                 data_source = '10.1016/j.jafrearsci.2017.02.034',
                 country_code = 'DZA')
    
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/Northwestern_Sahara_basin_CT_aquifer_ALG/variogram_conductivity.csv",
                 site_id = 'Northwestern_Sahara_basin_CT_aquifer',
                 var_type = "hydraulic_conductivity",
                 direction = "x",
                 unit = "1/1",
                 data_source = '10.1016/j.jafrearsci.2017.02.034',
                 country_code = 'DZA')
    
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/Nubian_Sandstone_aquifer_EGY/variogram_transmissivity_x.csv",
                 site_id = 'Nubian_Sandstone_aquifer',
                 var_type = "hydraulic_transmissivity",
                 direction = "x",
                 unit = "1/1",
                 data_source = '10.3390/w12020604',
                 country_code = 'EGY')
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/Nubian_Sandstone_aquifer_EGY/variogram_transmissivity_y.csv",
                 site_id = 'Nubian_Sandstone_aquifer',
                 var_type = "hydraulic_transmissivity",
                 direction = "y",
                 unit = "1/1",
                 data_source = '10.3390/w12020604',
                 country_code = 'EGY')
    
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/Obersulzbach_sandstone_quarry_outcrop_GER/variogram_permeability_layer_1.csv",
                 site_id = 'Obersulzbach_sandstone_quarry_outcrop',
                 var_type = "permeability",
                 direction = "x",
                 unit = "1/2",
                 data_source = '10.3390/ijgi9060409',
                 country_code = 'DEU')
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/Obersulzbach_sandstone_quarry_outcrop_GER/variogram_permeability_layer_2.csv",
                 site_id = 'Obersulzbach_sandstone_quarry_outcrop',
                 var_type = "permeability",
                 direction = "x",
                 unit = "2/2",
                 data_source = '10.3390/ijgi9060409',
                 country_code = 'DEU')
    
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/Oligocene_Huagang_Formation_CHI/variogram_permeability.csv",
                 site_id = 'Oligocene_Huagang_Formation',
                 var_type = "permeability",
                 direction = "x",
                 unit = "1/1",
                 data_source = '10.1016/j.marpetgeo.2019.104044',
                 country_code = 'CHN')
    
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/Pingtung_plain_TAI/variogram_conductivity_layer_1.csv",
                 site_id = 'Pingtung_plain',
                 var_type = "hydraulic_conductivity",
                 direction = "x",
                 unit = "1/3",
                 data_source = '10.3390/w9030164',
                 country_code = 'TWN')
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/Pingtung_plain_TAI/variogram_conductivity_layer_2.csv",
                 site_id = 'Pingtung_plain',
                 var_type = "hydraulic_conductivity",
                 direction = "x",
                 unit = "2/3",
                 data_source = '10.3390/w9030164',
                 country_code = 'TWN')
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/Pingtung_plain_TAI/variogram_conductivity_layer_3.csv",
                 site_id = 'Pingtung_plain',
                 var_type = "hydraulic_conductivity",
                 direction = "x",
                 unit = "3/3",
                 data_source = '10.3390/w9030164',
                 country_code = 'TWN')
    
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/Plain_of_Haouz_MOR/variogram_transmissivity_x.csv",
                 site_id = 'Plain_of_Haouz',
                 var_type = "hydraulic_transmissivity",
                 direction = "x",
                 unit = "1/1",
                 data_source = '10.1111/j.1745-6584.1996.tb01859.x',
                 country_code = 'MAR')
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/Plain_of_Haouz_MOR/variogram_transmissivity_y.csv",
                 site_id = 'Plain_of_Haouz',
                 var_type = "hydraulic_transmissivity",
                 direction = "y",
                 unit = "1/1",
                 data_source = '10.1111/j.1745-6584.1996.tb01859.x',
                 country_code = 'MAR')
    
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/Platte_river_US/variogram_conductivity.csv",
                 site_id = 'Platte_river',
                 var_type = "hydraulic_conductivity",
                 direction = "x",
                 unit = "1/1",
                 data_source = '10.1007/s11269-010-9698-5',
                 country_code = 'USA')
    
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/Prairie_Creek_test_site_US/variogram_conductivity_layer_1.csv",
                 site_id = 'Prairie_Creek_test_site',
                 var_type = "hydraulic_conductivity",
                 direction = "x",
                 unit = "1/3",
                 data_source = '10.1029/2002WR001383',
                 country_code = 'USA')
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/Prairie_Creek_test_site_US/variogram_conductivity_layer_2.csv",
                 site_id = 'Prairie_Creek_test_site',
                 var_type = "hydraulic_conductivity",
                 direction = "x",
                 unit = "2/3",
                 data_source = '10.1029/2002WR001383',
                 country_code = 'USA')
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/Prairie_Creek_test_site_US/variogram_conductivity_layer_3.csv",
                 site_id = 'Prairie_Creek_test_site',
                 var_type = "hydraulic_conductivity",
                 direction = "x",
                 unit = "3/3",
                 data_source = '10.1029/2002WR001383',
                 country_code = 'USA')
    
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/RMA_Superfund_site_US/variogram_conductivity.csv",
                 site_id = 'RMA_Superfund_site',
                 var_type = "hydraulic_conductivity",
                 direction = "x",
                 unit = "1/1",
                 data_source = '10.1089/ees.1999.16.315',
                 country_code = 'USA')
    
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/Sand_box_US/variogram_conductivity.csv",
                 site_id = 'Sand_box_US',
                 var_type = "hydraulic_conductivity",
                 direction = "x",
                 unit = "1/1",
                 data_source = '10.1029/2000WR900096',
                 country_code = 'USA')
    
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/San-Pedro_area_CI/variogram_transmissivity.csv",
                 site_id = 'San_Pedro_area',
                 var_type = "hydraulic_transmissivity",
                 direction = "x",
                 unit = "1/1",
                 data_source = '10.3989/egeol.40672.159',
                 country_code = 'CHL')
    
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/Savannah_River_site_US/variogram_conductivity_layer_1_x.csv",
                 site_id = 'Savannah_River_site',
                 var_type = "hydraulic_conductivity",
                 direction = "x",
                 unit = "1/3",
                 data_source = '10.1007/s00477-011-0459-7',
                 country_code = 'USA')
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/Savannah_River_site_US/variogram_conductivity_layer_1_y.csv",
                 site_id = 'Savannah_River_site',
                 var_type = "hydraulic_conductivity",
                 direction = "y",
                 unit = "1/3",
                 data_source = '10.1007/s00477-011-0459-7',
                 country_code = 'USA')
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/Savannah_River_site_US/variogram_conductivity_layer_1_z.csv",
                 site_id = 'Savannah_River_site',
                 var_type = "hydraulic_conductivity",
                 direction = "z",
                 unit = "1/3",
                 data_source = '10.1007/s00477-011-0459-7',
                 country_code = 'USA')
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/Savannah_River_site_US/variogram_conductivity_layer_2_x.csv",
                 site_id = 'Savannah_River_site',
                 var_type = "hydraulic_conductivity",
                 direction = "x",
                 unit = "2/3",
                 data_source = '10.1007/s00477-011-0459-7',
                 country_code = 'USA')
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/Savannah_River_site_US/variogram_conductivity_layer_2_y.csv",
                 site_id = 'Savannah_River_site',
                 var_type = "hydraulic_conductivity",
                 direction = "y",
                 unit = "2/3",
                 data_source = '10.1007/s00477-011-0459-7',
                 country_code = 'USA')
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/Savannah_River_site_US/variogram_conductivity_layer_2_z.csv",
                 site_id = 'Savannah_River_site',
                 var_type = "hydraulic_conductivity",
                 direction = "z",
                 unit = "2/3",
                 data_source = '10.1007/s00477-011-0459-7',
                 country_code = 'USA')
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/Savannah_River_site_US/variogram_conductivity_layer_3_x.csv",
                 site_id = 'Savannah_River_site',
                 var_type = "hydraulic_conductivity",
                 direction = "x",
                 unit = "3/3",
                 data_source = '10.1007/s00477-011-0459-7',
                 country_code = 'USA')
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/Savannah_River_site_US/variogram_conductivity_layer_3_y.csv",
                 site_id = 'Savannah_River_site',
                 var_type = "hydraulic_conductivity",
                 direction = "y",
                 unit = "3/3",
                 data_source = '10.1007/s00477-011-0459-7',
                 country_code = 'USA')
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/Savannah_River_site_US/variogram_conductivity_layer_3_z.csv",
                 site_id = 'Savannah_River_site',
                 var_type = "hydraulic_conductivity",
                 direction = "z",
                 unit = "3/3",
                 data_source = '10.1007/s00477-011-0459-7',
                 country_code = 'USA')
    
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/Shurijeh-B_reservoir_IRN/variogram_permeability_x.csv",
                 site_id = 'Shurijeh-B_reservoir',
                 var_type = "permeability",
                 direction = "x",
                 unit = "1/1",
                 data_source = '10.1007/s13202-018-0587-4',
                 country_code = 'IRN')
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/Shurijeh-B_reservoir_IRN/variogram_permeability_y.csv",
                 site_id = 'Shurijeh-B_reservoir',
                 var_type = "permeability",
                 direction = "y",
                 unit = "1/1",
                 data_source = '10.1007/s13202-018-0587-4',
                 country_code = 'IRN')
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/Shurijeh-B_reservoir_IRN/variogram_permeability_z.csv",
                 site_id = 'Shurijeh-B_reservoir',
                 var_type = "permeability",
                 direction = "z",
                 unit = "1/1",
                 data_source = '10.1007/s13202-018-0587-4',
                 country_code = 'IRN')
    
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/Sierra_Ladrones_formation_US/variogram_permeability_x.csv",
                 site_id = 'Sierra_Ladrones_formation',
                 var_type = "permeability",
                 direction = "x",
                 unit = "1/1",
                 data_source = '10.1016/j.sedgeo.2005.11.005',
                 country_code = 'USA')
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/Sierra_Ladrones_formation_US/variogram_permeability_z.csv",
                 site_id = 'Sierra_Ladrones_formation',
                 var_type = "permeability",
                 direction = "z",
                 unit = "1/1",
                 data_source = '10.1016/j.sedgeo.2005.11.005',
                 country_code = 'USA')
    
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/Sindhudurg_district_IND/variogram_transmissivity.csv",
                 site_id = 'Sindhudurg_district',
                 var_type = "transmissivity",
                 direction = "x",
                 unit = "1/1",
                 data_source = '10.1007/s00477-016-1317-4',
                 country_code = 'IND')
    
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/Snake_River_aquifer_US/variogram_conductivity_x.csv",
                 site_id = 'Snake_River_aquifer',
                 var_type = "hydraulic_conductivity",
                 direction = "x",
                 unit = "1/1",
                 data_source = '10.1130/0016-7606(1997)109<0855:GAORHC>2.3.CO;2',
                 country_code = 'USA')
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/Snake_River_aquifer_US/variogram_conductivity_y.csv",
                 site_id = 'Snake_River_aquifer',
                 var_type = "hydraulic_conductivity",
                 direction = "y",
                 unit = "1/1",
                 data_source = '10.1130/0016-7606(1997)109<0855:GAORHC>2.3.CO;2',
                 country_code = 'USA')
    
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/South_Jingyang_Plateau_CHI/variogram_conductivity_layer_1.csv",
                 site_id = 'South_Jingyang_Plateau',
                 var_type = "hydraulic_conductivity",
                 direction = "x",
                 unit = "1/2",
                 data_source = '10.1016/j.enggeo.2017.08.002',
                 country_code = 'CHN')
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/South_Jingyang_Plateau_CHI/variogram_conductivity_layer_2.csv",
                 site_id = 'South_Jingyang_Plateau',
                 var_type = "hydraulic_conductivity",
                 direction = "x",
                 unit = "2/2",
                 data_source = '10.1016/j.enggeo.2017.08.002',
                 country_code = 'CHN')
    
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/South_Pars_gas_field_IRN/variogram_permeability.csv",
                 site_id = 'South_Pars_gas_field',
                 var_type = "permeability",
                 direction = "x",
                 unit = "1/1",
                 data_source = '10.2478/s13533-012-0142-7',
                 country_code = 'IRN')
    
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/Southwest_CHI/variogram_conductivity_layer_1.csv",
                 site_id = 'Southwest_China',
                 var_type = "hydraulic_conductivity",
                 direction = "x",
                 unit = "1/12",
                 data_source = '10.1016/j.jhydrol.2018.09.016',
                 country_code = 'CHN')
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/Southwest_CHI/variogram_conductivity_layer_2.csv",
                 site_id = 'Southwest_China',
                 var_type = "hydraulic_conductivity",
                 direction = "x",
                 unit = "2/12",
                 data_source = '10.1016/j.jhydrol.2018.09.016',
                 country_code = 'CHN')
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/Southwest_CHI/variogram_conductivity_layer_3.csv",
                 site_id = 'Southwest_China',
                 var_type = "hydraulic_conductivity",
                 direction = "x",
                 unit = "3/12",
                 data_source = '10.1016/j.jhydrol.2018.09.016',
                 country_code = 'CHN')
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/Southwest_CHI/variogram_conductivity_layer_4.csv",
                 site_id = 'Southwest_China',
                 var_type = "hydraulic_conductivity",
                 direction = "x",
                 unit = "4/12",
                 data_source = '10.1016/j.jhydrol.2018.09.016',
                 country_code = 'CHN')
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/Southwest_CHI/variogram_conductivity_layer_5.csv",
                 site_id = 'Southwest_China',
                 var_type = "hydraulic_conductivity",
                 direction = "x",
                 unit = "5/12",
                 data_source = '10.1016/j.jhydrol.2018.09.016',
                 country_code = 'CHN')
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/Southwest_CHI/variogram_conductivity_layer_6.csv",
                 site_id = 'Southwest_China',
                 var_type = "hydraulic_conductivity",
                 direction = "x",
                 unit = "6/12",
                 data_source = '10.1016/j.jhydrol.2018.09.016',
                 country_code = 'CHN')
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/Southwest_CHI/variogram_conductivity_layer_7.csv",
                 site_id = 'Southwest_China',
                 var_type = "hydraulic_conductivity",
                 direction = "x",
                 unit = "7/12",
                 data_source = '10.1016/j.jhydrol.2018.09.016',
                 country_code = 'CHN')
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/Southwest_CHI/variogram_conductivity_layer_8.csv",
                 site_id = 'Southwest_China',
                 var_type = "hydraulic_conductivity",
                 direction = "x",
                 unit = "8/12",
                 data_source = '10.1016/j.jhydrol.2018.09.016',
                 country_code = 'CHN')
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/Southwest_CHI/variogram_conductivity_layer_9.csv",
                 site_id = 'Southwest_China',
                 var_type = "hydraulic_conductivity",
                 direction = "x",
                 unit = "9/12",
                 data_source = '10.1016/j.jhydrol.2018.09.016',
                 country_code = 'CHN')
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/Southwest_CHI/variogram_conductivity_layer_10.csv",
                 site_id = 'Southwest_China',
                 var_type = "hydraulic_conductivity",
                 direction = "x",
                 unit = "10/12",
                 data_source = '10.1016/j.jhydrol.2018.09.016',
                 country_code = 'CHN')
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/Southwest_CHI/variogram_conductivity_layer_11.csv",
                 site_id = 'Southwest_China',
                 var_type = "hydraulic_conductivity",
                 direction = "x",
                 unit = "11/12",
                 data_source = '10.1016/j.jhydrol.2018.09.016',
                 country_code = 'CHN')
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/Southwest_CHI/variogram_conductivity_layer_12.csv",
                 site_id = 'Southwest_China',
                 var_type = "hydraulic_conductivity",
                 direction = "x",
                 unit = "12/12",
                 data_source = '10.1016/j.jhydrol.2018.09.016',
                 country_code = 'CHN')
    
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/Takelsa_multilayer_aquifer_TUN/variogram_transmissivity.csv",
                 site_id = 'Takelsa_multilayer_aquifer',
                 var_type = "hydraulic_transmissivity",
                 direction = "x",
                 unit = "1/1",
                 data_source = '10.1007/s12665-017-7021-y',
                 country_code = 'TUN')
    
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/Ticino_valley_ITA/variogram_conductivity_layer_1_x.csv",
                 site_id = 'Ticino_valley',
                 var_type = "hydraulic_conductivity",
                 direction = "x",
                 unit = "1/8",
                 data_source = '10.2110/jsr.2006.091',
                 country_code = 'ITA')
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/Ticino_valley_ITA/variogram_conductivity_layer_1_y.csv",
                 site_id = 'Ticino_valley',
                 var_type = "hydraulic_conductivity",
                 direction = "y",
                 unit = "1/8",
                 data_source = '10.2110/jsr.2006.091',
                 country_code = 'ITA')
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/Ticino_valley_ITA/variogram_conductivity_layer_1_z.csv",
                 site_id = 'Ticino_valley',
                 var_type = "hydraulic_conductivity",
                 direction = "z",
                 unit = "1/8",
                 data_source = '10.2110/jsr.2006.091',
                 country_code = 'ITA')
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/Ticino_valley_ITA/variogram_conductivity_layer_2_x.csv",
                 site_id = 'Ticino_valley',
                 var_type = "hydraulic_conductivity",
                 direction = "x",
                 unit = "2/8",
                 data_source = '10.2110/jsr.2006.091',
                 country_code = 'ITA')
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/Ticino_valley_ITA/variogram_conductivity_layer_2_y.csv",
                 site_id = 'Ticino_valley',
                 var_type = "hydraulic_conductivity",
                 direction = "y",
                 unit = "2/8",
                 data_source = '10.2110/jsr.2006.091',
                 country_code = 'ITA')
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/Ticino_valley_ITA/variogram_conductivity_layer_2_z.csv",
                 site_id = 'Ticino_valley',
                 var_type = "hydraulic_conductivity",
                 direction = "z",
                 unit = "2/8",
                 data_source = '10.2110/jsr.2006.091',
                 country_code = 'ITA')
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/Ticino_valley_ITA/variogram_conductivity_layer_3_x.csv",
                 site_id = 'Ticino_valley',
                 var_type = "hydraulic_conductivity",
                 direction = "x",
                 unit = "3/8",
                 data_source = '10.2110/jsr.2006.091',
                 country_code = 'ITA')    
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/Ticino_valley_ITA/variogram_conductivity_layer_3_y.csv",
                 site_id = 'Ticino_valley',
                 var_type = "hydraulic_conductivity",
                 direction = "y",
                 unit = "3/8",
                 data_source = '10.2110/jsr.2006.091',
                 country_code = 'ITA')
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/Ticino_valley_ITA/variogram_conductivity_layer_3_z.csv",
                 site_id = 'Ticino_valley',
                 var_type = "hydraulic_conductivity",
                 direction = "z",
                 unit = "3/8",
                 data_source = '10.2110/jsr.2006.091',
                 country_code = 'ITA')
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/Ticino_valley_ITA/variogram_conductivity_layer_4_x.csv",
                 site_id = 'Ticino_valley',
                 var_type = "hydraulic_conductivity",
                 direction = "x",
                 unit = "4/8",
                 data_source = '10.2110/jsr.2006.091',
                 country_code = 'ITA')
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/Ticino_valley_ITA/variogram_conductivity_layer_4_y.csv",
                 site_id = 'Ticino_valley',
                 var_type = "hydraulic_conductivity",
                 direction = "y",
                 unit = "4/8",
                 data_source = '10.2110/jsr.2006.091',
                 country_code = 'ITA')
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/Ticino_valley_ITA/variogram_conductivity_layer_4_z.csv",
                 site_id = 'Ticino_valley',
                 var_type = "hydraulic_conductivity",
                 direction = "z",
                 unit = "4/8",
                 data_source = '10.2110/jsr.2006.091',
                 country_code = 'ITA')
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/Ticino_valley_ITA/variogram_conductivity_layer_5_x.csv",
                 site_id = 'Ticino_valley',
                 var_type = "hydraulic_conductivity",
                 direction = "x",
                 unit = "5/8",
                 data_source = '10.2110/jsr.2006.091',
                 country_code = 'ITA')
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/Ticino_valley_ITA/variogram_conductivity_layer_5_y.csv",
                 site_id = 'Ticino_valley',
                 var_type = "hydraulic_conductivity",
                 direction = "y",
                 unit = "5/8",
                 data_source = '10.2110/jsr.2006.091',
                 country_code = 'ITA')
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/Ticino_valley_ITA/variogram_conductivity_layer_5_z.csv",
                 site_id = 'Ticino_valley',
                 var_type = "hydraulic_conductivity",
                 direction = "z",
                 unit = "5/8",
                 data_source = '10.2110/jsr.2006.091',
                 country_code = 'ITA')
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/Ticino_valley_ITA/variogram_conductivity_layer_6_x.csv",
                 site_id = 'Ticino_valley',
                 var_type = "hydraulic_conductivity",
                 direction = "x",
                 unit = "6/8",
                 data_source = '10.2110/jsr.2006.091',
                 country_code = 'ITA')
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/Ticino_valley_ITA/variogram_conductivity_layer_6_y.csv",
                 site_id = 'Ticino_valley',
                 var_type = "hydraulic_conductivity",
                 direction = "y",
                 unit = "6/8",
                 data_source = '10.2110/jsr.2006.091',
                 country_code = 'ITA')
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/Ticino_valley_ITA/variogram_conductivity_layer_6_z.csv",
                 site_id = 'Ticino_valley',
                 var_type = "hydraulic_conductivity",
                 direction = "z",
                 unit = "6/8",
                 data_source = '10.2110/jsr.2006.091',
                 country_code = 'ITA')
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/Ticino_valley_ITA/variogram_conductivity_layer_7_x.csv",
                 site_id = 'Ticino_valley',
                 var_type = "hydraulic_conductivity",
                 direction = "x",
                 unit = "7/8",
                 data_source = '10.2110/jsr.2006.091',
                 country_code = 'ITA')    
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/Ticino_valley_ITA/variogram_conductivity_layer_7_y.csv",
                 site_id = 'Ticino_valley',
                 var_type = "hydraulic_conductivity",
                 direction = "y",
                 unit = "7/8",
                 data_source = '10.2110/jsr.2006.091',
                 country_code = 'ITA')
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/Ticino_valley_ITA/variogram_conductivity_layer_7_z.csv",
                 site_id = 'Ticino_valley',
                 var_type = "hydraulic_conductivity",
                 direction = "z",
                 unit = "7/8",
                 data_source = '10.2110/jsr.2006.091',
                 country_code = 'ITA')
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/Ticino_valley_ITA/variogram_conductivity_layer_8_x.csv",
                 site_id = 'Ticino_valley',
                 var_type = "hydraulic_conductivity",
                 direction = "x",
                 unit = "8/8",
                 data_source = '10.2110/jsr.2006.091',
                 country_code = 'ITA')
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/Ticino_valley_ITA/variogram_conductivity_layer_8_y.csv",
                 site_id = 'Ticino_valley',
                 var_type = "hydraulic_conductivity",
                 direction = "y",
                 unit = "8/8",
                 data_source = '10.2110/jsr.2006.091',
                 country_code = 'ITA')
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/Ticino_valley_ITA/variogram_conductivity_layer_8_z.csv",
                 site_id = 'Ticino_valley',
                 var_type = "hydraulic_conductivity",
                 direction = "z",
                 unit = "8/8",
                 data_source = '10.2110/jsr.2006.091',
                 country_code = 'ITA')
    
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/Tono_uranium_deposit_JAP/variogram_conductivity_x.csv",
                 site_id = 'Tono_uranium_deposit',
                 var_type = "hydraulic_conductivity",
                 direction = "x",
                 unit = "1/1",
                 data_source = '10.1016/j.tecto.2015.06.008',
                 country_code = 'JPN')
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/Tono_uranium_deposit_JAP/variogram_conductivity_z.csv",
                 site_id = 'Tono_uranium_deposit',
                 var_type = "hydraulic_conductivity",
                 direction = "z",
                 unit = "1/1",
                 data_source = '10.1016/j.tecto.2015.06.008',
                 country_code = 'JPN')
    
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/Topopah_Spring_tuff_US/variogram_permeability_x.csv",
                 site_id = 'Topopah_Spring_tuff',
                 var_type = "permeability",
                 direction = "x",
                 unit = "1/1",
                 data_source = '10.5194/hess-16-29-2012',
                 country_code = 'USA')
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/Topopah_Spring_tuff_US/variogram_permeability_y.csv",
                 site_id = 'Topopah_Spring_tuff',
                 var_type = "permeability",
                 direction = "y",
                 unit = "1/1",
                 data_source = '10.5194/hess-16-29-2012',
                 country_code = 'USA')
    
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/Triassic_Hawkesbury_sandstone_Sydney_basin_AUS/variogram_permeability_layer_1_x.csv",
                 site_id = 'Triassic_Hawkesbury_sandstone_Sydney_basin',
                 var_type = "permeability",
                 direction = "x",
                 unit = "1/2",
                 data_source = '10.1306/64EDA21C-1724-11D7-8645000102C1865D',
                 country_code = 'AUS')
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/Triassic_Hawkesbury_sandstone_Sydney_basin_AUS/variogram_permeability_layer_1_z.csv",
                 site_id = 'Triassic_Hawkesbury_sandstone_Sydney_basin',
                 var_type = "permeability",
                 direction = "z",
                 unit = "1/2",
                 data_source = '10.1306/64EDA21C-1724-11D7-8645000102C1865D',
                 country_code = 'AUS')
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/Triassic_Hawkesbury_sandstone_Sydney_basin_AUS/variogram_permeability_layer_2_x.csv",
                 site_id = 'Triassic_Hawkesbury_sandstone_Sydney_basin',
                 var_type = "permeability",
                 direction = "x",
                 unit = "2/2",
                 data_source = '10.1306/64EDA21C-1724-11D7-8645000102C1865D',
                 country_code = 'AUS')
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/Triassic_Hawkesbury_sandstone_Sydney_basin_AUS/variogram_permeability_layer_2_z.csv",
                 site_id = 'Triassic_Hawkesbury_sandstone_Sydney_basin',
                 var_type = "permeability",
                 direction = "z",
                 unit = "2/2",
                 data_source = '10.1306/64EDA21C-1724-11D7-8645000102C1865D',
                 country_code = 'AUS')
    
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/Trifa_aquifer_north_zone_MOR/variogram_conductivity.csv",
                 site_id = 'Trifa_aquifer_north_zone',
                 var_type = "hydraulic_conductivity",
                 direction = "x",
                 unit = "1/1",
                 data_source = '10.1007/s10040-007-0166-0',
                 country_code = 'MAR')
    
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/Trifa_aquifer_south_zone_MOR/variogram_conductivity.csv",
                 site_id = 'Trifa_aquifer_south_zone',
                 var_type = "hydraulic_conductivity",
                 direction = "x",
                 unit = "1/1",
                 data_source = '10.1007/s10040-007-0166-0',
                 country_code = 'MAR')
    
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/Tuebingen_site_GER/variogram_conductivity_x.csv",
                 site_id = 'Tuebingen_site',
                 var_type = "hydraulic_conductivity",
                 direction = "x",
                 unit = "1/1",
                 data_source = '10.1007/s10040-011-0706-5',
                 country_code = 'DEU')
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/Tuebingen_site_GER/variogram_conductivity_z.csv",
                 site_id = 'Tuebingen_site',
                 var_type = "hydraulic_conductivity",
                 direction = "z",
                 unit = "1/1",
                 data_source = '10.1007/s10040-011-0706-5',
                 country_code = 'DEU')
    
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/Upper_Awash_basin_ETH/variogram_transmissivity.csv",
                 site_id = 'Upper_Awash_basin',
                 var_type = "hydraulic_transmissivity",
                 direction = "x",
                 unit = "1/1",
                 data_source = '10.1007/s12665-012-2011-6',
                 country_code = 'ETH')
    
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/Upper_Jurassic_Ain_Dar_field_SA/variogram_porosity_x.csv",
                 site_id = 'Upper_Jurassic_Ain_Dar_field',
                 var_type = "porosity",
                 direction = "x",
                 unit = "1/1",
                 data_source = '10.1007/s12517-012-0708-1',
                 country_code = 'SAU')
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/Upper_Jurassic_Ain_Dar_field_SA/variogram_porosity_y.csv",
                 site_id = 'Upper_Jurassic_Ain_Dar_field',
                 var_type = "porosity",
                 direction = "y",
                 unit = "1/1",
                 data_source = '10.1007/s12517-012-0708-1',
                 country_code = 'SAU')
    
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/Upper_Jurassic_Ghawar_field_SA/variogram_porosity_x.csv",
                 site_id = 'Upper_Jurassic_Ghawar_field',
                 var_type = "porosity",
                 direction = "x",
                 unit = "1/1",
                 data_source = '10.1007/s12517-012-0708-1',
                 country_code = 'SAU')
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/Upper_Jurassic_Ghawar_field_SA/variogram_porosity_y.csv",
                 site_id = 'Upper_Jurassic_Ghawar_field',
                 var_type = "porosity",
                 direction = "y",
                 unit = "1/1",
                 data_source = '10.1007/s12517-012-0708-1',
                 country_code = 'SAU')
    
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/Upper_Jurassic_Haradh_field_SA/variogram_porosity_x.csv",
                 site_id = 'Upper_Jurassic_Haradh',
                 var_type = "porosity",
                 direction = "x",
                 unit = "1/1",
                 data_source = '10.1007/s12517-012-0708-1',
                 country_code = 'SAU')
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/Upper_Jurassic_Haradh_field_SA/variogram_porosity_y.csv",
                 site_id = 'Upper_Jurassic_Haradh',
                 var_type = "porosity",
                 direction = "y",
                 unit = "1/1",
                 data_source = '10.1007/s12517-012-0708-1',
                 country_code = 'SAU')
    
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/Upper_Maastrichtian_chalk_outcrops_DEN/variogram_permeability_x.csv",
                 site_id = 'Upper_Maastrichtian_chalk_outcrops',
                 var_type = "permeability",
                 direction = "x",
                 unit = "1/1",
                 data_source = '10.1016/S0264-8172(01)00043-5',
                 country_code = 'DNK')
    
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/Upper_Ulayyah_reservoir_SA/variogram_indicator_layer_1_x.csv",
                 site_id = 'Upper_Ulayyah_reservoir',
                 var_type = "indicator",
                 direction = "x",
                 unit = "1/5",
                 data_source = '10.1016/j.petrol.2019.106664',
                 country_code = 'SAU')
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/Upper_Ulayyah_reservoir_SA/variogram_indicator_layer_1_y.csv",
                 site_id = 'Upper_Ulayyah_reservoir',
                 var_type = "indicator",
                 direction = "y",
                 unit = "1/5",
                 data_source = '10.1016/j.petrol.2019.106664',
                 country_code = 'SAU')
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/Upper_Ulayyah_reservoir_SA/variogram_indicator_layer_1_z.csv",
                 site_id = 'Upper_Ulayyah_reservoir',
                 var_type = "indicator",
                 direction = "z",
                 unit = "1/5",
                 data_source = '10.1016/j.petrol.2019.106664',
                 country_code = 'SAU')
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/Upper_Ulayyah_reservoir_SA/variogram_indicator_layer_2_x.csv",
                 site_id = 'Upper_Ulayyah_reservoir',
                 var_type = "indicator",
                 direction = "x",
                 unit = "2/5",
                 data_source = '10.1016/j.petrol.2019.106664',
                 country_code = 'SAU')
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/Upper_Ulayyah_reservoir_SA/variogram_indicator_layer_2_y.csv",
                 site_id = 'Upper_Ulayyah_reservoir',
                 var_type = "indicator",
                 direction = "y",
                 unit = "2/5",
                 data_source = '10.1016/j.petrol.2019.106664',
                 country_code = 'SAU')
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/Upper_Ulayyah_reservoir_SA/variogram_indicator_layer_2_z.csv",
                 site_id = 'Upper_Ulayyah_reservoir',
                 var_type = "indicator",
                 direction = "z",
                 unit = "2/5",
                 data_source = '10.1016/j.petrol.2019.106664',
                 country_code = 'SAU')
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/Upper_Ulayyah_reservoir_SA/variogram_indicator_layer_3_x.csv",
                 site_id = 'Upper_Ulayyah_reservoir',
                 var_type = "indicator",
                 direction = "x",
                 unit = "3/5",
                 data_source = '10.1016/j.petrol.2019.106664',
                 country_code = 'SAU')
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/Upper_Ulayyah_reservoir_SA/variogram_indicator_layer_3_y.csv",
                 site_id = 'Upper_Ulayyah_reservoir',
                 var_type = "indicator",
                 direction = "y",
                 unit = "3/5",
                 data_source = '10.1016/j.petrol.2019.106664',
                 country_code = 'SAU')
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/Upper_Ulayyah_reservoir_SA/variogram_indicator_layer_3_z.csv",
                 site_id = 'Upper_Ulayyah_reservoir',
                 var_type = "indicator",
                 direction = "z",
                 unit = "3/5",
                 data_source = '10.1016/j.petrol.2019.106664',
                 country_code = 'SAU')
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/Upper_Ulayyah_reservoir_SA/variogram_indicator_layer_4_x.csv",
                 site_id = 'Upper_Ulayyah_reservoir',
                 var_type = "indicator",
                 direction = "x",
                 unit = "4/5",
                 data_source = '10.1016/j.petrol.2019.106664',
                 country_code = 'SAU')
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/Upper_Ulayyah_reservoir_SA/variogram_indicator_layer_4_y.csv",
                 site_id = 'Upper_Ulayyah_reservoir',
                 var_type = "indicator",
                 direction = "y",
                 unit = "4/5",
                 data_source = '10.1016/j.petrol.2019.106664',
                 country_code = 'SAU')
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/Upper_Ulayyah_reservoir_SA/variogram_indicator_layer_4_z.csv",
                 site_id = 'Upper_Ulayyah_reservoir',
                 var_type = "indicator",
                 direction = "z",
                 unit = "4/5",
                 data_source = '10.1016/j.petrol.2019.106664',
                 country_code = 'SAU')
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/Upper_Ulayyah_reservoir_SA/variogram_indicator_layer_5_x.csv",
                 site_id = 'Upper_Ulayyah_reservoir',
                 var_type = "indicator",
                 direction = "x",
                 unit = "5/5",
                 data_source = '10.1016/j.petrol.2019.106664',
                 country_code = 'SAU')
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/Upper_Ulayyah_reservoir_SA/variogram_indicator_layer_5_y.csv",
                 site_id = 'Upper_Ulayyah_reservoir',
                 var_type = "indicator",
                 direction = "y",
                 unit = "5/5",
                 data_source = '10.1016/j.petrol.2019.106664',
                 country_code = 'SAU')
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/Upper_Ulayyah_reservoir_SA/variogram_indicator_layer_5_z.csv",
                 site_id = 'Upper_Ulayyah_reservoir',
                 var_type = "indicator",
                 direction = "z",
                 unit = "5/5",
                 data_source = '10.1016/j.petrol.2019.106664',
                 country_code = 'SAU')
    
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/Vargem_de_Caldas_basin_BRZ/variogram_conductivity_x.csv",
                 site_id = 'Vargem_de_Caldas_basin',
                 var_type = "hydraulic_conductivity",
                 direction = "x",
                 unit = "1/1",
                 data_source = '10.1016/j.envsoft.2013.01.009',
                 country_code = 'BRZ')
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/Vargem_de_Caldas_basin_BRZ/variogram_conductivity_y.csv",
                 site_id = 'Vargem_de_Caldas_basin',
                 var_type = "hydraulic_conductivity",
                 direction = "y",
                 unit = "1/1",
                 data_source = '10.1016/j.envsoft.2013.01.009',
                 country_code = 'BRZ')
    
#    df = fill_df(df, f_path="../data_prep/aquifer_variograms/Vega_de_Granada_aquifer_SPA/variogram_transmisssivity.csv",
#                 site_id = 'Upper_Maastrichtian_chalk_outcrops',
#                 var_type = "hydraulic_transmissvity",
#                 direction = "x",
#                 unit = "1/1",
#                 data_source = '10.1111/j.1745-6584.2008.00494.x',
#                 country_code = 'ESP')
    
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/Waste_Isolation_Pilot_Plant_site_US/variogram_conductivity.csv",
                 site_id = 'Waste_Isolation_Pilot_Plant_site',
                 var_type = "hydraulic_conductivity",
                 direction = "x",
                 unit = "1/1",
                 data_source = '10.1029/1998WR900107',
                 country_code = 'USA')
    
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/West_Bear_Creek_watershed_US/variogram_consuctivity_layer_1.csv",
                 site_id = 'West_Bear_Creek_watershed',
                 var_type = "hydraulic_conductivity",
                 direction = "x",
                 unit = "1/1",
                 data_source = '10.1016/j.jhydrol.2008.06.017',
                 country_code = 'USA')
    
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/Western_Denmark_DEN/variogram_conductivity_layer_1.csv",
                 site_id = 'Western_Denmark',
                 var_type = "hydraulic_conductivity",
                 direction = "x",
                 unit = "1/3",
                 data_source = ' 10.1016/0022-1694(92)90007-I',
                 country_code = 'DNK')
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/Western_Denmark_DEN/variogram_conductivity_layer_2.csv",
                 site_id = 'Western_Denmark',
                 var_type = "hydraulic_conductivity",
                 direction = "x",
                 unit = "2/3",
                 data_source = ' 10.1016/0022-1694(92)90007-I',
                 country_code = 'DNK')
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/Western_Denmark_DEN/variogram_conductivity_layer_3.csv",
                 site_id = 'Western_Denmark',
                 var_type = "hydraulic_conductivity",
                 direction = "x",
                 unit = "3/3",
                 data_source = ' 10.1016/0022-1694(92)90007-I',
                 country_code = 'DNK')
    
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/Yolo_basin_US/variogram_transmissivity.csv",
                 site_id = 'Yolo_basin',
                 var_type = "hydraulic_transmissivity",
                 direction = "x",
                 unit = "1/1",
                 data_source = '10.1007/BF01036238',
                 country_code = 'USA')
    
    df = fill_df(df, f_path="../data_prep/aquifer_variograms/Yucca_Mountain_US/variogram_permeability.csv",
                 site_id = 'Yucca_Mountain',
                 var_type = "permeability",
                 direction = "x",
                 unit = "1/1",
                 data_source = 'OSTI-Identifier:138040',
                 country_code = 'USA')
    
    
    # write data frame to file
    write_df(df)
    