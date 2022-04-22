import argparse
import requests, json
import sys
from sys import argv
import os

#arguments and parser

parser = argparse.ArgumentParser()

parser.add_argument ("-ip", help= "ip-info -ip (your ip)", type=str, dest='target', required=True )

args = parser.parse_args()

#colours used
red = '\033[31m'
yellow = '\033[93m'
lgreen = '\033[92m'
clear = '\033[0m'
bold = '\033[01m'
cyan = '\033[96m'

os.system("toilet -f mono12 -F gay yen yang majaze")
print (lgreen+bold+"         (...... coded by yen yang majaze .....) \n"+clear)
print (yellow+bold+"   ((.... search on telegram https://t.me/hacker1122811 ....)) \n"+clear)


ip = args.target

api = "http://ip-api.com/json/"

try:
        data = requests.get(api+ip).json()
        sys.stdout.flush()
        a = lgreen+bold+"[$]"
        b = cyan+bold+"[$]"
        print (a, "Victim", data['query'])
        print(red+"iran Anonymos"+red)
        print (b, "ISP", data['isp'])
        print(red+"iran Anonymos"+red)
        print (a, "[Organisation", data['org'])
        print(red+"yen yang mjaze"+red)
        print (b, "City", data['city'])
        print(red+"iran Anonymos"+red)
        print (a, "Region", data['region'])
        print(red+"iran Anonymos"+red)
        print (b, "Longitude", data['lon'])
        print(red+"yen yang majaze"+red)
        print (a, "Latitude", data['lat'])
        print(red+"yen yang majaze"+red)
        print (b, "Time zone", data['timezone'])
        print(red+"iran Anonymos"+red)
        print (a, "Zip code", data['zip'])
        print (" "+yellow)

except KeyboardInterrupt:
        print ('mersi'+lgreen)
        sys.exit(0)
except requests.exceptions.ConnectionError as e:
        print (red+"[~]"+" no internet ! "+clear)
sys.exit(1)