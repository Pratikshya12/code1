import mysql.connector as connector
import json
import requests

class MunicipalDataPost:
	def __init__(self):
		self.conn = connector.connect(host='localhost',port='3306',user='root',password='Selenag1997@',database='covid',auth_plugin='mysql_native_password')
		query = "create table if not exists municipality(municipalId int unique,MunicipalName varchar(200),districtId int NOT NULL,CONSTRAINT fk_districtId FOREIGN KEY(districtId) REFERENCES district(districtId))"
		cur = self.conn.cursor()
		cur.execute(query)
		self.conn.commit()	
		print("Municipality Created")

	def insert_municipality(self,id,municipal,district):
		query = "insert into municipality(municipalId,MunicipalName,districtId) values({},'{}',{})".format(id,municipal,district)
		cur = self.conn.cursor()
		cur.execute(query)
		self.conn.commit()
		print("Municipality Created")

municipal = MunicipalDataPost()
municipal_json_data = json.loads(requests.get("https://data.askbhunte.com/api/v1/municipals").text)
for municipal_data in municipal_json_data:
	municipal.insert_municipality(municipal_data.get('id'),municipal_data.get('title'),municipal_data.get('district'))
	print("Municipality added in database")