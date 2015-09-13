#!/usr/bin/env python

import MySQLdb

conn = MySQLdb.connect("192.168.0.168","root","123456","test")

cur = conn.cursor()

def addUser(username,password):
	sql = "insert into users(username,password) values('%s','%s')" %(username,password)
	cur.execute(sql)
	result = cur.fetchall()
	conn.commit()
	conn.close()
