from enum import Enum


class FinanceVersions(Enum):
    # Versions for budget & forecast
    B0 = 'B0'
    R1 = 'R1'
    R2 = 'R2'
    R3 = 'R3'
    # Versions for AR SCA
    KOS = 'KOS'
    PNH = 'PNH'
    # Version for AR SSA/AMA
    SSA = 'SSA'
    AMA = 'AMA'

