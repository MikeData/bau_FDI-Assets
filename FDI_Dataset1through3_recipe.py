# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 13:55:41 2015

@author: Mike
"""

from __future__ import unicode_literals
from ONSdatabaker.constants import *

def per_file(tabs):    
    return [PARAMS(0)]
    
def per_tab(tab):
    
    anchor = tab.excel_ref(PARAMS(3))
    obs = anchor.fill(DOWN).expand(RIGHT).is_not_blank()
    unwanted = tab.filter(contains_string ('Source: Office'))
    unwanted = unwanted | tab.filter(contains_string ('The largest change between methods is a shift '))
    unwanted = unwanted | tab.excel_ref('O1').expand(DOWN).expand(RIGHT)
    obs = obs-unwanted

    anchor.shift(LEFT).expand(DOWN).is_not_blank().dimension(TIME, DIRECTLY, LEFT)

    anchor.expand(RIGHT).parent().is_not_blank().dimension("Investment", DIRECTLY, ABOVE)
    
    first_header= anchor.shift(UP).expand(RIGHT).parent().is_not_blank()
    first_header | tab.filter('£ million').shift(DOWN)    
    first_header.dimension("Investment first", CLOSEST, LEFT) 
    
    unwanted = tab.excel_ref('D').is_not_blank().filter('2011.0').fill(LEFT)
    unwanted = unwanted | tab.excel_ref('D').is_not_blank().filter('2012.0').fill(LEFT)
    unwanted = unwanted | tab.excel_ref('D').is_not_blank().filter('2013.0').fill(LEFT)

    # Get first and second part of location
    find = tab.excel_ref('A').is_not_blank()
    find = find - unwanted
    # find = find | find.shift(1, 1)
    find.dimension("Area", CLOSEST, ABOVE)
    
    find = tab.excel_ref('B').is_not_blank()
    find = find - unwanted
    find = find | tab.excel_ref('A1').fill(DOWN).is_bold().shift(RIGHT)
    find.dimension("Area 1", CLOSEST, ABOVE)    
    
    find = tab.excel_ref('C').is_not_blank()
    find = find - unwanted
    find = find | tab.excel_ref('A1').fill(DOWN).is_bold().shift(2, 0)
    find.dimension("Area 2", CLOSEST, ABOVE)
    
    yield obs
    

    
