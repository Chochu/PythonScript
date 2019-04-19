import requests
import csv
import time
import sys
desc = "Description"
def isMember(item_ID):
    global desc
    URL = "http://services.runescape.com/m=itemdb_oldschool/api/catalogue/detail.json?item=" + str(item_ID)
    response = requests.get(URL)
    #check if the page exist
    #print(response)
    if response.status_code != 404:
        desc = str(response.json()['item']['description'])
        if (response.json()['item']['members'] == "true"):
            return "True"
        else:
            return "False"
    else:
        desc = "NULL"
        return "Not Tradable"    

def main(startID):
    filew = open('myfile.csv','a')
    with open('OSRS Item.csv', newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            if int(row[0]) < int(startID):
                continue
            print ("Checking "+ row[1]+"...")
            try:
                row[3] = isMember(str(row[0]))
            except:
                filew.close()
                time.sleep(2)
                return row[0];
            row[4] = desc
            filew.write(str(row[0])+ ","+str(row[1])+ ","+str(row[2])+ ","+str(row[3])+ ","+str(row[4])+"\n")
    filew.close()
    
if __name__ == "__main__":
    startID = 0
    while(int(startID) < 7709):
        startID = main(startID)
    
