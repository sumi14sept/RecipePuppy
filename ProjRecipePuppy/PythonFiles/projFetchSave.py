import sqlite3
import json
import urllib

def main():
    raw=getData('http://www.recipepuppy.com/api/') #fetch data from API
    data_list=loadData(raw) #load Json Data
    saveData(data_list) #Save datalist to the database
    print("Data is saved successfully")

#load Json data into a list object    
def loadData(raw):
    json_object = json.load(raw)
    listResult=json_object["results"]
    data_list=[]
    for data in listResult:       
        data_list.append(tuple(data.values()))
    return data_list

#fetch Data from RecipePuppy Api
def getData(url):
    try:
        f = urllib.request.urlopen(url)
    except Exception as e:
        print(str(e))
    return f

#Save Data in dbRecipes database
def  saveData(data_list):
    try:
       con = sqlite3.connect('dbRecipes.db')
       c = con.cursor()
    
    
    # Insert data list to the tblRecipePuppy table
       c.executemany('INSERT INTO tblRecipePuppy VALUES (?,?,?,?)', data_list)

    # Save (commit) the changes
       con.commit()
    except Exception as e:
        print(str(e))
    #close the connection
    con.close() 
    
    
main()