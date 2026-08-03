from nba_api.stats.static import players

#GET ALL PLAYERS 
#Turns CSV into a list of dictionaries instead 
nba_players = players.get_players()

print("Active NBA Atheletes:")
for player in nba_players:
    if player["is_active"]:
        print(player["full_name"])
   