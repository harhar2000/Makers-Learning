
class MusicLibrary:

    def __init__(self):
        self.tracks = []     

    def add(self, track):
        self.tracks.append(track)
    
    def search_by_title(self, keyword):
        return [track for track in self.tracks if keyword.lower() in track.lower()]


library = MusicLibrary()
library.add("Bohemian Rhapsody")
library.add("Another One Bites the Dust")
library.add("Killer Queen")

print(library.search_by_title("queen"))  # Expected: ['Killer Queen']
print(library.search_by_title("bohemian"))  # Expected: ['Bohemian Rhapsody']



class Track:

    def __init__(self, title, artist):
        self.title = title
        self.artist = artist

    def format(self):
        return f"{self.title} by {self.artist}"


track = Track("Bohemian Rhapsody", "Queen")
print(track.format())