import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/player_stats.csv")

#Point Distrubtion Histogram 
plt.figure(figsize= (8,5))
plt.hist(df["PTS"], color="hotpink", bins = 25)

plt.title("Distrubution of Player Points")
plt.xlabel("Total Points")
plt.ylabel("Number of Players")

plt.savefig("graphs/point_distrubution.png")

#Minutes vs Points Scatter
plt.figure(figsize= (8,5))
plt.scatter(df["MIN"], df["PTS"],color="hotpink", alpha = 0.6)

plt.title("Minutes Played vs Points Scored")
plt.xlabel("Minutes Player")
plt.ylabel("Points Scored")



plt.savefig("graphs/minutes_vs_points.png")


# Assists vs Turnovers Scatter 
plt.figure(figsize= (8,5))
plt.scatter(df["AST"], df["TOV"],color="hotpink", alpha = 0.6)

plt.title("Assists vs Turnovers")
plt.xlabel("Assits")
plt.ylabel("Turnovers")



plt.savefig("graphs/assists_vs_turnovers.png")


#Top 10 scorers Bar 

top_players = df.sort_values("PTS", ascending = False).head(10)
labels = top_players["PLAYER_NAME"] + " (" + top_players["SEASON_ID"] + ")"
plt.figure(figsize =(10,6))
plt.barh(labels, top_players["PTS"], color = "hotpink" )
plt.subplots_adjust(left=0.35)
plt.title("Top 10 Highest Scoring Seasons")
plt.xlabel("Points")
plt.ylabel("Player")

plt.gca().invert_yaxis()

plt.savefig("graphs/top_scorers.png")



#Rebounds vs Blocks Scatter
plt.figure(figsize=(8,5))
plt.scatter(df["REB"], df["BLK"], color ="hotpink", alpha=0.6)

plt.title("Rebounds vs Blocks")
plt.xlabel("Rebounds")
plt.ylabel("Blocks")

plt.savefig("graphs/rebounds_vs_blocks.png")
plt.show()