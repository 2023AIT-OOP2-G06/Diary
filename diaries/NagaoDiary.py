from diaries.AbstractDiary import AbstractDiary

class DiarySample(AbstractDiary):
    
    def get_date(self):
        return "2021-12-14"
    
    def get_summary(self):
        return "風邪ひいてて呼吸がしんどい"
    
    def get_author(self):
        return "Nagao"