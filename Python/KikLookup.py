# Written by Netkas (Soufian Blood)

import requests
import argparse
import requests
import json

parser = argparse.ArgumentParser(description='options for Kik Lookup')
parser.add_argument('-u', '--username', help="Username to grab information from")
parser.add_argument('-e', '--endpoint', help="The WS2 endpoint Location.")
args = parser.parse_args()

class Lookup(object):
    def __init__(self, args=args):
        self.args = args
        if not self.args.username:
            print('Username is not set, Use the "-h" arg for more information')
            exit()
        if not self.args.endpoint:
            print("endpoint Location is not set, use the -h arg for more information")
            exit()
        Results = self.Query()
        try:
            if Results['firstName']:
                print(' [+] FirstName: ' + Results['firstName'])
            else:
                print(' [x] FirstName not found')
        except:
            print(' [!] Invalid encoding in FirstName')
            pass
        try:
            if Results['lastName']:
                print(' [+] LastName: ' + Results['lastName'])
            else:
                print(' [x] LastName not found')
        except:
            print(' [!] Invalid encoding in LastName')
            pass
        try:
            if Results['displayPicLastModified']:
                print(' [+] Display Pic Last Modified: ' + str(Results['displayPicLastModified']))
            else:
                print(' [x] Display Pic Last Modified not found')
        except:
            print(' [!] Invalid encoding in Display Pic Last Modified')
            pass
        try:
            if Results['displayPic']:
                print(' [+] Display Pic URL: ' + Results['displayPic'])
            else:
                print(' [x] Display Pic URL not found')
        except:
            print(' [!] Invalid encoding in Display Pic URL')
            pass

    def Query(self):
        print(' [+] Making request...')
        getheaders = {
            'Accept-Language': 'en-US,en;q=0.8',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/37.0.2062.120 Chrome/37.0.2062.120 Safari/537.36'
        }
        Session = requests.Session()
        Response = Session.get('https://' + self.args.endpoint + '/user/' + self.args.username, headers=getheaders)

        print(' [+] Request Success!')
        return json.loads(Response.content.decode('utf-8'))
 
if __name__ == "__main__":
    Lookup()