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

# Clean up and concatenate the Location fields                                                                 
obs_file['dim_item_id_3'] = obs_file['dim_item_id_3'].map(str.strip) + ' ' + obs_file['dim_item_id_4'].map(str.strip) + ' ' + obs_file['dim_item_id_5'].map(str.strip)
obs_file['dimension_item_label_eng_3'] = obs_file['dim_item_id_3']

# Clean up and concatenate the Investment fields                                                                 
obs_file['dim_item_id_1'] = obs_file['dim_item_id_2'].map(str.strip) + ' - ' + obs_file['dim_item_id_1'].map(str.strip)
obs_file['dimension_item_label_eng_1'] = obs_file['dim_item_id_1']

# Manually fix mismatches from the locations closest-above scipr (i.e Europe in USA etc)
obs_file['dim_item_id_3'] = obs_file['dim_item_id_3'].map(lambda x: x.replace('OTHER EUROPEAN', 'OTHER EUROPEAN COUNTRIES')).astype(str)
obs_file['dim_item_id_3'] = obs_file['dim_item_id_3'].map(lambda x: x.replace('NEAR & MIDDLE EAST', 'NEAR & MIDDLE EAST COUNTRIES')).astype(str)
obs_file['dim_item_id_3'] = obs_file['dim_item_id_3'].map(lambda x: x.replace('OTHER ASIAN', 'OTHER ASIAN COUNTRIES')).astype(str)
obs_file['dim_item_id_3'] = obs_file['dim_item_id_3'].map(lambda x: x.replace('AUSTRALASIA & ', 'AUSTRALASIA & OCEANIA')).astype(str)
obs_file['dim_item_id_3'] = obs_file['dim_item_id_3'].map(lambda x: x.replace('CENTRAL & EASTERN', 'CENTRAL & EASTERN EUROPE')).astype(str)
obs_file['dimension_item_label_eng_3'] = obs_file['dim_item_id_3']

# Get rid of any no lookup errorsi
obs_file = tf.remove_from_columns(obs_file, ['dim_item_id_3'], ['NoLookupError', 'of which '])
obs_file['dim_item_id_3'] = obs_file['dim_item_id_3'].map(str.strip)
obs_file['dimension_item_label_eng_3'] = obs_file['dim_item_id_3']

# Strip trialing 0 from time
obs_file['time_dim_item_id'] = obs_file['time_dim_item_id'].astype(str)
obs_file['time_dim_item_label_eng'] = obs_file['time_dim_item_label_eng'].astype(str)
obs_file['time_dim_item_id'] = obs_file['time_dim_item_id'].map(lambda x: x.replace('.0', '')).astype(str)
obs_file['time_dim_item_label_eng'] = obs_file['time_dim_item_label_eng'].map(lambda x: x.replace('.0', '')).astype(str)

# Remove the dimensions we dont need anymore: args = (dataframe, [dimensons to drop])
obs_file = tf.dismiss(obs_file, ['dim_id_2', 'dim_id_4', 'dim_id_5'])
obs_file.fillna('', inplace = True)

# Repair gap in dimension numbering
obs_file = tf.validateheaders(obs_file)

obs_file.to_csv(sys.argv[3] + '.csv', index=False)
