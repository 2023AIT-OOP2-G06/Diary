from diaries.AbstractDiary import AbstractDiary

class SuzukiDiary(AbstractDiary):
    
    def get_date(self):
        return "2023-12-20"
    
    def get_summary(self):
        return "ずっと頭が痛いです"
    
    def get_author(self):
        return "Suzuki"