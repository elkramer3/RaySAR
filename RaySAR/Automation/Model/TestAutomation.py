import ModelAutomation as ma
filename = '/home/ekramer3/Documents/RaySAR/RaySAR/Automation/Overpass geometries/TestGeometry.csv'
geo_data = ma.read_Geo(filename)
num_pts = len(geo_data.index)
print(num_pts)

num_pts = 1
for i in range(num_pts):
    geo = [geo_data.iloc[i][0],geo_data.iloc[i][1]]
    ma.gen_header_footer_POV(geo)
