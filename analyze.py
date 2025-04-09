import pandas as pd

# Load your dataset
df = pd.read_csv("sample_games.csv")  

# Split into Home and Away games
home = df[df['Location'] == 'Home']
away = df[df['Location'] == 'Away']

# Select only numeric/stat columns (excluding Game ID, Date, Location, and Opponent)
stat_columns = df.select_dtypes(include='number').columns

# Calculate averages
home_avg = home[stat_columns].mean().round(2)
away_avg = away[stat_columns].mean().round(2)

# Decide which stats are better when LOWER
lower_is_better = ['Turnovers']

# Print results
print("Home Averages:")
print(home_avg)
print("\nAway Averages:")
print(away_avg)

print("\nWho performed better?")
for stat in stat_columns:
    if stat in lower_is_better:
        better = 'Home' if home_avg[stat] < away_avg[stat] else 'Away'
    else:
        better = 'Home' if home_avg[stat] > away_avg[stat] else 'Away'
    
    print(f"{stat}: {better} performed better")