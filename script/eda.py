import pandas as pd

df = pd.read_csv("data/player_stats.csv")
print(df.columns)
print(df.head())
print(df.info())
print(df.describe())

# NO missing values within data set 
print(df.isnull().sum())

top_players = df.sort_values("PTS", ascending = False, ignore_index= True)
print("Top 10 Scoring Active NBA Athletes")
print(top_players[["PLAYER_NAME", "SEASON_ID", "PTS"]].head(10))


#NBA AVERAGES 
print("Average Points", round(df["PTS"].mean(),2))
print("Average Assists", round(df["AST"].mean(),2))
print("Average Rebounds", round(df["REB"].mean(),2))

#NBA EXTREMES
highest_score = df.loc[df["PTS"].idxmax()]
highest_assist = df.loc[df["AST"].idxmax()]
highest_rebound = df.loc[df["REB"].idxmax()]

print("Highest Scorer \n")
print("Player:", highest_score["PLAYER_NAME"])
print("Season:", highest_score["SEASON_ID"])
print("Rebounds:", highest_score["PTS"])
print("Above average:", highest_score["PTS"] -  round(df["PTS"].mean(),2),"\n")

print("Highest Assists \n")
print("Player:", highest_assist["PLAYER_NAME"])
print("Season:", highest_assist["SEASON_ID"])
print("Rebounds:", highest_assist["AST"])
print("Above average:", highest_assist["AST"] -  round(df["AST"].mean(),2),"\n")

print("Highest Rebounder \n")
print("Player:", highest_rebound["PLAYER_NAME"])
print("Season:", highest_rebound["SEASON_ID"])
print("Rebounds:", highest_rebound["REB"])
print("Above average:", highest_rebound["REB"] -  round(df["REB"].mean(),2))