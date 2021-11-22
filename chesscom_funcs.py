#from bs4.element import _SimpleStrainable
from chessdotcom import get_player_stats
import requests
from bs4 import BeautifulSoup

def verify_account(username):
    url = f"https://chess.com/member/{username}"
    content = requests.get(url).text

    soup = BeautifulSoup(content, 'html.parser')
    profile_card = soup.find(class_="profile-card-location")
    
    try:
        location_text = profile_card.text.rstrip().lstrip().lower()
    except AttributeError: # that means that they have not set a location (it will return None and Python will not be able to .rstrip(None))
        return False

    if location_text == "chero-verify":
        return True
    return False

def get_rapid_rating(username):
    player = get_player_stats(username)
    rapid_rating = player.stats.chess_rapid.last.rating

    return rapid_rating

def get_bullet_rating(username):
    player = get_player_stats(username)
    bullet_rating = player.stats.chess_bullet.last.rating

    return bullet_rating

def get_blitz_rating(username):
    player = get_player_stats(username)
    blitz_rating = player.stats.chess_blitz.last.rating
    
    return blitz_rating
