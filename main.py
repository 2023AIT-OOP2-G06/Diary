from diaries.DiarySample import DiarySample
from diaries.NagaoDiary import NagaoDiary
from diaries.MakinoDiary import MakinoDiary

# ↓のリストには、メンバーの各日記が格納されます。
diaries = [
    DiarySample(),
    NagaoDiary(),
    MakinoDiary(),
]

for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()