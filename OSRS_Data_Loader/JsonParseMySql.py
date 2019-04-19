import requests
import json
import re
import mysql.connector

def main():
    cnx = mysql.connector.connect(user='Test', password='123', host='127.0.0.1', database='leagueoflegend')
    cursor = cnx.cursor()
    URL = "https://rsbuddy.com/exchange/summary.json"
    
    response = requests.get(URL)

    #Clean Up
    m = (re.sub(r'\"\d+\":','',response.text))
    m = "{\"Item\":[" + m[1:]
    m = m[:-1] + "]}"
    
    #parse into json
    jfile = json.loads(m)
##    filew = open("teds.txt","a")
##    filew.write(str(jfile))

    #Store to database
    header = "INSERT INTO runescape.item VALUES"
    for e in jfile['Item']:
        footer = "('" + str(e['sp']) + "','"+ str(e['members']) + "','"+ str(e['sell_average']) + "','"+ str(e['buy_average']) + "','"+ str(e['overall_average']) + "','"+ str(e['id']) + "','"+ str(e['name']).replace("'","\\'") + "')"
        print(footer)
        cursor.execute(header + footer)
        cnx.commit()
    cursor.close()
    cnx.close()
    
if __name__ == "__main__":
  main()
