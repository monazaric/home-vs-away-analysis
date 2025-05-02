import pandas as pd

# Load dataset
df = pd.read_csv("season_games.csv")

# Select numeric/stat columns, excluding GameID
stat_columns = df.select_dtypes(include='number').columns
stat_columns = [col for col in stat_columns if col != "GameID"]

# Lower-is-better stats
lower_is_better = ['Turnovers', 'Personal Fouls']

# Ask user for comparison type
mode = input("Would you like to compare ALL games or SELECT games? (Enter 'all' or 'select'): ").strip().lower()

if mode == 'select':
    # Show available games
    print("\nAvailable games:")
    for idx, row in df.iterrows():
        print(f"{row['GameID']}: Opponent: {row['Opponent']}, Location: {row['Location']}, Date: {row['Date']}")
    
    # Ask for selected GameIDs (comma-separated)
    selected_ids = input("\nEnter the GameIDs of the games you'd like to compare (separated by commas): ")
    selected_ids = [int(id.strip()) for id in selected_ids.split(',') if id.strip().isdigit()]
    
    selected_games = df[df['GameID'].isin(selected_ids)]
    
    if selected_games.empty:
        print("No valid games selected.")
    else:
        # Split selected games into Home and Away
        home = selected_games[selected_games['Location'] == 'Home']
        away = selected_games[selected_games['Location'] == 'Away']
        
        # Calculate averages
        home_avg = home[stat_columns].mean().round(2)
        away_avg = away[stat_columns].mean().round(2)
        
        print("\nSelected Home Game Averages:")
        print(home_avg)
        
        print("\nSelected Away Game Averages:")
        print(away_avg)
        
        # Compare selected games
        print("\nWho performed better?")
        for stat in stat_columns:
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
else:
    # Use existing ALL games logic
    home = df[df['Location'] == 'Home']
    away = df[df['Location'] == 'Away']
    
    home_avg = home[stat_columns].mean().round(2)
    away_avg = away[stat_columns].mean().round(2)
    
    print("\nHome Averages:")
    print(home_avg)
    
    print("\nAway Averages:")
    print(away_avg)
    
    print("\nWho performed better?")
    for stat in stat_columns:
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