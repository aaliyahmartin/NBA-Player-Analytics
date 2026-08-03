import pandas as pd
df =pd.read_csv("data/player_stats.csv")

corr = df.corr(numeric_only= True)
pts_corr= corr["PTS"].sort_values(ascending=False)
pts_corr.to_csv("data/points_correlation.csv")


import matplotlib.pyplot as plt

plt.figure(figsize=(12,10))
plt.imshow(corr, aspect="auto")

plt.colorbar()

plt.xticks(range(len(corr.columns)), corr.columns, rotation=90)
plt.yticks(range(len(corr.columns)), corr.columns)

plt.title("Correlation Matrix")

plt.tight_layout()

plt.savefig("graphs/correlation_heatmap.png")
plt.show()