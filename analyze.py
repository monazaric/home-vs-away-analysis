import pandas as pd

# Load your dataset
df = pd.read_csv("sample_games.csv")  

# Split into Home and Away games
home = df[df['Location'] == 'Home']
away = df[df['Location'] == 'Away']

# Select only numeric/stat columns (excluding Game ID, Date, Location, and Opponent)
stat_columns = df.select_dtypes(include='number').columns

# Exclude GameID
stat_columns = [col for col in stat_columns if col != "GameID"]

# Calculate averages
home_avg = home[stat_columns].mean().round(2)
away_avg = away[stat_columns].mean().round(2)

# Decide which stats are better when LOWER
lower_is_better = ['Turnovers', 'PersonalFouls']

# Let user decide which stats they want compared
print("Choose a stat to compare:")
print("1. Points")
print("2. FG%")
print("3. Turnovers")
print("4. Steals")
print("4. Personal Fouls")
print("5. Assists")
choice = input("Enter number: ")

stat_map = {"1": "Points", "2": "FG%", "3": "Turnovers","4": "Steals","5": "Personal Fouls","6": "Assists"}
stat = stat_map.get(choice)

if stat:
    avg_home = df[df["Location"] == "Home"][stat].mean()
    avg_away = df[df["Location"] == "Away"][stat].mean()
    print(f"{stat} - Home: {avg_home:.2f}, Away: {avg_away:.2f}")
else:
    print("Invalid choice.")

# Stats to compare
stats_to_compare = ["Points", "FG%", "Turnovers", "Steals", "PersonalFouls"]

# Print results
print("Home Averages:")
print(home_avg)
print("\nAway Averages:")
print(away_avg)

print("\nWho performed better?")
for stat in stats_to_compare:
    home_value = home_avg.get(stat)
    away_value = away_avg.get(stat)
    
    if pd.notna(home_value) and pd.notna(away_value):
        if stat in lower_is_better:
            if home_value < away_value:
                print(f"{stat}: Home performed better")
            elif away_value < home_value:
                print(f"{stat}: Away performed better")
            else:
                print(f"{stat}: Performance was equal")
        else:
            if home_value > away_value:
                print(f"{stat}: Home performed better")
            elif away_value > home_value:
                print(f"{stat}: Away performed better")
            else:
                print(f"{stat}: Performance was equal")
    else:
        print(f"{stat}: Insufficient data for comparison")