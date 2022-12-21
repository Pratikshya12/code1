import mysql.connector as connector
import json
import requests

class Infected:
    def __init__(self):
        self.con = connector.connect(host='localhost',port='3306',user='root',password='Selenag1997@',database='covid',auth_plugin='mysql_native_password')
        print(self.con)
        query = "create table if not exists infected(infected_Id INT NOT NULL AUTO_INCREMENT,provinceId int,districtID int NOT NULL,municipalId int NOT NULL,gender varchar(10),ward int,PRIMARY KEY(infected_Id),CONSTRAINT fk_infected_provinceId FOREIGN KEY(provinceId) REFERENCES province(provinceId),CONSTRAINT fk_infected_districtId FOREIGN KEY(districtId) REFERENCES district(districtId),CONSTRAINT fk_municipal_municipalId FOREIGN KEY(municipalId) REFERENCES municipality(municipalId))"
        cur = self.con.cursor()
        print(cur)
        cur.execute(query)
        self.con.commit()
        print("Created")

    def insert_infected(self,province,district,municipal,gender,ward):
        query = "insert into infected(provinceId,districtId,municipalId,gender,ward) values({},{},{},'{}',{})".format(province,district,municipal,gender,ward)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("Infected data Created")



infected = Infected()
infected_json_data = json.loads(requests.get("https://data.askbhunte.com/api/v1/covid").text)
for infected_data in infected_json_data:
    infected.insert_infected(infected_data.get('province'),infected_data.get('district'),infected_data.get('municipality'),infected_data.get('gender'),infected_data.get('ward'))
    print("infected added in database")	
