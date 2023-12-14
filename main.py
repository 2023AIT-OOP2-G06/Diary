from diaries.DiarySample import DiarySample
from diaries.MakinoDiary import MakinoDiary
from diaries.NagaoDiary import NagaoDiar
from diaries.k22133Diary import k22133Diary

# ↓のリストには、メンバーの各日記が格納されます。
diaries = [
    DiarySample(),
    MakinoDiary(),
    NagaoDiary(),
    k22133Diary()
]

for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()