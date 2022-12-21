import mysql.connector as connector
from fpdf import FPDF
from matplotlib import pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
from PyPDF2 import PdfMerger

con = connector.connect(host='localhost',port='3306',user='root',password='Selenag1997@',database='covid',auth_plugin='mysql_native_password')
cur = con.cursor()
municipality_output = {}

class Municipality:
	def __init__(self):
		pass

	def connect_db(self,query):
		data = []
		cur.execute(query)
		for item in cur:
			data.append(item[0])
		return data

	def municipality_total_details(self,DistrictName,MunicipalName):
		municipality_query = "select count(*) from covid.data where DistrictName = '{}' and MunicipalName = '{}'; ".format(DistrictName,MunicipalName)
		municipality_total_data = self.connect_db(municipality_query)
		return municipality_total_data[0]

	def municipality_male_details(self,DistrictName,MunicipalName):
		query = "select count(*) from covid.data where DistrictName = '{}' and MunicipalName = '{}' and gender = '{}' ".format(DistrictName,MunicipalName,'male')
		municipality_male_data = self.connect_db(query)
		print(municipality_male_data)
		return municipality_male_data[0]

	def municipality_female_details(self,DistrictName,MunicipalName):
		query = "select count(*) from covid.data where DistrictName = '{}' and MunicipalName = '{}' and gender = '{}' ".format(DistrictName,MunicipalName,'female')
		municipality_female_data = self.connect_db(query)
		print(municipality_female_data)
		return municipality_female_data[0]


m1 = Municipality()
DistrictName = input("Enter district name where municipality lies : ")
MunicipalName = input("Enter municipality name : ")
municipality_output.update({
	"{} Municipality  Total Infected ".format(MunicipalName) : m1.municipality_total_details(DistrictName,MunicipalName),
	"{} Municipality  Male Infected".format(MunicipalName) : m1.municipality_male_details(DistrictName,MunicipalName),
	"{} Municipality Female Infected".format(MunicipalName) : m1.municipality_female_details(DistrictName,MunicipalName) 
})
print(municipality_output)

pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial","B",16)
pdf.cell(w=50,h=0,txt = "District Name : {}\n".format(DistrictName),align="L",ln=1)
pdf.cell(w=50,h=10,txt = "Municipality Name : {} \n".format(MunicipalName),align="L",ln=1)
slices = [m1.municipality_male_details(DistrictName,MunicipalName),m1.municipality_female_details(DistrictName,MunicipalName)]
activities = ["Male","Female"]
cols = ['c','m']
plt.pie(slices,labels=activities,colors=cols,startangle=90,shadow=True,radius=1,autopct='%0.1f%%')
plt.title("Pie Chart")
plt.savefig("{}_{}graph.pdf".format(DistrictName,MunicipalName),bbox_inches="tight",pad_inches=2,transparent=True)
for item in municipality_output:
	pdf.set_font("Times","I",13)
	print(item,municipality_output[item])
	pdf.multi_cell(w=0,h=20,txt = " {} = {} ".format(item,municipality_output[item]),border=1,align="L")
pdf.output("{}_{}.pdf".format(DistrictName,MunicipalName))
pdfs = ["{}_{}graph.pdf".format(DistrictName,MunicipalName),"{}_{}.pdf".format(DistrictName,MunicipalName)]
merger = PdfMerger()
for pdf in pdfs:
	merger.append(pdf)
merger.write("Total_Details_{}_{}.pdf".format(DistrictName,MunicipalName))
merger.close()


