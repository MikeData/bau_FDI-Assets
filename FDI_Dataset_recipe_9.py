# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 13:55:41 2015

@author: Mike
"""

from __future__ import unicode_literals
from ONSdatabaker.constants import *

def per_file(tabs):    
    return ["2.1", "3.1", "4.1"]
    
def per_tab(tab):
    
    anchor = tab.excel_ref('D8')
    
    obs = anchor.expand(DOWN).expand(RIGHT).is_not_blank().is_not_whitespace()
    unwanted = tab.filter(contains_string ('Source: Office')) | tab.excel_ref('A10').expand(DOWN).filter(contains_string ('1')).expand(RIGHT).expand(DOWN)
    obs = obs-unwanted

    anchor.shift(0,-3).expand(RIGHT).is_not_blank().dimension(TIME, DIRECTLY, ABOVE)
    
    tab.dimension(PARAMS(0), PARAMS(1))    
    
    tab.excel_ref('A2').dimension('Type', CLOSEST, ABOVE)    
    
    unwanted = tab.excel_ref('E').is_not_blank().filter('2013.0').fill(LEFT)
    unwanted = unwanted | tab.excel_ref('D').is_not_blank().filter('2013.0').fill(LEFT)

    # Get first and second part of location
    find = tab.excel_ref('A').is_not_blank().is_not_whitespace()
    find = find - unwanted
    # find = find | find.shift(1, 1)
    find.dimension("Area", CLOSEST, ABOVE)
    
    find = tab.excel_ref('B').is_not_blank().is_not_whitespace()
    find = find - unwanted
    find = find | tab.excel_ref('A1').fill(DOWN).is_not_blank().shift(RIGHT)
    find.dimension("Area 1", CLOSEST, ABOVE)    
    
    find = tab.excel_ref('C').is_not_blank().is_not_whitespace()
    find = find - unwanted
    find = find | tab.excel_ref('A1').fill(DOWN).is_not_blank().shift(2, 0)
    find.dimension("Area 2", CLOSEST, ABOVE) 
    
    yield obs
    
    

    
