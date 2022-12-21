import mysql.connector as connector
from fpdf import FPDF
from matplotlib import pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
from PyPDF2 import PdfMerger

con = connector.connect(host='localhost',port='3306',user='root',password='Selenag1997@',database='covid',auth_plugin='mysql_native_password')
cur = con.cursor()
district_output = {}

class District:
	def __init__(self):
		pass

	def connect_db(self,query):
		data = []
		cur.execute(query)
		for item in cur:
			data.append(item[0])
		return data

	def district_total_details(self,district):
		district_query = "select count(*) from covid.data where DistrictName = '{}'; ".format(district)
		district_total_data = self.connect_db(district_query)
		return district_total_data[0]

	def district_male_details(self,district):
		query = "select count(*) from covid.data where DistrictName = '{}' and gender = '{}' ".format(district,'male')
		district_male_data = self.connect_db(query)
		print(district_male_data)
		return district_male_data[0]

	def district_female_details(self,district):
		query = "select count(*) from covid.data where DistrictName = '{}' and gender = '{}' ".format(district,'female')
		district_female_data = self.connect_db(query)
		print(district_female_data)
		return district_female_data[0]

	def get_municipalities(self,district):
		query = "select MunicipalName from covid.municipalities where DistrictName='{}';".format(district)
		municipalities_list = self.connect_db(query)
		return municipalities_list


d1 = District()
district_name = input("Enter district name: ")
district_output.update({
	"District Total Infected " : d1.district_total_details(district_name),
	"District Male Infected" : d1.district_male_details(district_name),
	"District Female Infected" : d1.district_female_details(district_name) 
})
municipalities_list = d1.get_municipalities(district_name)
print(municipalities_list)

pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial","U",16)
pdf.cell(w=50,h=10,txt = " District Name : {} ".format(district_name),align="L",ln=1)
slices = [d1.district_male_details(district_name),d1.district_female_details(district_name)]
activities = ['Male',"Female"]
cols = ['c','m']
plt.pie(slices,labels=activities,colors=cols,startangle=90,shadow=True,radius=1,autopct='%0.1f%%')
plt.title("Pie Chart")
plt.savefig("district_graph{}.pdf".format(district_name),bbox_inches="tight",pad_inches=2,transparent=True)
for item in district_output:
	pdf.set_font("Times","I",13)
	print(item,district_output[item])
	pdf.multi_cell(w=0,h=5,txt = "{} = {} ".format(item,district_output[item]),border=1,align="L")
pdf.cell(w=0,h=20,txt = " Total Municipalities in {}:".format(district_name),align="L",ln=1)
for items in municipalities_list:
	print(items)
	pdf.multi_cell(w=0,h=10,txt = "{}".format(items),align="L")
#pdf.cell(w=0,h=10,txt = "\n\n {} \n \n".format(municipalities_list),align="L")
pdf.output("district{}.pdf".format(district_name))
pdfs = ["district_graph{}.pdf".format(district_name),"district{}.pdf".format(district_name)]
merger = PdfMerger()
for pdf in pdfs:
	merger.append(pdf)
merger.write("Total_district_{}.pdf".format(district_name))
merger.close()














