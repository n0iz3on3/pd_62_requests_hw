import requests
from pprint import pprint

def get_questions_from_stckvrflw(keyword):
    url = 'https://api.stackexchange.com/2.3/questions?fromdate=1661385600&todate=1661558400&order=desc&sort=creation&site=stackoverflow'
    response = requests.get(url).json()
    for items in response['items']:
        if keyword in items['tags']:
            pprint(items['title'])
        
get_questions_from_stckvrflw('python')