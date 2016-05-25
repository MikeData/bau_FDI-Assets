# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 14:42:18 2015

@author: Mike
"""

import pandas as pd
import sys
import transform_lib as tf

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
obs_file['data_marking'] = obs_file['data_marking'].map(lambda x: x.replace('nan', ''))

# Strip trialing 0 from time
obs_file['time_dim_item_id'] = obs_file['time_dim_item_id'].astype(str)
obs_file['time_dim_item_label_eng'] = obs_file['time_dim_item_label_eng'].astype(str)
obs_file['time_dim_item_id'] = obs_file['time_dim_item_id'].map(lambda x: x.replace('.0', ''))
obs_file['time_dim_item_label_eng'] = obs_file['time_dim_item_label_eng'].map(lambda x: x.replace('.0', ''))

# Add the outward/inward tag then get rid of dim 2
obs_file['dim_item_id_1'] = obs_file['dim_item_id_1'].astype(str)
obs_file['dim_item_id_2'] = obs_file['dim_item_id_2'].astype(str)
obs_file['dim_item_id_1'] = obs_file['dim_item_id_1'] + " (" + obs_file['dim_item_id_2'] + ")"
obs_file = tf.dismiss(obs_file, ['dim_id_2'])
 
# Sort out the index
obs_file.fillna('', inplace = True)
obs_file = obs_file.drop('index', 1)

# clean nan values
obs_file.fillna('', inplace=True)

# Clean the whitesapceout of dimension 1
obs_file['dim_item_id_1'] = obs_file['dim_item_id_1'].map(str).map(lambda x: x.strip())
obs_file['dimension_item_label_eng_1'] = obs_file['dim_item_id_1']

# Sort the time
obs_file = obs_file.sort(['dim_id_1', 'time_dim_item_id'], ascending=False)

obs_file.to_csv(sys.argv[3], index=False)