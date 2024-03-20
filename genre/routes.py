from flask import Blueprint, render_template

genre = Blueprint('genre', __name__)

@genre.route('/top_genres')
def top_genres():
    # Logic to fetch and display the user's top genres
    return render_template('top_genres.html')
