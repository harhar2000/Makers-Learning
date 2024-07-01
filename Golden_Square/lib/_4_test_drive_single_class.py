
class DiaryEntry:
    def __init__(self, title, contents):
        self.title = title
        self.contents = contents
        self.words = self.contents.split()
        self.current_word_index = 0

    def format(self):
        return f"{self.title}: {self.contents}"

    def count_words(self):
        return len(self.contents.split())

    def reading_time(self, wpm):
        word_count = self.count_words()
        return (word_count + wpm -1) // wpm

    def reading_chunk(self, wpm, minutes):
        total_words_can_read = wpm * minutes
        start_index = self.current_word_index
        end_index = start_index + total_words_can_read
        chunk = ' '.join(self.words[start_index:end_index])
        
        self.current_word_index = end_index
        if self.current_word_index >= len(self.words):
            self.current_word_index = 0  # Reset for next reading cycle

        return chunk


class GrammarStats:
    def __init__(self):
        self.total_texts = 0
        self.valid_texts = 0

    def check(self, text):
        self.total_texts += 1
        if text and text[0].isupper() and text.endswith('.'):
            self.valid_texts += 1
            return True
        else:
            return False

    def percentage_good(self):
        if self.total_texts == 0:
            return 0
        return int((self.valid_texts / self.total_texts) * 100)
