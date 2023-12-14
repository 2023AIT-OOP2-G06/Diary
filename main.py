from diaries.DiarySample import DiarySample
from diaries.k22133Diary import k22133Diary

# ↓のリストには、メンバーの各日記が格納されます。
diaries = [
    DiarySample(), 
    k22133Diary()
]

for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()