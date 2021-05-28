'''
A script to coordinate the generation of QC reports for the TSHC and TMSP panels at the WMRGL.

'''

import os
import pandas as pd
import argparse
import sys
import re
import numpy as np
import glob
import enum

class GenerateQCReport:
    def __init__(self):
        # Assign panel TSHC/TSMP


    @staticmethod
    def assign_panel(ws_1, ws_2, sample_sheet):
        '''
        Assiging a panel and <panel>_main funtion to process pipeline output.
        '''
        panel = re.search(panel_regex, ws_1).group(1)

        if panel == 'TSHC':
            tshc_main(ws_1, ws_2)
        elif panel == 'TSMP' or panel == 'CLL':
            ho_main(panel, ws_1, sample_sheet)
        else:
            raise Exception('Error: Panel specified not recognised.')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-ws_1', action='store', required=True, help='Path to worksheet 1 output files include TSHC_<ws>_version dir')
    parser.add_argument('-ws_2', action='store', help='Path to worksheet 2 output files include TSHC_<ws>_version dir')
    parser.add_argument('-out_dir', action='store', help='Specifing an output directory to store html reports')
    parser.add_argument('-s', action='store', help='SampleSheet requrired for HO panel quality checks')
    args = parser.parse_args()

