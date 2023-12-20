from diaries.DiarySample import DiarySample
from diaries.NagaoDiary import NagaoDiary
from diaries.MakinoDiary import MakinoDiary
from diaries.tsugeDiary import tsugeDiary

# ↓のリストには、メンバーの各日記が格納されます。
diaries = [
    DiarySample(),
    NagaoDiary(),
    MakinoDiary(),
    tsugeDiary(),
]

for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()