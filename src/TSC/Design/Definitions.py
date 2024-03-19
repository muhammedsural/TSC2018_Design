from enum import Enum

class SeismicResistanceBuildingsClass(Enum):
    A11 = 1
    A12 = 2
    A13 = 3
    A14 = 5
    A15 = 6
    A16 = 7
    A21 = 8
    A22 = 9
    A23 = 10
    A24 = 11
    A31 = 12
    A32 = 13
    A33 = 14
    B11 = 15
    B12 = 16
    B13 = 17
    B14 = 18
    B15 = 19
    B21 = 20
    B31 = 21
    B32 = 22
    B33 = 23
    B34 = 24
    C11 = 25
    C12 = 26
    C13 = 27
    C14 = 28
    C15 = 29
    C16 = 30
    C21 = 31
    C22 = 32
    C31 = 33
    C32 = 34
    C33 = 35
    D1  = 36
    D2  = 37
    E11 = 38
    E12 = 39
    E21 = 40
    E22 = 41
    F1  = 42
    F2  = 43


class SeismicDesignClass(Enum):
    one     = 1
    one_a   = 2
    two     = 3
    two_a   = 4
    three   = 5
    three_a = 6
    four    = 7
    four_a  = 8

class DuctilityLevel(Enum):
    Yuksek  = 0
    Karma   = 1
    Sinirli = 2

class ResSystemType(Enum):
    BACerceve           = 0
    BABoslukluPerde     = 1
    BABosluksuzPerde    = 2
    BAKarma             = 3
    CECerceve           = 4
    CEMerkeziCapraz     = 5
    CEDisMerkeziCapraz  = 6
    CEKarma             = 7

class SlabSystem(Enum):
    Plak_kirisli        = 0
    Plak_kirissiz       = 1
    TekDogrultuluDisli  = 2
    CiftDogrultuluDisli = 3
    Kaset               = 4
    Waffle              = 5
