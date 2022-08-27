import requests

superheroes_list = ["Hulk", "Captain america", "Thanos"]

def get_superhero(names):
    response = requests.get("https://akabab.github.io/superhero-api/api/all.json").json()
    superheroes_dict = {}
    for superhero in response:
        if superhero["name"] in names:
            superheroes_dict[superhero["name"]] = superhero["powerstats"]["intelligence"]
    print(f'Most Intelligence - {max(superheroes_dict, key=superheroes_dict.get)}')

get_superhero(superheroes_list)