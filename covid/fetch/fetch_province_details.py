import mysql.connector as connector
from fpdf import FPDF
from matplotlib import pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
from PyPDF2 import PdfMerger
# from collections import defaultdict


con = connector.connect(host='localhost',port='3306',user='root',password='Selenag1997@',database='covid',auth_plugin='mysql_native_password')
cur = con.cursor()
province_list = {1:'Province 1',2:'Madesh',3:'Bagmati',4:'Gandaki',5:'Lumbini',6:'Karnali',7:'Sudhur Paschim'}
province_output = {}


class Province:
	# con = connector.connect(host='localhost',port='3306',user='root',password='Sweepr@123',database='covid',auth_plugin='mysql_native_password')
	# cur = con.cursor()
	def __init__(self):
		pass
		# self.con = connector.connect(host='localhost',port='3306',user='root',password='Sweepr@123',database='covid',auth_plugin='mysql_native_password')
		# cur = self.con.cursor()

	
	def connect_db(self,query):
		data = []
		cur.execute(query)
		for item in cur:
			data.append(item[0])
		return data

	def get_districts(self,province_no):
		district_query = "select DistrictName from covid.district where provinceId = {} ;".format(province_no)
		district_list = self.connect_db(district_query)
		return district_list

	def get_municipality(self,district_list):
		provincial_municipality_list = {}
		for districts in district_list:
			municipality_query = "select MunicipalName from covid.municipalities where DistrictName='{}';".format(districts)
			municipality_list = self.connect_db(municipality_query)
			provincial_municipality_list.update({districts : municipality_list})
		return provincial_municipality_list


	def province_total_details(self,province_no):
		province_query = "select count(*) from covid.data where ProvinceName = '{}'; ".format(province_list[province_no])
		province_total_data = self.connect_db(province_query)
		print(province_total_data)
		return province_total_data[0]

	def province_male_details(self,province_no):
		query = "select count(*) from covid.data where ProvinceName = '{}' and gender = '{}' ".format(province_list[province_no],'male')
		province_male_data = self.connect_db(query)
		print(province_male_data)
		return province_male_data[0]


	def province_female_details(self,province_no):
		query = "select count(*) from covid.data where ProvinceName = '{}' and gender = '{}' ".format(province_list[province_no],'female')
		province_female_data = self.connect_db(query)
		print(province_female_data)
		return province_female_data[0]



p1 = Province()
province_num = int(input("Enter province no"))
# p1.province_female_details(num)
# p1.province_male_details(num)
# new = p1.get_municipality(p1.get_districts(num))
#print(new)
province_output.update({'Total Infected People': p1.province_total_details(province_num),
	'Total Male Infected':p1.province_male_details(province_num),
	'Total Female Infected' : p1.province_female_details(province_num),
	'Total Districts' :p1.get_districts(province_num)
	})
#print(province_output)

municipalities = p1.get_municipality(p1.get_districts(province_num))
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial","B",16)
pdf.cell(w=50,h=0,txt = "Province no : {}\n\n\n\n".format(province_num),align="C",ln=1)
slices = [p1.province_male_details(province_num),p1.province_female_details(province_num)]
activities = ['Male',"Female"]
cols = ['c','m']
plt.pie(slices,labels=activities,colors=cols,startangle=90,shadow=True,radius=1,autopct='%0.1f%%')
plt.title("Pie Chart")
plt.savefig("province_graph{}.pdf".format(province_num),bbox_inches="tight",pad_inches=2,transparent=True)
for item in province_output:
	pdf.set_font("Times","I",13)
	print(item,province_output[item])
	pdf.multi_cell(w=0,h=10,txt = "{} = {} ".format(item,province_output[item]),border=1,align="L")
for items in municipalities:
	print(items,municipalities[items])
	pdf.multi_cell(w=0,h=10,txt = "Total Municipalities of {} =  {} \n \n".format(items,municipalities[items]),align="L")
pdf.output("province{}.pdf".format(province_num))
pdfs = ["province_graph{}.pdf".format(province_num),"province{}.pdf".format(province_num)]
merger = PdfMerger()
for pdf in pdfs:
	merger.append(pdf)
merger.write("Total_province_{}.pdf".format(province_num))
merger.close()




