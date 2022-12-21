import time
import mysql.connector as connector
from fpdf import FPDF
from matplotlib import pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
from PyPDF2 import PdfMerger

from fetch_and_post_to_db import *

def connect_db(query):
	con = connector.connect(host='localhost',port='3306',user='root',password='Selenag1997@',database='covid',auth_plugin='mysql_native_password')
	cur = con.cursor(query)
	for item in cur:
		print(item)



print("Getting COVID Data of Provinces, District , Municipality \n")
time.sleep(2)
print("\n_________________________________________________________________________________________________________\n")

choice = input("Enter p for Province,d for District ,m for Municipality : \n")
if choice == "p":
	from fetch.fetch_province_details import *
elif choice == "d":
	from fetch.fetch_district_details import *
elif choice == "m":
	from fetch.fetch_municipality_details import *
else:
	print("wrong Selection")
