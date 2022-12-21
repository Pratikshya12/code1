# import time
# from fetch.fetch_province_details import Province
# from fetch.fetch_district_details import District



# con = connector.connect(host='localhost',port='3306',user='root',password='Sweepr@123',database='covid',auth_plugin='mysql_native_password')
# cur = con.cursor()
# def connect_db(self,query):
# 	data = []
# 	cur.execute(query)
# 	for item in cur:
# 		data.append(item[0])
# 	return data


# print("Getting COVID Data of Provinces, District , Municipality \n")
# time.sleep(2)
# print("\n_________________________________________________________________________________________________________\n")
# print("Enter p for Province , d for District , m for Municipality \n")
# choice = input("")
# if choice == "p":
# 	province_output = {}
# 	province_list = {1:'Province 1',2:'Madesh',3:'Bagmati',4:'Gandaki',5:'Lumbini',6:'Karnali',7:'Sudhur Paschim'}
# 	print("Here are suggestions of Provinces for you\n")
# 	time.sleep(2)
# 	print("_____________________________________________________________________________________________\n")
# 	query = "select ProvinceName from covid.province;"
# 	provinces_list = connect_db(query)
# 	for p in provinces_list:
# 		print(p,end="")
# 	province_num = int(input("Enter province no : "))
# 	if province_num > 0 && province_num < 8 :
# 		p1 = Province()
# 		province_output.update({'Total Infected People': p1.province_total_details(province_num),
# 			'Total Male Infected':p1.province_male_details(province_num),
# 			'Total Female Infected' : p1.province_female_details(province_num),
# 			'Total Districts' :p1.get_districts(province_num)
# 		})
# 		#print(province_output)

# 		municipalities = p1.get_municipality(p1.get_districts(province_num))
# 		pdf = FPDF()
# 		pdf.add_page()
# 		pdf.set_font("Arial","B",16)
# 		pdf.cell(w=50,h=0,txt = "Province no : {}\n\n\n\n".format(province_num),align="L")
# 		slices = [p1.province_male_details(province_num),p1.province_female_details(province_num)]
# 		activities = ['Male',"Female"]
# 		cols = ['c','m']
# 		plt.pie(slices,labels=activities,colors=cols,startangle=90,shadow=True,radius=1,autopct='%0.1f%%')
# 		plt.title("Pie Chart")
# 		plt.savefig("province_graph{}.pdf".format(province_num),bbox_inches="tight",pad_inches=2,transparent=True)
# 		for item in province_output:
# 			pdf.set_font("Arial","I",16)
# 			print(item,province_output[item])
# 			pdf.multi_cell(w=0,h=10,txt = " \n{} = {} ".format(item,province_output[item]),align="L")
# 		for items in municipalities:
# 			print(items,municipalities[items])
# 			pdf.multi_cell(w=0,h=10,txt = "\n\n Total Municipalities of {} =  {} \n \n".format(items,municipalities[items]),align="C")
# 		pdf.output("province{}.pdf".format(province_num))
# 		pdfs = ["province_graph{}.pdf".format(province_num),"province{}.pdf".format(province_num)]
# 		merger = PdfMerger()	
# 		for pdf in pdfs:
# 			merger.append(pdf)
# 			merger.write("Total_province_{}.pdf".format(province_num))
# 		merger.close()

# 	else:
# 		print("Wrong input on province number")

# elif choice == "d":



