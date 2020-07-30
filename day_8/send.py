import requests
import sys
from datetime import datetime

from format import format_msg


def send(name, website=None):  # name_ej, item_ej
    msg = format_msg(name_ej=name, item_ej=website)
    return msg



r = requests.get('https://heyheymycode.herokuapp.com/api/v1/2/')
print(r.json())
print(r.status_code)

if __name__ == "__main__":
    print(sys.argv)
    name = ''
    name_2 = ''
    if len(sys.argv) > 1:
        name = sys.argv[1]
        name_2 = sys.argv[2]
    response = send(name, name_2)
    print(response)