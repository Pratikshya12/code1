import mysql.connector as connector
import json
import requests

class DistrictDataPost:
	def __init__(self):
		self.con = connector.connect(host='localhost',port='3306',user='root',password='Selenag1997@',database='covid',auth_plugin='mysql_native_password')
		query = 'create table if not exists district(districtId int unique,DistrictName varchar(100),provinceId int,CONSTRAINT fk_provinceId FOREIGN KEY(provinceId) REFERENCES province(provinceId))'
		cur = self.con.cursor()
		cur.execute(query)
		self.con.commit()
		print("Created")

	def insert_district(self,id,district,province):
		query = "insert into district(districtId,DistrictName,provinceId) values({},'{}',{})".format(
			id,district,province)
		print(query)
		cur = self.con.cursor()
		cur.execute(query)
		self.con.commit()
		print("district saved to db")


district = DistrictDataPost()
response = requests.get("https://data.askbhunte.com/api/v1/districts")
print(response.text)
district_json_data = json.loads(response.text)
for district_data in district_json_data: 
	district.insert_district(district_data.get('id'),district_data.get('code'),district_data.get('province'))
	print("District with id : ",str(district_data.get('id')))