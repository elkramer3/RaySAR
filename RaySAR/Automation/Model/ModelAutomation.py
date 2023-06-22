import pandas as pd
import math
import numpy as np
import os

def read_Geo(filename):
    # Reads overpass geometry file and saves geometry
    # Input - overpass geometry filename
    # Output - Pandas dataframe of overpass geometry

    data = pd.read_csv(filename)
    data.columns = ['x','y','z']

    #print(data['el'][0])
        
    return data

def gen_header_footer_POV(geo):
    # Creates text log file in POV-Ray format for corresponding overpass geometry
    # Input - Overpass geometry of current time step
    # Output - text for POV-Ray script file

    POV_Model_filename = '/home/ekramer3/Documents/RaySAR/RaySAR/Testfile/Box_Automation/Box_Automation.pov'
    fin = open(POV_Model_filename, "r") # Open POV file
    POVstr = fin.read() # Read POV file
    fin.close() # Close POV file

    # headtext = [] # Initialisation: Line to save in header of POV file
    endtext = [] # Initialisation: Line to save in end part of POV file
    
    fout = open(POV_Model_filename, "w") # Open POV file

    pt = '#include "colors.inc"\n#include "finish.inc"\n\n'
    headtext = pt

    # Contribution file should be created
    pt = 'global_settings {SAR_Output_Data 1 SAR_Intersection 0}\n\n'
    headtext = headtext + pt

    # Dummy distance in horizontal plane for calculating sensor position
    D = 10 # [m]
    scale_geo = (geo / np.sqrt(geo[0]**2 + geo[1]**2 + geo[2]**2)) * D

    # Look at (Position where the sensor is looking at in POV coordinate system):
    x_la = 0 # [m]
    y_la = 0 # [m]
    z_la = 0 # [m]

    # Sensor location (Position of signal source in POV coordinate system)
    x_lo = scale_geo[0] # in [m]
    y_lo = scale_geo[1] # in [m]
    z_lo = scale_geo[2] # in [m]

    right = 25 # horizontal size of view
    up = 25 # vertical size of view

    # Sensor information
    pt = '#declare Cam = camera {\n  orthographic\n'
    headtext = headtext + pt
    # Position where the sensor is looking at
    pt = '  look_at <' + str(x_la) + ',' + str(y_la) + ',' + str(z_la) + '>\n'
    headtext = headtext + pt
    # Sensor location (Position of signal source)
    pt = '  location <' + str(x_lo) + ',' + str(y_lo) + ',' + str(z_lo) + '>\n'
    headtext = headtext + pt
    pt = '  right ' + str(right) + ' *x\n'
    headtext = headtext + pt
    pt = '  up ' + str(up) + ' *y\n'
    headtext = headtext + pt
    pt = '}\n\ncamera{Cam}\n\n'
    headtext = headtext + pt

    # Light source
    pt = 'light_source {\n'
    headtext = headtext + pt
    pt = '  0*x\n'
    headtext = headtext + pt
    # Color of light source: white
    pt = '  color rgb <1,1,1>\n'
    headtext = headtext + pt
    # Type of light source
    pt = '  parallel\n'
    headtext = headtext + pt
    # <x y z> position of light
    pt = '  translate <' + str(x_lo) + ',' + str(y_lo) + ',' + str(z_lo) + '>\n'
    headtext = headtext + pt
    # Direction of spotlight
    pt = '  point_at <' + str(x_la) + ',' + str(y_la) + ',' + str(z_la) + '>\n}\n\n'
    headtext = headtext + pt

    fout.write("".join(headtext) + POVstr)

    fout.close()

    # # Size of the simulated SAR image: Number of rows of simulated SAR image
    # PS_rows = 5 # Spatial resolution along rows (in UTM north direction Y) of SAR image in [m]
    # PS_columns = 5 # Spatial resolution along columns (in UTM east direction X) of SAR image in [m]
    # up = 500 # up: Height of image plane of simulated SAR image in [m] --> Along range image axis
    # right = 500 # right: Width of image plane of simulated SAR image in [m] --> Along azimuth image axis
    # rows_simu = round(up / PS_rows)
    # # Number of columns of simulated SAR image and optical image
    # columns_simu = round(right / PS_columns)
    return '/home/ekramer3/Documents/RaySAR/RaySAR/Testfile/Box_Automation/', 'Box_Automation.pov'

def run_POVRay(POVFilePath,POVFileName):
    # SAR case: Run POV-Ray to render optical image based on POV file and to generate
    # signal contribution file based on POV file
    
    """
    Input:
    aPovfile: Name of POV file
    columns_simu: Number of columns of simulated image
    rows_simu: Number of rows of simulated image
    sensor: Name of sensor
    det: Definition of input parameters (Look at class 'InputPara' in
    'Script.py')
    Output:
    SAR case: Rendered optical image and contribution file which contains
    signal contributions with coordinates and signal strengths and is
    necessary for Rendering of SAR image in RaySAR
    Optical case: Rendered optical image
    Used function:
    None
    Used in function:
    'GeoRayImg.Model2GeoI'
    """

    # Navigate to model file directory
    cmd = 'cd ' + POVFilePath + '; ' + 'povray ' + POVFileName
    os.system(cmd)
    return