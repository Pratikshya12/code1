import mysql.connector as connector

con = connector.connect(host='localhost',port='3306',user='root',password='Selenag1997@',database='covid',auth_plugin='mysql_native_password')
cur = con.cursor()

class DbManipulator:
	con = connector.connect(host='localhost',port='3306',user='root',password='Selenag1997@',database='covid',auth_plugin='mysql_native_password')
	cur = con.cursor()
	def __init__(self):
		pass
		# self.con = connector.connect(host='localhost',port='3306',user='root',password='Sweepr@123',database='covid',auth_plugin='mysql_native_password')
		# cur = self.con.cursor()

	
	def connect_db(self,query):
		cur.execute(query)
		con.commit()

	def create_and_insert_new_municipalities_tables(self,*args,**kwargs):
		query = "create table municipalities(municipalId int,MunicipalName varchar(100),DistrictName varchar(100));"
		self.connect_db(query)
		query = "Insert into municipalities(municipalId,MunicipalName,DistrictName) select m.municipalId,m.MunicipalName,d.DistrictName from municipality m left join district d on m.districtId=d.districtId"
		print("New table created named municipalities")
		self.connect_db(query)
		print("new table created")

	def create_and_insert_new_infected_tables(self,*args,**kwargs):
		query = "create table data(infected_Id int not null auto_increment,ProvinceName varchar(50),DistrictName varchar(100),MunicipalName varchar(150),gender varchar(10),ward int,primary key(infected_Id));"
		self.connect_db(query)
		query = "Insert into data(ProvinceName,DistrictName,MunicipalName,gender,ward) select p.ProvinceName,d.DistrictName,m.MunicipalName,i.gender,i.ward from infected i left join province p on i.provinceId = p.provinceId left join district d on i.districtId = d.districtId left join municipality m on i.municipalId = m.municipalId;"
		self.connect_db(query)
		print("New Table Created")


db1 = DbManipulator()
db1.create_and_insert_new_municipalities_tables()
db1.create_and_insert_new_infected_tables()
print("\n Fetching from API is now completed lets move ahead.")




