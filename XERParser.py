from msilib import Table
import re
import json
import copy
from tkinter import CURRENT

from xml.sax.saxutils import prepare_input_source
XERFile = open("ScheduleExport.xer", "r")
count = 0
counttable = 0

class XERTable:
    def __init__(self, tablename, columns, rowcontent):
        tablename = ""
        columns = []
        rowcontent = []

xer_overall_dict = {
    
    }

xer_table_dict = {
    "table_name": "",
    "columns": [],
    "rows": []
    }

TableArray = []

current_tablename = ""
current_Columns = []
current_rows = []
current_rowcontent = []
item_count = 0
temp_column_rowpair = {
        }
for item in XERFile:
    
    if "%T" in item:
        #get name of table
        if current_tablename == "":
            current_tablename = item[3:len(item)]
            item_count += 1
            print(str(item_count))
        else:
            #now we take the column rowpair and fill it out
            temp_column_rowpair_arr = []
            #we get all our rows
            for row in current_rows:
                # we take the first row
             
             for index,val in enumerate(row):
                  # we take each value in that row
                  #we get the index of that value
                temp_column_rowpair[list(temp_column_rowpair.keys())[index]] = val
             temp_column_rowpair_arr.append(copy.deepcopy(temp_column_rowpair))


            #now we copy it to our table array
            temp_xer_dict = {
                "table_name": "",
                "content" : ""
            }
            temp_xer_dict["table_name"] = copy.deepcopy(current_tablename)
            temp_xer_dict["content"] = copy.deepcopy(temp_column_rowpair_arr)
            TableArray.append(temp_xer_dict)
           # xer_overall_dict.update({item_count:xer_table_dict})
            
            current_Columns.clear()
            current_rows.clear()
            current_tablename = ""
            current_tablename = item[3:len(item)]
            item_count += 1
            print(str(item_count))
    if "%F" in item:
       current_Columns =  re.split('	', item)
       current_Columns.remove('%F')
       temp_column_rowpair = dict.fromkeys(current_Columns)
       print (current_Columns)
    if "%R" in item:
        current_rowcontent = re.split('	', item)
        current_rowcontent.remove('%R')
        current_rows.append(current_rowcontent)
        
        
with open("test.json", "w") as outfile:
    stringjson = json.dumps(TableArray).replace('','0')
    json.dump(json.loads(stringjson), outfile)


print(str(count))
print(str(counttable))





XERFile.close()


# get the tables separated out and identified and grouped with their columns and then their contents
#for item in XERFile:
#    temp_column_rowpair = {
#        }
#    if "%T" in item:
        #get name of table
#        if current_tablename == "":
 #           current_tablename = item[3:len(item)]
  #          item_count += 1
   #         print(str(item_count))
    #    else:
#            temp_xer_dict = {
 #               "table_name": "",
  #              "columns": [],
   #             "rows": []}
    #        temp_xer_dict["table_name"] = copy.deepcopy(current_tablename)
#            temp_xer_dict["columns"] = copy.deepcopy(current_Columns)
 #           temp_xer_dict["rows"] = copy.deepcopy(current_rows)
  #          TableArray.append(temp_xer_dict)
           # xer_overall_dict.update({item_count:xer_table_dict})
            
#            current_Columns.clear()
 #           current_rows.clear()
  #          current_tablename = ""
   #         current_tablename = item[3:len(item)]
    #        item_count += 1
     #       print(str(item_count))
   # if "%F" in item:
    #   current_Columns =  re.split('	', item)
     #  current_Columns.remove('%F')
      # print (current_Columns)
 #   if "%R" in item:
  #      current_rowcontent = re.split('	', item)
   #     current_rowcontent.remove('%R')
    #    current_rows.append(current_rowcontent)