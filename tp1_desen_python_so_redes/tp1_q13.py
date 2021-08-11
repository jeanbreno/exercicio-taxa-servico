# -*- coding: utf-8 -*-
"""
Created on Sun Aug  8 21:47:12 2021

@author: 009671631
"""

import subprocess
p_id = subprocess.Popen("notepad")
print("PID do processo criado:", p_id.pid)