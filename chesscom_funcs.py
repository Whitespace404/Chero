from bs4.element import _SimpleStrainable
from chessdotcom import get_player_stats
import requests
from bs4 import BeautifulSoup

def verify_account(username):
    url = f"https://chess.com/member/{username}"
    content = requests.get(url).text()

    soup = BeautifulSoup(content, 'html.parser')
    print(soup.find(class_="profile-card-username "))

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

verify_account("thegigabyte")