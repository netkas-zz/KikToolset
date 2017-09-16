# Written by Netkas (Soufian Blood)

import requests
import argparse
import requests
from bs4 import BeautifulSoup

parser = argparse.ArgumentParser(description='options for Kik Email Resolver')
parser.add_argument('-u', '--username', help="Username to resolve from.")
parser.add_argument('-e', '--endpoint', help="The WS2 endpoint Location.")
args = parser.parse_args()

class Resolver(object):
    def __init__(self, args=args):
        self.args = args
        if not self.args.username:
            print('Username is not set, Use the "-h" arg for more information')
            exit()
        if not self.args.endpoint:
            print("endpoint Location is not set, use the -h arg for more information")
            exit()
        print(self.Resolve())

    def Resolve(self):
        print(' [+] Making request...')
        postheaders = {
            'Accept-Language': 'en-US,en;q=0.8',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/37.0.2062.120 Chrome/37.0.2062.120 Safari/537.36'
        }
        payload = {
            'emailOrUsername': self.args.username
        }
        Session = requests.Session()
        Response = Session.post('https://' + self.args.endpoint + '/p', data=payload, headers=postheaders)

        print(' [+] Request Success!')
        Soup = BeautifulSoup(Response.content, 'lxml')
        try:
            ErrorStats = Soup.find_all('p', class_='highlight_green')
            if "days before" in ErrorStats[0].string:
                return(" [X] You must wait 1-3 Days before making another request to this account.")
            if "is invalid" in ErrorStats[0].string:
                return(" [X] Too many requests from this IP, you are temporarily blocked.")
        except:
            print(" [!] No alert messages, Maybe it worked?")
            pass
        try:
            dataList = Soup.find_all('p')
            EmailFound = ''
            for index in range(len(dataList)):
                for word in dataList[index].string.split():
                    if "@" in word:
                        return(" [+] Success: " + word)
            print(" [!] No success messages found either. Error01")
        except:
            print(" [!] No success messages found either. Error02")
            print(" [DEBUG] ")
            print(Response.content)
            pass
        return(" [X] Unable to resolve the Kik Account")
 
if __name__ == "__main__":
    Resolver()