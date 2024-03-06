from flask import Blueprint, render_template

music = Blueprint('music', __name__)

@music.route('/most_streamed')
def most_streamed():
    # Logic to fetch and display the user's most streamed songs
    return render_template('most_streamed.html')
