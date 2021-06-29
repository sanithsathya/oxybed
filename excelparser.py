from FLTC import FLTC
import pandas
import json

def parse_excel():
    df = pandas.read_excel("data\FLC.xlsx") 
    list = []
    for index, row in df.iterrows():
        fltc = FLTC(-1, row["District"],row["Area"] ,row["FLC Name"], row["Address"] ,row["Total Normal Beds"],row["Total Oxygen Beds"],row["Occupied Normal Beds"],row["Occupied Oxygen Beds"] )
        list.append(fltc)
    return list
            
def parse_excel_to_json(district=None):
    df = pandas.read_excel("data\FLC.xlsx")
    list = []
    for index, row in df.iterrows():
        fltc1 = FLTC(row["District"],row["Area"] ,row["FLC Name"], row["Address"] ,row["Total Normal Beds"],row["Total Oxygen Beds"],row["Occupied Normal Beds"],row["Occupied Oxygen Beds"] )
        if (district is None or fltc1.district == district):
            list.append(fltc1.__dict__)
    print(list)
    s = json.dumps(list)
    return s
