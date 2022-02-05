import ssl
import sqlite3

try:
    import dateutil as parser
except: pass

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

conn = sqlite3.connect('content.sqlite')
cur = conn.cursor()

baseurl = "https://data.cityofnewyork.us/resource/uvpi-gqnh.json"

cur.execute('''CREATE TABLE IF NOT EXISTS Tree_Data
    (id INTEGER UNIQUE, tree_id INTEGER, created_at TEXT,
     tree_dbh INTEGER, status TEXT, spc_latin TEXT,
     spc_common TEXT, address TEXT, postcode INTEGER,
     zip_city TEXT, borocode INTEGER, borough TEXT,
     nta TEXT, nta_name: TEXT, latitude REAL,
     longitute REAL)''')

start = None
cur.execute('SELECT max(id) FROM Messages')
try:
    row = cur.fetchone()
    if row is None:
        start = 0
    else:
        start = row[0]
except:
    start = 0

if start is None:
    start = 0