import pandas as pd
from sklearn.preprocessing import StandardScaler
df = pd.read_csv("data/player_stats.csv")

#Player Value Percentages:
df["PLAYER_VALUE"] = (
    df["PTS"] * .35 +
    df["AST"] * .20 +
    df["REB"] * .20 +
    df["STL"] * .15 +
    df["BLK"] * .10
)

print(df[["PLAYER_NAME","SEASON_ID","PLAYER_VALUE"]].sort_values("PLAYER_VALUE",ascending=False).head(3))

df.to_csv("data/player_value.csv", index = False)



#NORMALIZED STATISTICS/VALUE

features = [ 
    "PTS",
    "REB",
    "AST",
    "STL",
    "BLK",
]
scaler = StandardScaler()
df[features] = scaler.fit_transform(df[features])