import requests
import datetime
import json
from config import EPIC_FREE_GAMES_URL

def get_free_games():
    response = requests.get(EPIC_FREE_GAMES_URL)
    
    if response.status_code != 200:
        print(f"❌ Error fetching free games: {response.status_code}")
        return []

    data = response.json()
    games = []

    for game in data.get("data", {}).get("Catalog", {}).get("searchStore", {}).get("elements", []):
        # Check if the game has a current free promotion
        promotions = game.get("promotions", {})
        if promotions and promotions.get("promotionalOffers"):
            offer = promotions["promotionalOffers"][0]["promotionalOffers"][0]
            end_date = datetime.datetime.fromisoformat(offer["endDate"][:-1])  # Remove 'Z' from ISO format
            
            games.append({
                "title": game["title"],
                "url": f'https://store.epicgames.com/en-US/p/{game["productSlug"]}',
                "end_date": end_date.strftime("%A, %B %d, %Y at %I:%M %p UTC")  # Formatted date
            })

    return games

# Testing the function
if __name__ == "__main__":
    free_games = get_free_games()
    print(json.dumps(free_games, indent=2))
