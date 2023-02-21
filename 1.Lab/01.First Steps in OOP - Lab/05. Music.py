class Music:
    def __init__(self, title, artist, lyrics):
        self.title = title
        self.artist = artist
        self.lyrics = lyrics

    def print_info(self):
        return f'This is "{self.title}" from "{self.artist}"'

    def play(self):
        return self.lyrics


song = Music("Title", "Artist", "Lyrics")
print(song.print_info())
print(song.play())

my_music = Music("Bohemian Rhapsody", "Queen", "Is this the real life? Is this just fantasy? Caught in a landslide, no escape from reality...")
print(my_music.print_info()) # This will output 'This is "Bohemian Rhapsody" from "Queen"'
print(my_music.play()) # This will output the lyrics of the music
