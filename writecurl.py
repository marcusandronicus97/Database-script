import os
import random
import time

ts = int(round(time.time() * 1000000000))


for x in range (0,100):
	value = (random.uniform(0,1))
	ts = ts - 600000000000
	measurement = "'cpu_load_short,host=server01,region=us-west value={0} {1}'".format(round(value,2),ts)
	cmd = "curl -i -XPOST 'http://localhost:8086/write?db=mydb' --data-binary "+measurement
	os.system(cmd)
	
