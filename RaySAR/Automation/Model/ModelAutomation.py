import pandas as pd
def read_Geo(filename):
    # Reads overpass geometry file and saves geometry
    # Input - overpass geometry filename
    # Output - Pandas dataframe of overpass geometry

    data = pd.read_csv(filename)
    data.columns = ['az','el']

    print(data['el'][0])
        
    return

