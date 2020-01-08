## Import
import speedtest
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from time import time,strftime,gmtime

## Paramètres
servers = []
# If you want to test against a specific server

threads = None
# If you want to use a single threaded test

test = True
# If you want to do the speedtest or just test the rest of the code

## Code

#Connect to google servers
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('/home/pi/Speedtest-Home/client_secret.json', scope)
client = gspread.authorize(creds)

if test == True:
  # Do a speedtest.
  print("Warning Speedtesting: You may encounter some slowlyness while the test is running.")
  s = speedtest.Speedtest()
  s.get_servers(servers)
  s.get_best_server()
  s.download(threads=threads)
  s.upload(threads=threads)
  print("Speedtest Done !!!")
  s.results.share()
  results_dict = s.results.dict()

# print(results_dict)

sheet = client.open("Speedtest-Home").sheet1

# print([ strftime("%H:%M:%S", gmtime()), strftime("%x"), results_dict["ping"], results_dict["download"]/1000000, results_dict["upload"]/1000000 ])

if test == True:
  print("Uploading Results")
  sheet.insert_row([
                    strftime("%H:%M:%S", gmtime()),
                    strftime("%x"),
                    results_dict["ping"],
                    round(results_dict["download"]/1000000 ,3),
                    round(results_dict["upload"]/1000000 ,3)
                    ], 2)
  print("Results Uploaded")
