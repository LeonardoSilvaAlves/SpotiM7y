from flask import Flask, render_template, request
import spotipy
from spotipy.oauth2 import SpotifyOAuth

app = Flask(__name__)

# Configuração da autenticação do Spotify
client_id = '5c6a85cb9cb6434789a3a53bc5c5fd50'
client_secret = 'a5552359231642cbaebe85fc065ae860'
redirect_uri = 'http://localhost:5000/callback'  # URL de redirecionamento após a autenticação
scope = 'user-library-read playlist-modify-private'

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id,
                                               client_secret=client_secret,
                                               redirect_uri=redirect_uri,
                                               scope=scope))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/callback')
def callback():
    # Lógica para lidar com a resposta da autenticação do Spotify
    return 'Callback route'

@app.route('/search', methods=['POST'])
def search():
    search_query = request.form['search_query']
    results = sp.search(q=search_query, type='track')
    # Lógica para processar os resultados da pesquisa e retornar os dados relevantes
    return render_template('search_results.html', results=results)

@app.route('/create_playlist', methods=['POST'])
def create_playlist():
    playlist_name = request.form['playlist_name']
    # Lógica para criar uma playlist no Spotify com base nos parâmetros fornecidos
    return 'Playlist created'

@app.route('/adjust_preferences', methods=['POST'])
def adjust_preferences():
    # Lógica para ajustar as preferências de música com base no feedback do usuário

    # Retorne uma resposta ou redirecione para uma página relevante após ajustar as preferências
    return 'Preferences adjusted'

if __name__ == '__main__':
    app.run(debug=True)
