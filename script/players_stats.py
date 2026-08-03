import pandas as pd
from nba_api.stats.static import players
from nba_api.stats.endpoints import playercareerstats
import time

df= pd.read_csv("data/players.csv")
df=df[df["is_active"] ==True]
all_stats = []


#Data frames for each active player
for index,row in df.iterrows():
    player_id = row["id"]
    player_name = row["full_name"]

    try:
        career = playercareerstats.PlayerCareerStats(player_id=player_id)

        stats = career.get_data_frames()[0]

        # Add the player's name to the stats table
        stats["PLAYER_NAME"] = player_name

        # Save this player's stats to our list
        all_stats.append(stats)

        print(f"Finished: {player_name}")

        time.sleep(0.6)

    except Exception as e:
        print(f"Skipped {player_name}: {e}")

# Combine all players into one DataFrame
player_stats = pd.concat(all_stats, ignore_index=True)

# Save the final dataset
player_stats.to_csv("data/player_stats.csv", index=False)

print("Finished!")

