"""
Lab 7, APIs and data collection
Joseph Ali-Shaw
September 28,2026
"""
import pandas as pd


# ----------------------------
# 1. Example DataFrame
# ----------------------------
dict_ = {'a': [11, 21, 31], 'b': [12, 22, 32]}
df = pd.DataFrame(dict_)
print(df.head())
print(df.mean())

from static import get_teams
nba_teams = get_teams()
# ----------------------------
# 2. Get NBA teams
# ----------------------------
nba_teams = get_teams()
print(f"First 2 teams: {nba_teams[:2]}") # Show first 2 teams as a preview
# Convert list of dicts -> DataFrame
df_teams = pd.DataFrame(nba_teams)
print(df_teams.head())

df_warriors = df_teams[['id']].values[0][0]
print(f"Id of Warriors = {df_warriors}")

# ----------------------------
# 3. Working with external API
# ----------------------------
# a. Download the pickle file
import requests
url = "https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/Chapter%205/Labs/Golden_State.pkl"
file_name = "Golden_State.pkl"
print("\nDownloading external data...")
response = requests.get(url)
if response.status_code == 200:
    with open(file_name, "wb") as f:
        f.write(response.content)
    print("Download complete.")
else:
    print("Download failed.")

# b. Load DataFrame from pickle
games = pd.read_pickle(file_name)
print("\nGames data from pickle file:")
print(games.head())

# c. Filter GSW vs Raptors
warriors_vs_raptors = games[games['MATCHUP'].str.contains('TOR')]
gsw_home_vs_raptors = warriors_vs_raptors[warriors_vs_raptors['MATCHUP'].str.contains(' vs. ')]
gsw_away_vs_raptors = warriors_vs_raptors[warriors_vs_raptors['MATCHUP'].str.contains(' @ ')]

# d. Calculate averages
home_avg_plus = gsw_home_vs_raptors['PLUS_MINUS'].mean()
away_avg_plus = gsw_away_vs_raptors['PLUS_MINUS'].mean()
home_avg_pts = gsw_home_vs_raptors['PTS'].mean()
away_avg_pts = gsw_away_vs_raptors['PTS'].mean()

print(f"Warriors home average {home_avg_plus}")
print(f"Warriors away average {away_avg_plus}")
print(f"Warriors home points average {home_avg_pts}")
print(f"Warriors away points average {away_avg_pts}")

print('------ LAB EXERCISE-------')
# a
url = "https://datahub.io/core/english-premier-league/r/season-2324.csv"
file_name = "epl_matches.csv"
print("\nDownloading external data...")
response = requests.get(url)
if response.status_code == 200:
    with open(file_name, "wb") as f:
        f.write(response.content)
    print("Download complete.")
else:
    print("Download failed.")

# b.
epl_df = pd.read_csv(file_name)
print("\nEPL Matches data from CSV file:")
print(epl_df.head())

# c.
arsenal_vs_chelsea = epl_df[ ((epl_df["HomeTeam"] == "Arsenal") & (epl_df["AwayTeam"] == "Chelsea")) | ((epl_df["HomeTeam"] == "Chelsea") & (epl_df["AwayTeam"] == "Arsenal"))]
arsenal_home = arsenal_vs_chelsea[arsenal_vs_chelsea["HomeTeam"] == "Arsenal"]
arsenal_away = arsenal_vs_chelsea[arsenal_vs_chelsea["AwayTeam"] == "Arsenal"]

# d. 
home_avg_pts = arsenal_home["FTHG"].mean()
away_avg_pts = arsenal_away["FTAG"].mean() 
home_avg_diff = (arsenal_home["FTHG"] - arsenal_home["FTAG"]).mean()
away_avg_diff = (arsenal_away["FTAG"] - arsenal_away["FTHG"]).mean()

print(f"Arsenal home goals average vs Chelsea: {home_avg_pts}")
print(f"Arsenal away goals average vs Chelsea: {away_avg_pts}")
print(f"Arsenal home goal difference average: {home_avg_diff}")
print(f"Arsenal away goal difference average: {away_avg_diff}")