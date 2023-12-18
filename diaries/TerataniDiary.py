from diaries.AbstractDiary import AbstractDiary

class TerataniDiary(AbstractDiary):
    
    def get_date(self):
        return "2021-12-15"
    
    def get_summary(self):
        return "なにもない一日じゃなかった"
    
    def get_author(self):
        return "Teratani"