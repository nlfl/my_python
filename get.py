# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import os

i=1
for i in range(16,126):
    url="http://dl.fullcirclemagazine.org/issue"+str(i)+"_en.pdf"
    print url
    cmd1="wget -c "  + url
    print cmd1
    os.system( cmd1)
    
    