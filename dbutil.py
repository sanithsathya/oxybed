import json
from FLTC import FLTC
from excelparser import parse_excel
import sqlite3

# to be called once while setting up the environment
def initialise_db():
    con = sqlite3.connect('data/flc.db')
    cur = con.cursor()
    cur.execute('''drop table if exists FLC''')
    cur.execute('''create table if not exists FLC
               (id INTEGER PRIMARY KEY AUTOINCREMENT,
               name TEXT NOT NULL, 
               area TEXT, 
               district TEXT NOT NULL, 
               address TEXT, 
               total_normal_bed INTEGER, 
               total_oxygen_bed INTEGER, 
               occupied_normal_bed INTEGER,
               occupied_oxygen_bed INTEGER, 
               location TEXT)''')
    list_of_fltc = parse_excel()
    for fltc in list_of_fltc:
        cur.execute(''' insert into FLC
                    
                    ('name', 'area', 'district', 'address', 'total_normal_bed', 
                    'total_oxygen_bed', 'occupied_normal_bed', 'occupied_oxygen_bed'
                    )
                    
                    values (?, ?, ?, ?, ?, ?, ?, ?)
                    ''', (fltc.flc_name, fltc.area, fltc.district, fltc.adress, fltc.Abeds, fltc.Aoxybeds, 
                          fltc.Obeds, fltc.OOybeds))
    con.commit()

def query_for_flc(district=None):
    con = sqlite3.connect('data/flc.db')
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    
    sql_result = []
    if (district is None):
        sql_result = cur.execute("SELECT * FROM FLC")
    else:
        sql_result = cur.execute("SELECT * FROM FLC where district = ?", (district,))
    fltc_list = []
    for row in sql_result:
        fltc = FLTC(row["id"], row["district"],row["area"] ,row["name"], row["address"],
             row["total_normal_bed"],row["total_oxygen_bed"],
             row["occupied_normal_bed"],row["occupied_oxygen_bed"] )
        fltc_list.append(fltc.__dict__)
    s = json.dumps(fltc_list)
    return s
