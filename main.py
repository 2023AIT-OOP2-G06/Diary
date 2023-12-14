from diaries.DiarySample import DiarySample
from diaries.MakinoDiary import MakinoDiary
from diaries.NagaoDiary import NagaoDiary

# ↓のリストには、メンバーの各日記が格納されます。
diaries = [
    DiarySample(),
    MakinoDiary(),
    NagaoDiary(),
]

for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()