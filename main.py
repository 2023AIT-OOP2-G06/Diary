from diaries.DiarySample import DiarySample
from diaries.HiranoDiary import HiranoDiary
from diaries.MakinoDiary import MakinoDiary
from diaries.NagaoDiary import NagaoDiary
from diaries.k22133Diary import k22133Diary
from diaries.TomonoriDiary import TomonoriDiary

# ↓のリストには、メンバーの各日記が格納されます。
diaries = [
    DiarySample(),
    MakinoDiary(),
    NagaoDiary(),
    k22133Diary(),
    TomonoriDiary(),
    HiranoDiary(),
]


for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()