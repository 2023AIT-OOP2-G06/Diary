from diaries.DiarySample import DiarySample
from diaries.HiranoDiary import HiranoDiary
from diaries.MakinoDiary import MakinoDiary
from diaries.tsugeDiary import tsugeDiary
from diaries.NagaoDiary import NagaoDiary
from diaries.k22133Diary import k22133Diary
from diaries.TomonoriDiary import TomonoriDiary
from diaries.TerataniDiary import TerataniDiary
from diaries.SuzukiDiary import SuzukiDiary

# ↓のリストには、メンバーの各日記が格納されます。
diaries = [
    DiarySample(),
    MakinoDiary(),
    tsugeDiary(),
    NagaoDiary(),
    k22133Diary(),
    TomonoriDiary(),
    HiranoDiary(),
    TerataniDiary(),
    SuzukiDiary(),
]


for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()