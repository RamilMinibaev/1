import pandas as pd
data = pd.read_csv ("nba.csv")
for key, value in data.items():
    print(key, value)
    print()