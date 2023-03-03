import billboard
import plotly.express as px
import lyricsgenius
import pandas as pd


# Warning: This code will take a long time to run you can change the number of songs to 10 and not more than 100
NUMBER_OF_SONGS = 100
'''
define a function that return the 100 songs from the Hot 100 of the Billboard using billboard.py
'''
def get_hot_100_songs():
    chart = billboard.ChartData('hot-100')[0:NUMBER_OF_SONGS]
    return chart


'''
define a function that chart from the Hot 100 of the Billboard as a parameter
and return a list of the 100 songs lyrics using lyricsgenius
'''
def get_songs_lyrics(chart):
    # Get the lyrics of each song from Genius
    genius = lyricsgenius.Genius("x_ApCOemXCM80lez6bpRdYiuu--j3qsTjMOdl6AaEsKzCZe5o7zSS6qkdHyCerUT")
    songs = []
    for song in chart:
        try:
            lyrics = genius.search_song(song.title, song.artist).lyrics
        except AttributeError:
            lyrics = None
        songs.append({'title': song.title, 'artist': song.artist, 'lyrics': lyrics})
    return songs


'''
define a function that get a list of songs from the lyricsgenius as a parameter
and count for each word in the song lyrics how many times it appears in the 100 songs
the function  return a dictionary of the 100 most common words in the 100 songs and their count
'''
def count_words_in_lyrics(songs):
    # Create a dictionary of the 100 most common words in the 100 songs and their count
    words_count = {}
    for song in songs:
        if song['lyrics'] is not None:
            for word in song['lyrics'].split():
                if word in words_count:
                    words_count[word] += 1
                else:
                    words_count[word] = 1
    # filter the dictionary to get only the 100 most common words
    words_count = dict(sorted(words_count.items(), key=lambda item: item[1], reverse=True)[:100])
    return words_count


'''
define a function that get dictionary of words and their count as a parameter
the function will create a graph of the words and their count using plotly.express
'''
def plot_words_count(words_count):
    # create a graph of the words and their count using plotly.express
    # create a data frame of the words and their count
    df = pd.DataFrame(words_count.items(), columns=['word', 'count'])
    # plot the data frame
    fig = px.bar(df, x='word', y='count')
    fig.show()



chart = get_hot_100_songs()
songs = get_songs_lyrics(chart)
words_count = count_words_in_lyrics(songs)

# plot the data frame
plot_words_count(words_count)
