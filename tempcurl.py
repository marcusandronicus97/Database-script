import os
from random import randint
import time

ts = int(round(time.time() * 1000000000))


for x in range (0,100):
	value = (randint(26,72))
	ts = ts - 600000000000
	measurement = "'avg_temperature,host=server01,region=us-west value={0} {1}'".format(value,ts)
	cmd = "curl -i -XPOST 'http://localhost:8086/write?db=mydb' --data-binary "+measurement
	os.system(cmd)
	
	
	
	
