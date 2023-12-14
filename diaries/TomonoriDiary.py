from diaries.AbstractDiary import AbstractDiary
class TomonoriDiary(AbstractDiary):
    def get_date(self):
        return "2023-12-14"
    def get_summary(self):
        return """風邪気味"""
    def get_author(self):
        return "Tomonori"