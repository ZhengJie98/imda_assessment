import sqlite3
import pandas as pd

conn = sqlite3.connect("ramen-ratings.db")

c = conn.cursor()

drop_table_query = '''DROP TABLE IF EXISTS RAMEN_RATINGS'''
c.execute(drop_table_query)


sql_query = ''' CREATE TABLE RAMEN_RATINGS (
    db_ID integer PRIMARY KEY autoincrement,
    ID integer,
    Country text,
    Brand text,
    Type text,
    Package text,
    Rating float
    )
    '''

c.execute(sql_query)

ramen_csv = pd.read_csv('ramen-ratings.csv')
ramen_csv.to_sql('RAMEN_RATINGS', conn, if_exists='append', index = False)
