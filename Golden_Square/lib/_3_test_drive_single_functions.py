# leap_year = True
# non_leap_year = False

# if years % 400 == 0, years == True
# if years % 100 == 0 and years % 400 == 1, years == False
# if years % 4 == 0 and years % 100 == 1, years == True
# if years % 4 == 1, years == False

def leap_year(years):
    if not isinstance(years, int) or years == 0:
        return False
    if years % 400 == 0:
        return True
    elif years % 100 == 0 and years % 400 != 0:
        return False
    elif years % 4 == 0 and years % 100 != 0:
        return True
    elif years % 4 != 0:
        return False





def make_snippet(string):
    words = string.split()
    if len(words) > 5:
        return " ".join(words[:5]) + "..."
    else:
        return string



def count_words(string):
    words = string.split()
    return len(words)


def estimate_reading_time(text, wpm=200):
    words = text.split()
    num_words = len(words)
    reading_time = num_words / wpm
    return reading_time

def put_text_in_capital_and_end_punctually(text):
    if not text[0].isupper():
        return False
    if text[-1] not in ['.', '!', '?']:
        return False
    return True