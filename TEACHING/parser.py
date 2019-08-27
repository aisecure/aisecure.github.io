
from bs4 import BeautifulSoup
from pdb import set_trace as st
import numpy as np
from datetime import datetime
# with open("2019.html", 'r') as fid:
# 	content = fid.read()
# soup = BeautifulSoup(content, 'html.parser')
# # print(soup.prettify())
# # st()
# tag = soup.find(id="wsb-canvas-template-page")
# store_list = []
# for child in tag.children:
# 	# print(child)
# 	store_list.append(child)
# new_list = []
# for cont in store_list[1].contents:
# 	try:
# 		out_str = cont.prettify(formatter='html')
# 		if "wsb-element-text" in out_str :
# 			if " Special Topics on " in out_str:
# 				continue
# 			elif "Useful Links" in out_str:
# 				continue
# 			elif "Paper Presentation Guidelines:" in out_str:
# 				continue
# 			elif "Goal of the clas" in out_str:
# 				continue
# 			elif "Course Schedule (Tentative)" in out_str:
# 				continue
# 			elif "Syllabus" in out_str:
# 				continue
# 			elif "class is to introduce" in out_str:
# 				continue
# 			new_list.append(out_str)
# 	except:
# 		pass
# print( "".join(new_list) )

with open("tmp.html", 'r') as fid:
	content = fid.read()
soup = BeautifulSoup(content, 'html.parser')
new_list = []
cont_list = []
for cont in soup.contents:
	try:
		date = cont.span.span.span.get_text().strip().split('\xa0')[0]
		new_list.append(date)
		cont_list.append(cont)
	except Exception as e:
		pass
date_list = []
for date in new_list:
	date_list.append( datetime.strptime(date, "%m/%d" ) )
ids = np.argsort(date_list) 
# print(np.array(new_list)[ids])
for idx in ids:
	print( cont_list[idx].prettify(formatter="html"))