import mysql.connector as connector
import json
import requests

class ProvinceDataPost:
	def __init__(self):
		self.con = connector.connect(host='localhost',port='3306',user='root',password='Selenag1997@',database='covid',auth_plugin='mysql_native_password')
		query = "create table if not exists province(provinceId int not null auto_increment,ProvinceName varchar(50),primary key(provinceId));"
		cur = self.con.cursor()
		cur.execute(query)
		print("province Created")

	def insert_province(self,province):
		query = "insert into province(ProvinceName) values('{}')".format(province)
		cur = self.con.cursor()
		cur.execute(query)
		self.con.commit()
		print("Province added")


province = ["Province 1","Madesh","Bagmati","Gandaki","Lumbini","Karnali","Sudhur Paschim"]
pr1 = ProvinceDataPost()
for item in province:
	pr1.insert_province(item)
	print("{} is added to database".format(item))