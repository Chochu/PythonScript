import mysql.connector
import requests
import json


def main():
  #League API Key
  Key = "899fd29c-1b5e-435f-821b-6aa28087af60"
  #Set connection
  cnx = mysql.connector.connect(user='Test', password='123', host='127.0.0.1', database='leagueoflegend')

  cursor = cnx.cursor()

  #Set url address
  URL = "https://na.api.pvp.net/api/lol/na/v1.2/champion?freeToPlay=false&api_key=899fd29c-1b5e-435f-821b-6aa28087af60"
  #Get request
  response = requests.get(URL)
  #Header of sql command
  header = "INSERT INTO `leagueoflegend`.`champion`(`idChampion`,`Key`,`name`,`title`) VALUES"
  #Check response
  if response.status_code != 404:
    for e in response.json()['champions']: #loop each champion and execute command to add to table
      ChampInfoURL = "https://global.api.pvp.net/api/lol/static-data/na/v1.2/champion/"+str(e['id'])+"?api_key="+Key
      Champinfo = (requests.get(ChampInfoURL)).json()

      text = "('" + str(Champinfo['id']) + "','"+ str(Champinfo['key']).replace("'","\\'") + "','"+ str(Champinfo['name']).replace("'","\\'") + "','"+ str(Champinfo['title']).replace("'","\\'") + "')"
      print("Inserting "+ text)
      cursor.execute(header + text)
      cnx.commit()

    cursor.close()
    cnx.close()

if __name__ == "__main__":
  main()
