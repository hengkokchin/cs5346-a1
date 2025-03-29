import pandas as pd

df = pd.read_csv('billboard_1990.csv')

final = []

for i in list(df['Genre'].unique()):
    children = []

    for j, r in df[df['Genre'] == i]['Subgenre'].value_counts().reset_index(name='counts').iterrows():
        children.append({
            "name": r['Subgenre'],
            "value": r['counts']
        })
    final.append({
        "name": i,
        "children": children
    })

final_json = {
    "name": "billboard_1990",
    "children": final
}

print(final_json)
