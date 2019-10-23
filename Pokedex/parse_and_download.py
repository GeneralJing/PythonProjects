from bs4 import BeautifulSoup
import argparse
import requests

ap = argparse.ArgumentParser()
ap.add_argument("-p", "--pokemon-list", required=True, help="path to where the raw Pokemon HTML resides")
ap.add_argument("-s", "--sprites", required=True, help="path to where the sprites will be stored")
args = vars(ap.parse_args())

soup = BeautifulSoup(open(args["pokemon_list"]).read())
names = []

for link in soup.findAll("a"):
    names.append(link.text)

for name in names:
    parsedName = name.lower()
    parsedName = parsedName.replace("'", "")
    parsedName = parsedName.replace(". ", "-")

    if name.find(u'\u2640') != -1:
        parsedName = "nidoran-f"
    elif name.find(u'\u2642') != -1:
        parsedName = "nidoran-m"

    print ("[x] downloading %s".format(name))
    url = "http://img.pokemondb.net/sprites/red-blue/normal/%s.png" % (parsedName)
    r = requests.get(url)
    if r.status_code!=200:
        print("[x] error downloading %s" % (name))
        continue

    f = open("%s/%s.png" % (args["sprites"], name.lower()), "wb")
    f.write(r.content)
    f.close()

