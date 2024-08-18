import pandas as pd
import numpy as np
from flask import render_template, request
from app import app, model
from app.spotify_client import get_id_from_url, get_track_features, get_required_track_analysis, get_track_info

app.app_context().push()


@app.route('/')
def layout():
    return render_template('layout.html')


@app.route('/home', methods=['GET'])
def home():
    return render_template('home.html', title='Home')


@app.route('/about')
def about():
    return render_template('about.html', title='About')


@app.route('/prediction_result')
def prediction_result():
    model_output = {}
    features = ['artist','danceability', 'energy', 'key', 'loudness', 'mode', 'speechiness', 'acousticness',
    'instrumentalness', 'liveness', 'valence', 'tempo', 'duration_ms', 'time_signature', 'chorus_hit','sections', 'num_artists', 'release_type']
    song_url = request.args.get('song_url')
    song_id = get_id_from_url(song_url)
    track_features = get_track_features(song_id)
    analysis_attrs = get_required_track_analysis(song_id)
    # artist, track_name, album, image_url = get_track_info(song_id)
    artists, track_name, album, image_url, release_type = get_track_info(song_id)
    num_artists = len(artists)
    artist = artists[0]['name']
    
    input_list = [artist] + track_features + analysis_attrs + [num_artists, release_type]
    
    model_input = {}
    
    for i, feature in enumerate(features):
        model_input[feature] = input_list[i]

    input_df = pd.DataFrame(model_input, index=[0])

    pred = model.predict(input_df)
    
    model_output['artist'] = artist
    model_output['album'] = album
    model_output['image_url'] = image_url
    model_output['track_name'] = track_name
    model_output['song_url'] = song_url
    
    if pred == 1:
        model_output['output'] = f'Congrats! Your song is predicted to be a hit'
    else:
        model_output['output'] = f'Unfortunately, your song is predicted to be a flop'
    
    return render_template('prediction_result.html', title='Result', model=model_output)


@app.route('/prediction')
def prediction():
    return render_template('prediction.html', title='Predict')


@app.route('/history')
def history():
    data = None
    return render_template('history.html', data=data, title='Previous Searches')







