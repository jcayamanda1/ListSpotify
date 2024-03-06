import requests
from urllib.parse import urlencode
from flask import request, redirect, session, url_for
import base64

class SpotifyAPI:
    # Spotify Base URL
    base_url = "https://api.spotify.com/v1"

    def __init__(self, client_id, client_secret, redirect_uri):
        self.client_id = client_id
        self.client_secret = client_secret
        self.redirect_uri = redirect_uri
        self.token_url = "https://accounts.spotify.com/api/token"
        self.auth_url = "https://accounts.spotify.com/authorize"

    def get_auth_query(self):
        # Method to get the query for authorization
        query = {
            "response_type": "code",
            "redirect_uri": self.redirect_uri,
            "scope": "user-top-read",  # Adjust the scope according to your needs
            "client_id": self.client_id
        }
        return f"{self.auth_url}?{urlencode(query)}"

    def auth_headers(self):
        # Encode Client ID and Secret for Authorization
        client_creds = f"{self.client_id}:{self.client_secret}"
        client_creds_b64 = base64.b64encode(client_creds.encode())
        return {
            "Authorization": f"Basic {client_creds_b64.decode()}"  # Basic <base64 encoded client_id:client_secret>
        }

    def auth_token(self, code):
        # Method to exchange code for an access token
        token_data = {
            "grant_type": "authorization_code",
            "code": code,
            "redirect_uri": self.redirect_uri
        }
        r = requests.post(self.token_url, data=token_data, headers=self.auth_headers())
        return r.json()  # Returns the token json response

    def get_user_top_tracks(self, access_token):
        # Method to get the user's top tracks
        url = f"{self.base_url}/me/top/tracks"
        headers = {
            "Authorization": f"Bearer {access_token}"
        }
        r = requests.get(url, headers=headers)
        return r.json()  # Returns the user's top tracks as json
