from diaries.AbstractDiary import AbstractDiary

class MakinoDiary(AbstractDiary):
    
    def get_date(self):
        return "2022-12-24"
    
    def get_summary(self):
        return "もう時期クリスマスですね。私は未来の話をしています。"
    
    def get_author(self):
        return "Makino"