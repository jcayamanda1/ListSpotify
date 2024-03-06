import requests
from urllib.parse import urlencode
from flask import request, redirect, session, url_for
import base64

class SpotifyAPI:
    # Spotify Base URL
    base_url = "https://api.spotify.com/v1"



    def get_user_top_tracks(self, access_token):
        # Method to get the user's top tracks
        url = f"{self.base_url}/me/top/tracks"
        headers = {
            "Authorization": f"Bearer {access_token}"
        }
        r = requests.get(url, headers=headers)
        return r.json()  # Returns the user's top tracks as json
