from influxdb.influxdb08 import InfluxDBClient
db = InfluxDBClient('127.0.0.1', '8086', 'root', 'root', 'db1')

import datetime
import time

import sqlite3 as lite
con = lite.connect('test.db')
#con = lite.connect('test.db',detect_types=lite.PARSE_DECLTYPES)
with con:

    cur = con.cursor()
    cur.execute("SELECT os.regdt, os.sid, o.oid,o.amount,o.pid FROM Orders o inner join orderstatus os")


    while True:

        row = cur.fetchone()

        if row == None:
            break
#2015-05-03 15:48:38
#        mytime=time.mktime(datetime.datetime.strptime(row[0],'%Y-%m-%d %H:%M:%S').timetuple())
        t = datetime.datetime.strptime(row[0],'%Y-%m-%d %H:%M:%S')
        mytime=time.mktime(t.timetuple())

        data = [
                {"points":[[mytime,row[1],row[2],row[3],row[4]]],
                    "name":"orders",
                    "columns":["time","sid","oid","amount","pid"]
                    }
                ]

        db.write_points(data)
