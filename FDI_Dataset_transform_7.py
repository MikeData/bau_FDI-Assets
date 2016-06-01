# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 14:42:18 2015

@author: Mike
"""

import sys
import transform_lib as tf
import pandas as pd
import py_lookups as lookup

# Combine the files
obs_file1 = pd.read_csv(sys.argv[1])
obs_file2 = pd.read_csv(sys.argv[2])

obs_file = pd.concat([obs_file1, obs_file2])

obs_file = obs_file[obs_file['observation'] != '*********']    
obs_file = obs_file.reset_index()    
        
# Add file footer
count = len(obs_file)
obs_file = obs_file.set_value(len(obs_file), 'observation', '*********')
obs_file = obs_file.set_value(len(obs_file) -1, 'data_marking', count)
obs_file['data_marking'] = obs_file['data_marking'].astype(str)
obs_file['data_marking'] = obs_file['data_marking'].map(lambda x: x.replace('.0', ''))

# Sort out the index
obs_file.fillna('', inplace = True)
obs_file = obs_file.drop('index', 1)

# Sort out type column, for Dataset 7
obs_file['dim_item_id_3'] = obs_file['dim_item_id_3'].astype(str)
obs_file['dim_item_id_3'][obs_file['dim_item_id_3'].map(lambda x: 'investment flows' in x)] = 'Direct investment flows analysed by area, main country and by industrial activity'
obs_file['dim_item_id_3'][obs_file['dim_item_id_3'].map(lambda x: 'investment position' in x)] = 'Investment position analysed by area, main country and by industrial activity'
obs_file['dim_item_id_3'][obs_file['dim_item_id_3'].map(lambda x: 'Earnings' in x)] = 'Earnings from direct investment analysed by area, main country and by industrial activity'


"""
obs_file['dim_item_id_3'] = obs_file['dim_item_id_3'].map(lambda x: x.replace('2.3: Foreign direct investment flows into the United Kingdom analysed by area & main country and by industrial activity of UK affiliates', 'Direct investment flows analysed by area, main country and by industrial activity')).astype(str)
obs_file['dim_item_id_3'] = obs_file['dim_item_id_3'].map(lambda x: x.replace('2.3 Foreign direct investment flows into the United Kingdom analysed by area & main country and by industrial activity of UK affiliates', 'Direct investment flows analysed by area, main country and by industrial activity')).astype(str)
obs_file['dim_item_id_3'] = obs_file['dim_item_id_3'].map(lambda x: x.replace('3.3: FDI international investment position in the United Kingdom analysed by area & main country and by industrial activity of UK affiliates', 'Investment position analysed by area, main country and by industrial activity')).astype(str)
obs_file['dim_item_id_3'] = obs_file['dim_item_id_3'].map(lambda x: x.replace('3.3 FDI international investment position in the United Kingdom analysed by area & main country and by industrial activity of UK affiliates', 'Investment position analysed by area, main country and by industrial activity')).astype(str)
obs_file['dim_item_id_3'] = obs_file['dim_item_id_3'].map(lambda x: x.replace('4.3 Earnings from foreign direct investment in the United Kingdom analysed by area & main country and by industrial activity of UK affiliates', 'Earnings from direct investment analysed by area, main country and by industrial activity')).astype(str)
obs_file['dim_item_id_3'] = obs_file['dim_item_id_3'].map(lambda x: x.replace('4.3: Earnings from foreign direct investment in the United Kingdom analysed by area & main country and by industrial activity of UK affiliates', 'Earnings from direct investment analysed by area, main country and by industrial activity')).astype(str)
obs_file['dim_item_id_3'] = obs_file['dim_item_id_3'].map(lambda x: x.replace('2.3 Foreign direct investment flows abroad analysed by area & main country and by industrial activity of foreign affiliates', 'Direct investment flows analysed by area, main country and by industrial activity')).astype(str)
obs_file['dim_item_id_3'] = obs_file['dim_item_id_3'].map(lambda x: x.replace('2.3: Foreign direct investment flows abroad analysed by area & main country and by industrial activity of foreign affiliates', 'Direct investment flows analysed by area, main country and by industrial activity')).astype(str)
obs_file['dim_item_id_3'] = obs_file['dim_item_id_3'].map(lambda x: x.replace('3.3 FDI international investment position abroad analysed by area & main country and by industrial activity of foreign affiliates', 'Investment position analysed by area, main country and by industrial activity')).astype(str)
obs_file['dim_item_id_3'] = obs_file['dim_item_id_3'].map(lambda x: x.replace('3.3: FDI international investment position abroad analysed by area & main country and by industrial activity of foreign affiliates', 'Investment position analysed by area, main country and by industrial activity')).astype(str)
obs_file['dim_item_id_3'] = obs_file['dim_item_id_3'].map(lambda x: x.replace('4.3 Earnings from foreign direct investment abroad analysed by area & main country and by industrial activity of overseas affiliates', 'Earnings from direct investment analysed by area, main country and by industrial activity')).astype(str)
obs_file['dim_item_id_3'] = obs_file['dim_item_id_3'].map(lambda x: x.replace('4.3: Earnings from foreign direct investment abroad analysed by area & main country and by industrial activity of overseas affiliates', 'Earnings from direct investment analysed by area, main country and by industrial activity')).astype(str)
"""

# Sort out type column for Dataset 8
obs_file['dim_item_id_3'] = obs_file['dim_item_id_3'].map(lambda x: x.replace('Direct investment flows analysed by area, main country and by industrial activity, 2012 to 2013 (Asset/Liability)', 'Direct investment flows analysed by area, main country and by industrial activity')).astype(str)
obs_file['dim_item_id_3'] = obs_file['dim_item_id_3'].map(lambda x: x.replace('Investment position analysed by area, main country and by industrial activity1, 2012 to 2013 (Asset/Liability)', 'Investment position analysed by area, main country and by industrial activity')).astype(str)
obs_file['dim_item_id_3'] = obs_file['dim_item_id_3'].map(lambda x: x.replace('Earnings from direct investment analysed by area, main country and by industrial activity, 2012 to 2013 (Asset/Liability)', 'Earnings from direct investment analysed by area, main country and by industrial activity')).astype(str)
obs_file['dimension_item_label_eng_3'] = obs_file['dim_item_id_3']

# Clean up and concatenate the Location fields                                                                 
obs_file['dim_item_id_4'] = obs_file['dim_item_id_4'].map(str.strip) + ' ' + obs_file['dim_item_id_5'].map(str.strip) + ' ' + obs_file['dim_item_id_6'].map(str.strip)
obs_file['dimension_item_label_eng_4'] = obs_file['dim_item_id_4']

# Manually fix mismatches from the locations closest-above scipr (i.e Europe in USA etc)
obs_file['dim_item_id_4'] = obs_file['dim_item_id_4'].map(lambda x: x.replace('OTHER EUROPEAN', 'OTHER EUROPEAN COUNTRIES')).astype(str)
obs_file['dim_item_id_4'] = obs_file['dim_item_id_4'].map(lambda x: x.replace('NEAR & MIDDLE EAST', 'NEAR & MIDDLE EAST COUNTRIES')).astype(str)
obs_file['dim_item_id_4'] = obs_file['dim_item_id_4'].map(lambda x: x.replace('OTHER ASIAN', 'OTHER ASIAN COUNTRIES')).astype(str)
obs_file['dim_item_id_4'] = obs_file['dim_item_id_4'].map(lambda x: x.replace('AUSTRALASIA & ', 'AUSTRALASIA & OCEANIA')).astype(str)
obs_file['dim_item_id_4'] = obs_file['dim_item_id_4'].map(lambda x: x.replace('CENTRAL & EASTERN', 'CENTRAL & EASTERN EUROPE')).astype(str)
obs_file['dim_item_id_4'] = obs_file['dim_item_id_4'].map(lambda x: x.replace('GULF', 'GULF ARABIAN COUNTRIES')).astype(str)
obs_file['dimension_item_label_eng_4'] = obs_file['dim_item_id_4']

# Get rid of any no lookup errorsi
obs_file = tf.remove_from_columns(obs_file, ['dim_item_id_4'], ['NoLookupError', 'of which '])
obs_file['dim_item_id_4'] = obs_file['dim_item_id_4'].map(str.strip)
obs_file['dimension_item_label_eng_4'] = obs_file['dim_item_id_4']

# Make Category Generic
obs_file = lookup.cat_lookup(obs_file, "dim_item_id_1")
obs_file['dimension_item_label_eng_1'] = obs_file['dim_item_id_1']

# Strip trialing 0 from time
obs_file['time_dim_item_id'] = obs_file['time_dim_item_id'].astype(str)
obs_file['time_dim_item_label_eng'] = obs_file['time_dim_item_label_eng'].astype(str)

obs_file['time_dim_item_id'] = obs_file['time_dim_item_id'].map(lambda x: x.replace('.0', '')).astype(str)
obs_file['time_dim_item_label_eng'] = obs_file['time_dim_item_label_eng'].map(lambda x: x.replace('.0', '')).astype(str)

# Remove the dimensions we dont need anymore: args = (dataframe, [dimensons to drop])
obs_file = tf.dismiss(obs_file, ['dim_id_5', 'dim_id_6'])
obs_file.fillna('', inplace = True)

obs_file.to_csv(sys.argv[3] + '.csv', index=False)
