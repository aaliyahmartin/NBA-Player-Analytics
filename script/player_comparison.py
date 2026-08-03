import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/player_value.csv")

player1 = "Stephen Curry"
player2 = "LeBron James"

comparison = df[
    df["PLAYER_NAME"].isin([player1, player2])
]


career_comparison = comparison.groupby("PLAYER_NAME")[
    ["PTS", "REB", "AST", "STL", "BLK", "PLAYER_VALUE"]
].mean()

print(career_comparison)
