from lib._6_test_drive_class_system import *

def test_initialisation():
    library = MusicLibrary()
    assert library.tracks == []

def test_add_track():
    library = MusicLibrary()
    library.add("Bohemian Rhapsody")
    assert library.tracks == ["Bohemian Rhapsody"]

def test_search_by_title_exact_match():
    library = MusicLibrary()
    library.add("Bohemian Rhapsody")
    library.add("Another One Bites the Dust")
    library.add("Killer Queen")
    result = library.search_by_title("Killer Queen")
    assert result == ["Killer Queen"]

def test_search_by_title_partial_match():
    library = MusicLibrary()
    library.add("Bohemian Rhapsody")
    library.add("Another One Bites the Dust")
    library.add("Killer Queen")
    result = library.search_by_title("Queen")
    assert result == ["Killer Queen"]

def test_search_by_title_case_insensitive():
    library = MusicLibrary()
    library.add("Bohemian Rhapsody")
    library.add("Another One Bites the Dust")
    library.add("Killer Queen")
    result = library.search_by_title("queen")
    assert result == ["Killer Queen"]

def test_search_by_title_no_match():
    library = MusicLibrary()
    library.add("Bohemian Rhapsody")
    library.add("Another One Bites the Dust")
    library.add("Killer Queen")
    result = library.search_by_title("Jazz")
    assert result == []

# Track class

def test_initialisation():
    track = Track("Imagine", "John Lennon")
    assert track.title == "Imagine"
    assert track.artist == "John Lennon"

def test_format():
    track = Track("Imagine", "John Lennon")
    assert track.format() == "Imagine by John Lennon"