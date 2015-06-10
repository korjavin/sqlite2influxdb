from influxdb.influxdb08 import InfluxDBClient
db = InfluxDBClient('127.0.0.1', '8086', 'root', 'root', 'db1')

data = [
  {"points":[[1],[2]],
   "name":"orders",
   "columns":["a"]
  }
]

db.write_points(data)
