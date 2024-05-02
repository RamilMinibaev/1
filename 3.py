import pandas as pd
dict = {'name': ["aparna", "pankaj", "sudhir", "Geeku"],
        'degree': ["MBA", "BCA", "M.Tech", "MBA"],
        'score': [90, 40, 80, 98]}
df = pd.DataFrame (dict)
for key, value in df.items():
    print(key, value)
    print()
