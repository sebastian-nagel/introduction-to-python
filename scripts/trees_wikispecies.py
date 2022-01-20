import json
import os.path

import pandas as pd
import requests

output = 'data/trees-wikispecies.json'

tree_cadastre_file = './data/KN_Baumkataster_2020.csv'
df = pd.read_csv(tree_cadastre_file)

N = 500
top_trees = df['Name_lat'].value_counts().head(500).to_frame()


# some tree names are too specific or are listed by synonyms
tree_synonyms = {
    'Platanus x acerifolia': 'Platanus × hispanica',
    'Thuja orientalis': 'Platycladus orientalis',
}

query_params = {
    'action': 'query',
    'format': 'json',
    'prop': 'iwlinks|langlinks|description',
    'lllimit': 300,
    'llprop': 'url|langname'
}

trees_wikispecies = {}
if os.path.exists(output):
    # update
    trees_wikispecies = json.load(open(output))

for tree in top_trees.index.to_list():
    q = tree
    if q in tree_synonyms:
        q = tree_synonyms[q]
    while True:
        if q in trees_wikispecies:
            print("Already done:", q)
            if tree != q:
                trees_wikispecies[tree] = trees_wikispecies[q]
            break
        print("Querying API for", q)
        query_params['titles'] = q.replace(' ', '_')
        response = requests.get('https://species.wikimedia.org/w/api.php',
                                params=query_params)
        data = json.loads(response.text)
        if "-1" in data["query"]["pages"]:
            print("Nothing found for", q)
            if "'" in q:
                # try without the variety in single quotes
                #  Fagus sylvatica 'Asplenifolia'
                q = q[:q.index("'")].rstrip()
                continue
            if " x " in q:
                # try without the " x "
                #  Prunus x serrulata
                #  => Prunus serrulata
                q = q.replace(" x ", " ")
                continue
            if " ssp. " in q:
                # try without the supspecies
                q = q[:q.index(" ssp. ")].rstrip()
                continue
        else:
            trees_wikispecies[tree] = data
            trees_wikispecies[q] = trees_wikispecies[tree]
        break

with open('data/trees-wikispecies.json', 'w') as fp:
    json.dump(trees_wikispecies, fp)
