import pandas as pd
from sklearn.preprocessing import StandardScaler

df = pd.read_csv("data/player_stats.csv")


# NORMALIZE STATISTICS

features = [
    "PTS",
    "REB",
    "AST",
    "STL",
    "BLK"
]

scaler = StandardScaler()

scaled_features = scaler.fit_transform(df[features])

scaled_df = pd.DataFrame(
    scaled_features,
    columns=[
        "PTS_scaled",
        "REB_scaled",
        "AST_scaled",
        "STL_scaled",
        "BLK_scaled"
    ]
)

df = pd.concat([df, scaled_df], axis=1)


# CREATE PLAYER VALUE USING NORMALIZED STATS

df["PLAYER_VALUE"] = (
    df["PTS_scaled"] * .35 +
    df["AST_scaled"] * .20 +
    df["REB_scaled"] * .20 +
    df["STL_scaled"] * .15 +
    df["BLK_scaled"] * .10
)


# CHECK RESULTS

print(
    df[
        ["PLAYER_NAME", "SEASON_ID", "PLAYER_VALUE"]
    ]
    .sort_values("PLAYER_VALUE", ascending=False)
    .head(10)
)


# SAVE FINAL DATASET

df.to_csv("data/player_value.csv", index=False)