# from utilities.email import get_email

import urllib.request

url ='https://developerservice03.herokuapp.com/dev'

# request_response = request.get(url)
response= urllib.request.urlopen(url)

def main():
    print("Hello World")

if __name__ == '__main__':
    main()


    