import requests
from colorama import init, Fore, Back

init()

responce = requests.get(
    'https://icanhazdadjoke.com/',
    headers={'Accept':'application/json'}
)

print( Back.WHITE + Fore.RED + 'Your dad joke: {0}'.format( responce.json()['joke']))

input("Press ENTER to continue!")
