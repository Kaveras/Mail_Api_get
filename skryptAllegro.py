import os
import sys

try:
	from bs4 import BeautifulSoup
except:
	try:
		os.system("sudo apt install python-bs4")
	except:
		os.system("sudo apt install python3-pip")
	os.system("pip install lxml")
try:
	from terminaltables import AsciiTable
except:
	os.system("pip install terminaltables")
try:	
	import requests
except:
	os.system("pip install requests")





def Szukaj(klucz, cenaOd=0, cenaDo=0, ilestron=1, segregacja='p'):
	
	link =""
	a1=""
	a2=""
	a3=""
	licznik=0
	sourceL = []
	table_data =[['Link','Nazwa','Cena','Stan']]
	
	itemslink=[]

	if(cenaDo==cenaOd):
		link='https://allegro.pl/listing?string='+klucz
		source = requests.get(link).text
	elif(cenaOd.isdigit() & cenaDo.isdigit()):
		link='https://allegro.pl/listing?string='+klucz+'&price_from='+str(cenaOd)+'&price_to='+str(cenaDo)
		source = requests.get(link).text
		#print(link)
	else:
		print("Jakis problem !")
		exit()

	soup = BeautifulSoup(source, 'lxml')
	#print("debug ->" + soup.find("div", class_="_1bo4a _np6in _ku8d6 _3db39_14wVQ _ymwpx _nt6qd").span.text)
	if(int(soup.find("div", class_="_1bo4a _np6in _ku8d6 _3db39_14wVQ _ymwpx _nt6qd").span.text) > 1):
		if(ilestron==''):
			ilestron='1'
	else:
		ilestron='1'

	
	if(segregacja=='1'):
		segregacja='p'
	else:
		segregacja='n'
	#try:
		#print("debug2 ilestron ->"+ilestron)
	#except Exception as e1:
		#print("debug2 ilestron ->"+str(ilestron))



	for x in range(0, int(ilestron)):
		#print("debug -> weszlo do petli")
		sourceL.append(link+'&order='+segregacja+"&p="+str(x+1))
		#print("debug -> link strony w petli -> "+sourceL[x])
		source1 = requests.get(sourceL[x]).text
		soup1 = BeautifulSoup(source1, 'lxml')
		fil1 = soup1.find_all('article')
		#fil2 = fil1.select("._9c44d_3pyzl")
		#fil2 = fil1.find('section', class="_9c44d_3pyzl")
		#fil3 = fil2.text.find_all('article')
		#print ("<table style=\"width:100%\"> <tr> <th>Nazwa</th> <th>Cena</th> <th>Stan</th> <th>Link</th> </tr>")
		a1= "<table style=\"width:100%\" border=\"1\"> <tr> <th>Nazwa</th> <th>Cena</th> <th>Stan</th> <th>Link</th> </tr>"
		for eleme in fil1:
			"""try :
				head = eleme.h2.a.text
				cena = eleme.span.text
				stan = eleme.dd.text
				print(head+" "+cena+" "+stan)

				
			except Exception as e:
				#print(e)
				pass
			"""
			"""
			try :
				head = eleme.h2.a.text
				cena = eleme.span.text
				stan = eleme.dd.text
				link = eleme.h2.a.get('href')
				table_data.append([licznik,head,cena,stan])
				itemslink.append(link)
				licznik=licznik+1
				
			except Exception as e:
				#print(e)
				pass
			"""
			try:
				helper = "<a href="+eleme.h2.a.get('href')+">"+"Link Do Aukcji</a>"
				#print ("<tr> <td>"+eleme.h2.a.text+"</td> <td>"+eleme.span.text+"</td> <td>"+eleme.dd.text+"</td> <td>"+helper+"</td> </tr>")
				a2=a2+"<tr> <td>"+eleme.h2.a.text+"</td> <td>"+eleme.span.text+"</td> <td>"+eleme.dd.text+"</td> <td>"+helper+"</td> </tr>"
			except:
				pass
		#print("</table>")
		a3="</table>"
		out123=(a1+a2+a3).encode('utf-8')
		#fo = open("test.html","w")
		#fo.write(a1+a2+a3)
		#fo.close()
		print(out123)	
	

Szukaj(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5])
