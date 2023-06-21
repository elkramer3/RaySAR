import pandas as pd
import math

def read_Geo(filename):
    # Reads overpass geometry file and saves geometry
    # Input - overpass geometry filename
    # Output - Pandas dataframe of overpass geometry

    data = pd.read_csv(filename)
    data.columns = ['az','el']

    #print(data['el'][0])
        
    return data

def gen_header_footer_POV(geo):
    # Creates text log file in POV-Ray format for corresponding overpass geometry
    # Input - Overpass geometry of current time step
    # Output - text for POV-Ray script file

    headtext = [] # Initialisation: Line to save in header of POV file
    endtext = [] # Initialisation: Line to save in end part of POV file
        
    # Dummy distance in horizontal plane for calculating sensor position
    D = 1 # [m]

    # Look at (Position where the sensor is looking at in POV coordinate system):
    # Position of model center (center of model box)
    x_la = 0 # [m]
    y_la = 0 # [m]
    z_la = 0 # [m]
    # Sensor location (Position of signal source in POV coordinate system)
    # --> Sensor location and Look at have the same POV right coordinate x and
    # only differ in POV up coordinate y and POV depth coordinate z
    x_lo = x_la # in [m]
    y_lo = y_la + D / math.tan(geo[1] / 180 * math.pi) # in [m]
    z_lo = z_la + D # in [m]

    # Size of the simulated SAR image: Number of rows of simulated SAR image
    PS_rows = 5 # Spatial resolution along rows (in UTM north direction Y) of SAR image in [m]
    PS_columns = 5 # Spatial resolution along columns (in UTM east direction X) of SAR image in [m]
    up = 500 # up: Height of image plane of simulated SAR image in [m] --> Along range image axis
    right = 500 # right: Width of image plane of simulated SAR image in [m] --> Along azimuth image axis
    rows_simu = round(up / PS_rows)
    # Number of columns of simulated SAR image and optical image
    columns_simu = round(right / PS_columns)

    pt = '#include "colors.inc"\n#include "finish.inc"\n\n// File produced by AccuTrans 3D\n\n#version 3.5;\n'
    # pts(pt, headtext) # Save print output in log file


    POV_Model_filename = '/home/ekramer3/Documents/RaySAR/RaySAR/Automation/Model/TestPOVFile.pov'
    fin = open(POV_Model_filename, "r") # Open POV file
    print(POV_Model_filename)
    POVstr = fin.read() # Read POV file
    print(POVstr)
    fin.close() # Close POV file
    
    fout = open(POV_Model_filename, "w") # Open POV file
    fout.write("".join(pt) + POVstr + "\n\n")
    fout.close()

    # # SAR image
    # if det.ImgOption == 1:
    # # Contribution file should be created
    # pt = "global_settings {max_trace_level %s SAR_Output_Data 1 SAR_Intersection 0}\n" % det.max_bounce
    # pts(pt, headtext) # Save print output in log file
    # # Optical image
    # else: # det.ImgOption == 2:
    # # Contribution file should not be created
    # pt = "global_settings {max_trace_level %s SAR_Output_Data 0 SAR_Intersection 0}\n" % det.max_bounce
    # pts(pt, headtext) # Save print output in log file

    # # Sensor information
    # pt = "#declare Cam = camera {"
    # pts(pt, headtext) # Save print output in log file
    # # Type of sensor
    # pt = "orthographic"
    # pts(pt, headtext) # Save print output in log file
    # # Position where the sensor is looking at
    # pt = "look_at <" + str(x_la) + "," + str(y_la) + "," + str(z_la) + ">"
    # pts(pt, headtext) # Save print output in log file

    # # Sensor location (Position of signal source)
    # pt = "location <" + str(x_lo) + "," + str(y_lo) + "," + str(z_lo) + ">"
    # pts(pt, headtext) # Save print output in log file
    # pt = "right " + str(right) + ' *x'
    # pts(pt, headtext) # Save print output in log file
    # pt = "up " + str(up) + ' *y'
    # pts(pt, headtext) # Save print output in log file
    # pt = "}\n\ncamera{Cam}\n"
    # pts(pt, headtext) # Save print output in log file

    # # Light source
    # pt = "light_source {"
    # pts(pt, headtext) # Save print output in log file
    # pt = "0*x"
    # pts(pt, headtext) # Save print output in log file
    # # Color of light source: white
    # pt = "color rgb <1,1,1>"
    # pts(pt, headtext) # Save print output in log file
    # # Type of light source
    # pt = "parallel"
    # pts(pt, headtext) # Save print output in log file

    # # SAR image
    # # Light source is at the same position as the sensor (signal source) --> Sun
    # position = sensor position
    # if det.ImgOption == 1:
    # # Translate light source to position of sensor (signal source)
    # pt = "translate <" + str(x_lo) + "," + \
    # str(y_lo) + "," + str(z_lo) + ">"
    # pts(pt, headtext) # Save print output in log file

    # # Light source point at the position of model center (center of model box)
    # pt = "point_at <" + str(x_la) + "," + str(y_la) + "," + str(z_la) + ">"
    # pts(pt, headtext) # Save print output in log file
    # pt = "}\n"
    # pts(pt, headtext) # Save print output in log file
    return 