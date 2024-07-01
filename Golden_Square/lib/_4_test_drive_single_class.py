
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
                self.current_word_index = 0 