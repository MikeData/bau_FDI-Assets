# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 13:55:41 2015

@author: Mike
"""

from __future__ import unicode_literals
from ONSdatabaker.constants import *

def per_file(tabs):    
    return ["Table 1.1", "1.2", "1.3"]
    
def per_tab(tab):
    
    anchor = tab.excel_ref('B4')
    
    obs = anchor.fill(DOWN).expand(RIGHT).is_not_blank().is_not_whitespace() - tab.filter(contains_string('Source: Office for National Statistics'))

    # Time
    anchor.expand(RIGHT).is_not_blank().is_not_whitespace().dimension(TIME,  DIRECTLY, ABOVE)

    # Investment
    if tab.name == '1.1':
        anchor.shift(LEFT).expand(DOWN).is_not_blank().is_not_whitespace().dimension('Flows by component', DIRECTLY, LEFT)
    if tab.name == '1.2':
        anchor.shift(LEFT).expand(DOWN).is_not_blank().is_not_whitespace().dimension('Investment position', DIRECTLY, LEFT)    
    if tab.name == '1.3':
        anchor.shift(LEFT).expand(DOWN).is_not_blank().is_not_whitespace().dimension('Earnings by component', DIRECTLY, LEFT)        

    # Use a dimension to keep track of whether its an inwards or outwards flow
    tab.dimension('DeleteMElater', PARAMS(0))

    yield obs
    
    

    
